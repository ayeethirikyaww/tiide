from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/ayee")
def ayee():
    return "Hello Aye Thiri Kyaw"
