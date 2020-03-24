from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.catches.models import Catch

#Variable to store which catch is going to be updated.
catchId = 0

@app.route("/catches", methods=["GET"])
def catches_index():
    return render_template("catches/list.html", catches = Catch.query.all())

@app.route("/catches/new/")
@login_required
def catches_form():
    return render_template("catches/new.html")

@app.route("/catches/", methods=["POST"])
@login_required
def catches_create():
    c = Catch(request.form.get("specie"), request.form.get("lure_or_fly"), request.form.get("length"), request.form.get("weight"), request.form.get("spot_id"), request.form.get("user_id"), request.form.get("description"), request.form.get("private_or_public"))
    db.session().add(c)
    db.session().commit()

    return redirect(url_for("catches_index"))

@app.route("/catches/<catch_id>/", methods=["POST"])
@login_required
def catches_change(catch_id):
    global catchId
    catchId = catch_id
    return render_template("catches/change.html")

@app.route("/catches/catchId", methods=["POST"])
@login_required
def catches_save():
    c = Catch.query.get(catchId)
    c.specie = request.form.get("specie")
    db.session().commit()

    return redirect(url_for("catches_index"))
