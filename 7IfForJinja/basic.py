from flask import *

app = Flask(__name__)

@app.route('/names')

def basic():


    a = ['python', 'java', 'javascript', 'c++', 'c', 'php']
    return render_template('abc.html', q=a)

if __name__ == '__main__':
    app.run()
