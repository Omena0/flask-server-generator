
#Generated with flask-server-generator!
#View it on github: https://github.com/Omena0/flask-server-generator

from flask import *
import lib
app = Flask(__name__)
app.secret_key=b"ce8a093b2b15e8de1c2620aaebfe24f4a7c12437222ccc93646e5b0cd88e9921"

@app.route("/")
def __home__():
    if True and "username" not in session: return redirect(url_for("login"))
    file = open(".html")
    content = file.read()
    file.close()
    return content
    
@app.errorhandler(404)
def __404__(a):
    try: lib.log('!',session["username"]+' Recieved 404 page!')
    except: lib.log('!','UNKNOWN USER Recieved 404 page!')
    file = open("404.html")
    content = file.read()
    file.close()
    return content
    
@app.route("/main")
def main():
    if True and "username" not in session: return redirect(url_for("login"))
    file = open("main.html")
    content = file.read()
    file.close()
    return content

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        lib.log('LOGIN',session["username"]+' Logged in.')
        return redirect(url_for("__home__"))
    file = open("__login__.html")
    content = file.read()
    file.close()
    return content
    