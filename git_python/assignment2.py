import requests
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def movieapp():
    return "Welcome to Flask" 
if __name__ == '__main__':
    a= movieapp
    print(a)
