from flask import *


app = Flask(__name__)




@app.route('/')

def basic():
   
    return render_template('myfile.html')


if __name__ == '__main__':
    app.run()
