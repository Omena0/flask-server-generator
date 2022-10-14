### Flask server generator by Omena0
### https://github.com/Omena0/flask-server-generator
### Usage permitted with apropriate credit (dont remove theese comments)


print('Initializing... [OS, Lib]')
import os
import lib

####### CONFIG #######

# Root site function name in app.py
__root__ = '__home__'

# Name of html file set as root, recommended to set as '' or '__home__' 
rootname = ''#.html

# Where to go after login
logonredirect = __root__

# Enable auth with %auth=True%
auth_enabled = True

# Force auth on every page and redirect to login page
force_auth = True



#### END CONFIG ####

lib.log('*','Initialized!')

app = open('app.py','wb')

lib.log('*','Initializing app...')

header = '''
### This file was generated with the Flask-Server-Generator!
### https://github.com/Omena0/flask-server-generator
### Usage permitted with apropriate credit (dont remove theese comments)
'''
code = '''
from flask import *
import lib
app = Flask(__name__)
app.secret_key=b"ce8a093b2b15e8de1c2620aaebfe24f4a7c12437222ccc93646e5b0cd88e9921"
'''

app.write(header.encode())
app.write(code.encode())
app.close()

lib.log('!','Done!')

names = []
page_contents = []

def hang():
    lib.log('*','Program is hanging, check program output above to see what might have went wrong!')
    while True: pass

index = 0
lib.log('*','Indexing HTML Files...')
for i in os.listdir():
    lib.log('*',f'{i}...')
    if not i.endswith('.html'):
        lib.log('!','Not an HTML File! Continuing search...')
        continue
    lib.log('!','HTML File found! Indexing..')
    names.append(i.replace('.html',''))
    lib.log('!','File Contents and name indexed!')
if names == []:
    lib.log('*','No HTML Files In folder! Aborting...')
    hang()
    
lib.log('!','Indexing complete!')

lib.log('*','Generating functions...')
app = open('app.py','ab')

index = 0
lib.log('*','App file openned!\n')
for i in names:
    if i == rootname:
        a = f'''
@app.route("/{i}")
def __home__():
    if {force_auth} and "username" not in session: return redirect(url_for("login"))
    file = open("{i}.html")
    content = file.read()
    file.close()
    return content
    '''
            
    elif i == '404': a = f'''
@app.errorhandler(404)
def __404__(a):
    try: lib.log('!',session["username"]+' Recieved 404 page!')
    except: lib.log('!','UNKNOWN USER Recieved 404 page!')
    file = open("{i}.html")
    content = file.read()
    file.close()
    return content
    '''
    elif i == '__login__':
        a = f'''
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        lib.log('LOGIN',session["username"]+' Logged in.')
        return redirect(url_for("{logonredirect}"))
    file = open("__login__.html")
    content = file.read()
    file.close()
    return content
    '''
    elif '%auth=True%' in i:
        if not auth_enabled: continue
        i = i.replace('%auth=True%','')
        a = f'''
@app.route("/{i}")
def {i}():
    if {force_auth} and "username" not in session: return redirect(url_for("login"))
    if 'username' in session:
        file = open("{i}.html")
        content = file.read()
        file.close()
        return content
    return "You are not logged in!"
'''
    else: a = f'''
@app.route("/{i}")
def {i}():
    if {force_auth} and "username" not in session: return redirect(url_for("login"))
    file = open("{i}.html")
    content = file.read()
    file.close()
    return content
'''
    lib.log(i,f'Writing function: {a}')
    lib.log('*',f'Return from file.write():  {app.write(a.encode())}')
    index = index + 1
lib.log('!','Complete! Closing file...')
app.close()
lib.log('!','All done!!! You can close this window!')
hang()
