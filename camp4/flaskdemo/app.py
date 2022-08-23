#importing Flask class from flask llibrary
from flask import Flask,redirect, url_for, request, render_template, jsonify, abort


app = Flask(__name__)



@app.route("/")
def hello_world():
    return """<p>Hello, World!</p>
    <button onclick="window.location.href='/greet'">Greet</button>
    <button onclick="window.location.href='/user/admin'">Admin</button>
    
    """

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '123':
        return 'hello admin'
    else:
        return 'hello guest'

books = [
    {   'id': 1,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J.K. Rowling',
        'year': 1997
    },
    {   'id': 2,
        'title': 'Jurassic Park',
        'author': 'Michael Crichton',
        'year': 1993
    },
    {   'id': 3,
        'title': 'The Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'year': 1954
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books':books})

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    #lsit comprehension
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book':book[0]})

@app.route('/books', methods=['POST'])
def create_book():
    if not request.json:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author'],
        'year': request.json['year']
    }
    books.append(book)
    return jsonify({'book':book}), 201
    
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'author' in request.json and type(request.json['author']) is not str:
        abort(400)
    if 'year' in request.json and type(request.json['year']) is not int:
        abort(400)
    book[0]['title'] = request.json['title']
    book[0]['author'] = request.json['author']
    book[0]['year'] = request.json['year']
    return jsonify({'book':book[0]})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    books.remove(book[0])
    return jsonify({'result':True})

    books.remove(book[0])
    return jsonify({'status':'deleted'})
    
API_URL = ('https://api.genderize.io/?name={}')

#create a new function for sending the api request to the url
def send_api(name):
    print(API_URL)
    #TRYING TO SEND THE API REQUEST USING REQUEST.GET()METHOD
    try:
        data = requests.get(API_URL.format(name)).json()
    except Exception as exec:
        print(exec)
        data=None
    return data


#if we are using browser, the default http method will be GET4
@app.route('/gender/<name>')
def gender(name):
    #call the send_api method and pass the name and receive the response
    response=send_api(name)
    return_text="your name"+response["name"]+


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
