#Generated with flask-server-generator!
#View it on github: https://github.com/Omena0/flask-server-generator
from flask import Flask
app = Flask(__name__)
@app.route("/")
def __home__():
    file = open(".html")
    content = file.read()
    file.close()
    return content
@app.route("/example")
def example():
    file = open("example.html")
    content = file.read()
    file.close()
    return content
@app.route("/home")
def home():
    file = open("home.html")
    content = file.read()
    file.close()
    return content
