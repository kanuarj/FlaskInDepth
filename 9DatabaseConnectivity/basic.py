from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)

#Configuration Elements
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'flask'


#Connection Element
mysql = MySQL(app)


@app.route('/')

def basic():

    return 'okay'



if __name__ == '__main__':
    app.run()
