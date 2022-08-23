from flask import Flask, render_template
#import the classl
app = Flask(__name__)

@app.route('/')
def user(name):
    return render_template('user.html', username = name)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)