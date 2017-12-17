from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])

def basic():
    if request.method == 'POST':
        if request.form['name'] and request.form['pass']:
        
            #variables to hold the requested form elements 
            names = request.form['name']
            passwords = request.form['pass']

            # Cursor for execution of SQL statements in Flask
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO register(name, password) VALUES(%s, %s)", (names, passwords))
            # Cursor needs to be committed for execution of the SQL commands
            cursor.connection.commit()
            # Always close the cursor
            cursor.close()
            
        
     
    return render_template('registration.html')


if __name__ == '__main__':
    app.run()
