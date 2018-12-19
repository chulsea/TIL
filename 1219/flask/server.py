from flask import Flask

app = Flask("firstapp")

@app.route("/")
def home():
    return "hello world!"

@app.route("/user")
def login():
    return "my name is pkch"