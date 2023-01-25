from flask import Flask, render_template, request, make_response, session, redirect, url_for
from flask_session import Session
from controller import Controller
from contacts import Contacts
from user import User

app = Flask(__name__)
app.secret_key = "123saif"

@app.route('/')
def hello():
    return "hello world"


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/log_out', methods=["POST"])
def logout():
    session.clear()
    msg="Logout successfull\nlogin again to access contact book"
    return render_template("login.html", msg=msg)


@app.route('/login_user', methods=["POST"])
def loginuser():
    email = request.form["email"]
    controllerobj = Controller()
    #validate email
    status = controllerobj.validate_email(email)
    if status == True:
        password = request.form["password"]
        statuspassword = controllerobj.matchpassword(email, password)
        if statuspassword == True:
            session["userid"] = controllerobj.get_user_id(email)
            print("Session is: ", session["userid"])
            return render_template("create_contcat.html")
        else:
            msg="Password incorrect"
            return render_template("login.html", msg=msg)
    else:
        msg = "Account does not exist!! try another email or sign up"
        return render_template("login.html", msg=msg)

    # print(Session["email"])


@app.route('/signup', methods=["POST"])
def signup():
    return render_template("signup.html")


@app.route('/signup_user', methods=["POST"])
def signupuser():
    email = request.form["email"]
    controllerobj = Controller()
    status = controllerobj.validate_email(email)
    if status == False:
        password = request.form["password"]
        passwordstatus = controllerobj.validate_password(password)
        if passwordstatus == False:
            msg = "Password must be 8 characters long"
            return render_template("signup.html", msg=msg)
        else:
            userobj = User(email, password)
            controllerobj.registeruser(userobj)
            return render_template("login.html")
    else:
        msg = "Email already exist"
        return render_template("signup.html", msg=msg)



@app.route('/create_contact', methods=["POST"])
def create_contact():  # put application's code here
    return render_template("create_contcat.html")


@app.route('/show_contact', methods=["POST"])
def show_contact():
    controllerobject=Controller()
    records = controllerobject.get_contacts(session["userid"])
    if len(records) == 0:
        msg = "No data fround"
        return render_template("create_contcat.html", msg=msg)
    return render_template("show_contacts.html", msg=records)


@app.route('/delete_contact', methods=["POST"])
def delete_contact():
    index = request.form["index"]
    controllerobj = Controller()
    controllerobj.delete_contact(index)
    records = controllerobj.get_contacts(session["userid"])
    if len(records) == 0:
        msg="No data fround"
        return render_template("create_contcat.html", msg=msg)
    return render_template("show_contacts.html", msg=records)


@app.route('/get_contacts', methods=["POST"])
def get_conatacts():
    name = request.form["name"]
    mobileno = request.form["mobileno"]
    city = request.form["city"]
    profession = request.form["profession"]
    userid = session["userid"]
    print("User id is:", userid)
    #validate name
    controllerobject = Controller()
    status = controllerobject.validate_name(name)
    if status == False:
        msg = "user already exist! try a different name"
        return render_template("create_contcat.html", msg=msg)
    #validate mobile number
    status = controllerobject.validate_mobileno(mobileno)
    if status == False:
        msg = "mobile number not correct\nkindly follow the pattern +923111234567890"
        return render_template("create_contcat.html", msg=msg)
    contact = Contacts(name, mobileno, city, profession, userid)
    controllerobject.dbobject.insert_contact(contact)
    return render_template("create_contcat.html")


@app.route('/find_contact', methods = ["POST"])
def find_contact():
    name = request.form["name"]
    controllerobject = Controller()
    result = controllerobject.search_contact(name)
    return render_template("searched_contact.html", msg=result)


@app.route('/search_contact', methods=["POST"])
def search_contact():
    return render_template("search_contact.html")


if __name__ == '__main__':
    app.run()
