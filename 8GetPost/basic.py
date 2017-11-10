from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])



def basic():
    #request.method and request.form
    if request.method == 'POST':
        if request.form['name'] and request.form['pass']:
            return 'Validation successful'
        else:
            return 'Validation unsuccessful'
        return 'Hi'
    
    
         
    return render_template('def.html')
        

if __name__ == '__main__':
    app.run()

