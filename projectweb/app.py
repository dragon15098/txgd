from flask import *
import mlab
from flask_login import *
from sessionuser import SessionUser
from werkzeug.utils import *
from models.user import User
from models.number import Number
import random
import os

app = Flask(__name__)
mlab.connect()
app.secret_key = "abc"
# num = Number()
# num.name = "abc"
# num.number = 0
# num. save()
# user = User()
# user.username = "ha"
# user.password = "ha"
# user.gender = "male"
# user.number = 10
# user.description = "ha"
# user.save()

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def hello_world():
    return redirect(url_for('homepage'))

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/login', methods=["GET", "POST"])
def login_web():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        user = User.objects(username=request.form["username"]).first()
        if user and user.password == request.form["password"]:
            session_user = SessionUser(user.id)
            user.update(set__token=str(user.id))
            login_user(session_user)
            return render_template("homepage.html")
        else:
            pass
            return redirect(url_for("login_web"))


@app.route('/sign_up', methods=["GET", "POST"])
def sign_up_web():
    if request.method == "GET":
        return render_template("sign_up.html")
    elif request.method == "POST":
        user = User.objects(username=request.form["username"]).first()
        num = Number.objects(name="abc").first()
        if not user and request.form["password"] == request.form["psw-repeat"]:
            new_user = User()
            new_user.username = request.form["username"]
            new_user.password = request.form["password"]
            new_user.description = "None"
            if request.form["gender"] == "male":
                new_user.gender = "male"
            else:
                new_user.gender = "female"
            new_user.number = num.number + 1
            num.name = "abc"
            num.number += 1
            num.save()
            new_user.save()
            return render_template("homepage.html")
        else:
            return render_template("sign_up.html")

@app.route('/boy_page')
def boy_page():
    num = Number.objects(name="abc").first()
    temp = random.randint(0, num.number)
    boy = User.objects(number=temp, gender="male").first()
    return render_template('boy_page.html', description=boy.description, user=users)


@app.route('/girl_page')
def girl_page():
    num = Number.objects(name="abc").first()
    temp = random.randint(0, num.number)
    girl = User.objects(number=temp, gender="male").first()
    return render_template('girl_page.html', description=girl.description)


@app.route('/update', methods=["GET", "POST"])
def update():
    if (request.method == "GET"):
        return render_template("update_info.html")
    if (request.method == "POST"):
        pass
        return render_template("update_info.html")



if __name__ == '__main__':
    app.run()