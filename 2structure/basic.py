from flask import *

app = Flask(__name__)

@app.route("/")

def hi():
    return "Hi"








if __name__ == '__main__':
    app.run()
