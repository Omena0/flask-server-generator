# Python Flask Server Generator
### Generate server code and automatically define page functions and route in flask!

## How to set up and use:
1. Download the repo and run build.cmd
2. Create the HTML files that you want to be on the website (into code)
### 3. Download and install python, and flask:
#### Install python
  - Go to the python website and download python 3.X (newest possible)
  - Run the installer file
  - Make sure to install pip in the installer options
#### Intsall flask
  - Open run prompt by pressing WIN + R
  - Type cmd and hit enter
  - In cmd type:
```
pip install flask
``` 
4. Run generator.exe (or py if you want)
5. Run code/START SERVER or open terminal (cmd or powershell) in code/ and type:
```
flask run
```
### 6. Connect to the website by:
7. Opening your internet browser
8. Going to your own website at:
```
http://127.0.0.1:5000/
```
8. You are done!
(Noone else can go there right now, look up some tutorial or something ill update this readme when i figure how to do things with flask)

## Features:
- [X] Only need to code html
- [X] Automatically generate python-flask server
- [X] Automatically route all html files based on their name
- [X] Automatically return html code from their corresponding files
- [X] Automatically send html page to client web-browsers
- [X] Is cool
- [X] ALOT of logging in generator
- [X] Username auth support (no psw yet)
- [X] Some cofiguratio options i generator
- [X] NEVER have to open app.py!!!
- [ ] Automatically port forward / host on public address (thats ur problem)


## How tf does it work?
It just appends code to app.py and then it all works! Ur welcome!!!

## Notes:
### HTML File structure:
- The script gets all files ending with .html, so only put files that it can read, and understand as .html
- The root page filename is empty by default
- To require login add %auth=True% somewehere in the filename (eg. home%auth=True%.html)
- 404 page and login page cannot require auth (for obvious reasons)
- The login page must be called __login__.html, to make sure it works copy the one already in he repo and edit that (dont edit the form that might break it)
- The 404 page must be called 404.html
- The server logs all logins and 404 pages (if the user isint logged in it will display as UNKNOWN)
- Make sure to change the app.secret_key if ur actually using this

### CSS:
- Reading css FILES isint supported (i guess) sice idk how flask works with css
- U can still include css in ur html code!
### La Script:
- it may not be 100% reliable...
- Havent done big testing on it, thats why its on github
### Example site:
- You can use this to learn how this works!
- I cant code html so someone else can make a better one
### Usage:
- Overall, Dont use it! Its terrible right now!
- If you use it without credit i will come to ur house  (dont remove the comments)
- I know where you live

#### This is really simple... Learn to code if u actually need this, its made for sites with over 40 pages.