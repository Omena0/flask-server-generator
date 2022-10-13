print('Initializing... [OS, Lib]')
import os
import lib

lib.log('*','Initialized!')

app = open('app.py','wb')

lib.log('*','Initializing app...')

header = '#Generated with flask-server-generator!\n#View it on github: https://github.com/Omena0/flask-server-generator\n'
code = 'from flask import Flask\napp = Flask(__name__)\n'
app.write(header.encode())
app.write(code.encode())
app.close()

lib.log('!','Done!')

names = []
page_contents = []

index = 0
lib.log('*','Indexing HTML Files...')
for i in os.listdir():
    lib.log('*',f'{i}...')
    if not i.endswith('.html'):
        lib.log('!','Not an HTML File! Continuing search...')
        continue
    lib.log('!','HTML File found! Indexing..')
    names.append(i.replace('.html',''))
##    file = open(i)
##    page_contents.append(file.read())
##    file.close()
    lib.log('!','File Contents and name indexed!')

lib.log('!','Indexing complete!')

lib.log('*','Generating functions...')
app = open('app.py','ab')

index = 0
lib.log('*','App file openned!\n')
for i in names:
    if i == '': name = '__home__'
    else: name = i 
    a = f'@app.route("/{i}")\ndef {name}():\n    file = open("{i}.html")\n    content = file.read()\n    file.close()\n    return content\n'
    lib.log(i,f'Writing function: {a}')
    lib.log('*',f'Return from file.write():  {app.write(a.encode())}')
    index = index + 1
lib.log('!','Complete! Closing file...')
app.close()
lib.log('!','All done!!!')
