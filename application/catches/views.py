from application import app, db
from flask import redirect, render_template, request, url_for
from application.catches.models import Catch

@app.route("/catches", methods=["GET"])
def catches_index():
    return render_template("catches/list.html", catches = Catch.query.all())

@app.route("/catches/new/")
def catches_form():
    return render_template("catches/new.html")

@app.route("/catches/", methods=["POST"])
def catches_create():
    c = Catch(request.form.get("specie"), request.form.get("lure_or_fly"), request.form.get("length"), request.form.get("weight"), request.form.get("spot_id"), request.form.get("user_id"), request.form.get("description"), request.form.get("private_or_public"))
    db.session().add(c)
    db.session().commit()

    return redirect(url_for("catches_index"))
