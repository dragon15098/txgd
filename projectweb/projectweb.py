from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('homepage'))

@app.route('/homepage')
def homepage():
    return render_template("homepage.html")


if __name__ == '__main__':
    app.run()
