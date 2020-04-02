from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.catches.models import Catch
from application.catches.forms import CatchForm
from application.auth.models import User
from application.fish.models import Fish

@app.route("/catches", methods=["GET"])
def catches_index():
    
    return render_template("catches/list.html", catches = Catch.query.all())

@app.route("/catches/new/")
@login_required
def catches_form():
    return render_template("catches/new.html", form = CatchForm())

@app.route("/catches/", methods=["POST"])
@login_required
def catches_create():
    form = CatchForm(request.form)

    if not form.validate():
        return render_template("catches/new.html", form = form)

    #Find the species from fish table.
    s_id = Fish.find_id_based_on_name(name= form.species.data.lower().strip())
    if s_id == None:
        return render_template("catches/new.html", form = form,
                               error = "No such species")
    c = Catch(
        form.lure_or_fly.data,
        form.length.data,
        form.weight.data,
        form.spot.data.capitalize(),
        form.description.data,
        form.private_or_public.data)
    c.species_id = s_id
    c.account_id = current_user.id
    c.fisher = current_user.name
    db.session().add(c)
    db.session().commit()

    return redirect(url_for("catches_index"))

catchId = 0

@app.route("/catches/<catch_id>/", methods=["POST"])
@login_required
def catches_change_or_delete(catch_id):

    global catchId
    catchId = catch_id
    return render_template("catches/change_or_delete.html", form = CatchForm())

@app.route("/catches/catchId", methods=["POST"])
@login_required
def catches_save():

    form = CatchForm(request.form)

    if form.delete.data:
        c = Catch.query.get(catchId)
        db.session().delete(c)
        db.session().commit()

        return redirect(url_for("catches_index"))

    if not form.validate():
        return render_template("catches/change.html", form = form)


    c = Catch.query.get(catchId)
    c.species = form.species.data.lower().strip()
    c.lure_or_fly = form.lure_or_fly.data
    c.length = form.length.data
    c.weight = form.weight.data
    c.spot = form.spot.data.capitalize()
    c.description = form.description.data
    c.private_or_public = form.private_or_public.data
    c.account_id = current_user.id
    c.fisher = current_user.name
    db.session().commit()

    return redirect(url_for("catches_index"))


