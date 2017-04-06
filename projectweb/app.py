from flask import *
from flask_login import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('homepage'))

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign_up')
def sign_up():
    return  render_template('sign_up.html')

@app.route('/boy_page')
def boy_page():
    return render_template('boy_page.html')
@app.route('/update', methods=["GET", "POST"])
def update():
    if (request.method == "GET"):
        return render_template("update_info.html")
    if (request.method == "POST"):
        pass
        return render_template("update_info.html")






if __name__ == '__main__':
    app.run()



