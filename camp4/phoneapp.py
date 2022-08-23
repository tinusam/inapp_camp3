import re
import pyodbc


conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-7IPO8LB\SQLEXPRESS;Database=contacts_db;Trusted_Connection=yes;')

myCursor = conn.cursor()


def searchNo():
    n = input('Number to search: ')
    try:
        myCursor.execute(
            'SELECT name, phone FROM Contacts WHERE Phone=?',
            (n)
        )
    except:
        print('Failed to get contacts')
    else:
        contacts = myCursor.fetchall()
        if len(contacts) > 0:
            print('Contacts:')
            for name, phone in contacts:
                print(f'{name}: {phone}\n')
        else:
            print('Number not found')


def searchName():
    n = input('Name to search: ')
    try:
        myCursor.execute(
            'SELECT name, phone FROM Contacts WHERE Name LIKE ?',
            (n)
        )
    except:
        print('Failed to get contacts')
    else:
        contacts = myCursor.fetchall()
        if len(contacts) > 0:
            print('Contacts:')
            for name, phone in contacts:
                print(f'{name}: {phone}\n')

def add():
    while(True):
        name = input('Enter name: ').strip()
        if ',' in name:
            print(', not allowed in name')
        else:
            break
    while(True):
        number = input('Enter number: ').strip()
        if re.match(r'[0-9]*', number):
            break
        else:
            print('Invalid input')
    try:
        myCursor.execute(
            'INSERT INTO Contacts VALUES (?, ?);',
            (name, number)
        )
        conn.commit()
    except:
        print('Failed to add contact')
    else:
        print('Contact added')

def delete():
    name = input('Enter name to delete: ')
    try:
        myCursor.execute(
            'DELETE FROM Contacts WHERE Name=?',
            (name)
        )
        conn.commit()
    except:
        print('Failed to delete')
    else:
        if myCursor.rowcount > 0:
            print('Deleted')
        else:
            print(f'{name} does not exist')

def sort():
    try:
        myCursor.execute('SELECT Name, Phone FROM Contacts ORDER BY Name;')
    except:
        print('Failed to fetch contacts')
    else:
        contacts = myCursor.fetchall()
        if len(contacts) > 0:
            print('Contacts:')
            for name, phone in contacts:
                print(f'{name}: {phone}\n')


while(True):
    
    print('1. List the contacts')
    print('2. Add new contact')
    print('3. Delete a contact')
    print('4. Search by name')
    print('5. Search by number')
    print('6. Exit')
    
    opt = int(input('> '))
    match opt:
        case 1: sort()
        case 2: add()
        case 3: delete()
        case 4: searchName()
        case 5: searchNo()
        case 6: break
        case _: print('Invalid input')

conn.close()
