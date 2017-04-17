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

app.config["UPLOAD_PATH"] = os.path.join(app.root_path, "uploads")
if not os.path.exists(app.config["UPLOAD_PATH"]):
    os.makedirs(app.config["UPLOAD_PATH"])

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def hello_world():
    return redirect(url_for('homepage'))


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@login_manager.user_loader
def user_loader(user_token):
    found_user = User.objects(token=user_token).first()
    if found_user:
        session_user = SessionUser(found_user.token)
        return session_user

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
        if not user and request.form["password"] == request.form["password-repeat"]:
            new_user = User()
            new_user.username = request.form["username"]
            new_user.password = request.form["password"]
            new_user.description = request.form["description"]

            # image
            file = request.files["source"]
            if file:
                filename = secure_filename(file.filename)
                if os.path.exists(os.path.join(os.path.join(app.config["UPLOAD_PATH"], filename))):
                    name_index = 0
                    # filename =home.png
                    original_name = filename.rsplit('.', 1)[0]
                    original_extension = filename.rsplit('.', 1)[1]
                    while os.path.join(app.config["UPLOAD_PATH"], filename):
                        name_index += 1
                        # new filename = home (1).png
                        filename = "{0} ({1}).{2}".format(original_name, name_index, original_extension)
                        # change filename add(name_index)
                file.save(os.path.join(app.config["UPLOAD_PATH"], filename))
                new_user.image = url_for('uploaded_file', filename=filename)

            if request.form["gender"] == "male":
                new_user.gender = "male"
                new_user.number = num.numberboy + 1
                num.numberboy +=1
            else:
                new_user.gender = "female"
                new_user.number = num.numbergirl +1
                num.numbergirl +=1

            num.save()
            new_user.save()
            return render_template("homepage.html")
        else:
            return render_template("sign_up.html")


@app.route('/boy_page')
def boy_page():
    num = Number.objects(name="abc").first()
    temp = random.randint(0, num.numberboy)
    boy = User.objects(number=temp, gender="male").first()
    return render_template('boy_page.html', description=boy.description, user=boy.image)


@app.route('/girl_page')
def girl_page():
    num = Number.objects(name="abc").first()
    temp = random.randint(0, num.numbergirl)
    girl = User.objects(number=temp, gender="male").first()
    return render_template('girl_page.html', description=girl.description)


@app.route('/update', methods=["GET", "POST"])
@login_required
def update():
    user = User.objects(token=current_user.id).first()
    if (request.method == "GET"):
        return render_template("update_info.html", image=user.image, description=user.description)
    if (request.method == "POST"):
        #image
        file = request.files["source"]
        if file:
            filename = secure_filename(file.filename)
            if os.path.exists(os.path.join(os.path.join(app.config["UPLOAD_PATH"], filename))):
                name_index = 0
                # filename =home.png
                original_name = filename.rsplit('.', 1)[0]
                original_extension = filename.rsplit('.', 1)[1]
                while os.path.join(app.config["UPLOAD_PATH"], filename):
                    name_index += 1
                    # new filename = home (1).png
                    filename = "{0} ({1}).{2}".format(original_name, name_index, original_extension)
                    # change filename add(name_index)
            file.save(os.path.join(app.config["UPLOAD_PATH"], filename))
            user.image = url_for('uploaded_file', filename=filename)

        return render_template("update_info.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_PATH"], filename)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run()
