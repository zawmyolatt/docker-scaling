import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello! My container name is :" + socket.gethostname()