from flask import Flask, request
app = Flask (__name__)

@app.route ("/welcome")
def say_welcome():
    return "welcome"

@app.route ("/welcome/home")
def welcome_home():
    return "Welcome Home"

@app.route ("/welcome/back")
def welcome_back():
    return "Welcome Back!"