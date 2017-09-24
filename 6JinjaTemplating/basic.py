from flask import *

app = Flask(__name__)


@app.route('/lang/<mylang>')

def basic(mylang):
    name = "Raunak"
    id = 50000
    return render_template('abc.html', n=name, i=id, l=mylang)


if __name__ == "__main__":
    app.run()
