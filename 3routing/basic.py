from flask import *

app = Flask(__name__)
'''\
@app.route('/hey')

def abc():
    return "hi"
'''
@app.route('/')

def hi():
    return "my name is raunak  "


@app.route('/mysite/<name>')

def name(name):
    return "Hi "+ name





if __name__ == '__main__':
    app.run()
    
