#!C:\ProgramData\Anaconda3\python.exe

import os
import sys
import cgi
import cgitb
import html
try:
    import msvcrt
    msvcrt.setmode(0,os.O_BINARY)
    msvcrt.setmode(1,os.O_BINARY)
except ImportError:
    print("<p>No msvcrt module found<p>")


# interpretors
# 'office' : '#!C:\Users\Prince Johnson\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe',
# 'home' : '#!C:\ProgramData\Anaconda3\python.exe'


print("Content-type: text/html\n\n")

cgitb.enable()
form = cgi.FieldStorage()
name = form.getvalue('name')
mail = form.getvalue('email')
password = form.getvalue('password')
emotions  = form.getlist('emotions')
satisfaction = form.getvalue('satisfied')
comments = form.getvalue('comment')
photo = form['bio-photo']

if photo.filename:
    photo_data = photo.file.read()
    fn = os.path.basename(photo.filename)
    open ('files/'+fn, 'wb').write(photo_data)
    msg = "The File"+fn+" uploaded successfully"
else:
    msg = "No file was uploaded"

location = form.getvalue('Location')

print("""<html>
<head>
<title>Feedback</title>
</head>
<body>
""")

print("<p>Name: %s</p>" % name)
print("<p>Email: %s</p>" % mail)
print("<p>Password: %s</p>" % password)
print("<p> Emotions are:</p><ul>")
for i in emotions:
    print("<li>%s</li>" % i)
print("</ul><p>Level of Satisfaction: %s</p>" % satisfaction)
print("<p>Comments: %s</p>" % comments)
print("<p>{} Bio-Photo:</p>".format(name))
print('<img src="files/{}" alt="{}" width="200" height="200">'.format(fn,fn))
print("<p>Location: %s</p>" % location)
print('''</body>
</html>''')




