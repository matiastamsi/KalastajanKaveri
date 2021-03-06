from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, bcrypt, login_required
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.newforms import SignUpForm
from application.catches.models import Catch

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())
    #"POST":
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

@app.route("/auth/create", methods=["POST"])
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
    #Create a new user.
    u = User(form.name.data, form.username.data, form.password.data)
    db.session().add(u)
    db.session().commit()

    login_user(u)

    return redirect(url_for("index"))

@app.route("/auth/change_or_delete/")
@login_required
def auth_change_or_delete():
    return render_template("auth/change_or_delete.html",
                           form = SignUpForm(),
                           u = current_user)

@app.route("/auth/save/<user_id>", methods=["POST"])
@login_required
def auth_save(user_id):

    form = SignUpForm(request.form)

    if form.delete.data:
        u = User.query.get(user_id)
        catches = Catch.query.filter(Catch.account_id==u.id)

        for catch in catches:
            db.session.delete(catch) #Delete all user's catches.

        db.session().delete(u)
        db.session().commit()

        return redirect(url_for("index"))

    #When saving changes, in database is still the old version
    #so let's check that there is no more than one match.
    if User.query.filter(User.name == form.name.data,
                         User.username == form.username.data).count() > 1:
        return render_template("auth/change_or_delete.html", form=form, u = current_user,
                               errorName = "Name is already taken!",
                               errorUsername = "Username is already taken!")
    elif User.query.filter(User.name == form.name.data).count() > 1:
        return render_template("auth/change_or_delete.html", form=form, u = current_user,
                               errorName = "Name is already taken!")
    elif User.query.filter(User.username == form.username.data).count() > 1:
        return render_template("auth/change_or_delete.html", form=form, u = current_user,
                               errorUsername = "Username is already taken!")

    if not form.validate():
        return render_template("auth/change_or_delete.html",
                               form=form,
                               u = current_user)
    #Change user information.
    u = User.query.get(user_id)
    u.name = form.name.data
    u.username = form.username.data
    u.password = form.password.data
    db.session().commit()

    return redirect(url_for("index"))

