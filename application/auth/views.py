from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.newforms import SignUpForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    
    found_user = User.query.filter_by(username = form.data['username']).first()

    if not found_user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")
    #Use bcrypt's method "check_password_hash" to check if password is correct.
    authenticated_user = bcrypt.check_password_hash(found_user.password,
                                                    form.data['password'])

    if authenticated_user:
        user = User.query.filter(User.username == form.username.data).first()
        login_user(user)
        return redirect(url_for("index"))
    else:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new/")
def auth_form():
    return render_template("auth/new.html", form = SignUpForm())

@app.route("/auth/", methods=["POST"])
def auth_create():
    form = SignUpForm(request.form)

    if User.query.filter(User.name == form.name.data,
                         User.username == form.username.data).first():
        return render_template("auth/new.html", form=form,
                               errorName = "Name is already taken!",
                               errorUsername = "Username is already taken!")
    elif User.query.filter(User.name == form.name.data).first():
        return render_template("auth/new.html", form=form,
                               errorName = "Name is already taken!")
    elif User.query.filter(User.username == form.username.data).first():
        return render_template("auth/new.html", form=form,
                               errorUsername = "Username is already taken!")

    if not form.validate():
        return render_template("auth/new.html", form=form)

    u = User(form.name.data, form.username.data, form.password.data)
    db.session().add(u)
    db.session().commit()

    login_user(u)
    return redirect(url_for("index"))

