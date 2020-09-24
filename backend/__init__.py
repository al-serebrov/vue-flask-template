from flask import Flask

app = Flask(__name__)


# a simple page that says hello
@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

