from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.fish.models import Fish
from application.fish.forms import FishForm
from application.auth.models import User

@app.route("/fish", methods=["GET"])
def fish_index():
    return render_template("fish/list.html", fishes = Fish.query.all(), authenticated = current_user.is_authenticated)

@app.route("/fish/new/")
@login_required(role="USER")
def fish_form():
    return render_template("fish/new.html", form = FishForm())

@app.route("/fish/", methods=["POST"])
@login_required(role="USER")
def fish_create():
    form = FishForm(request.form)

    if not form.validate():
        return render_template("fish/new.html", form = form)

    f = Fish(
        form.name.data.lower().strip(),
        form.minimum_catch_size.data,
        str(form.closed_season_starts_day.data) + '.' + str(form.closed_season_starts_month.data),
        str(form.closed_season_ends_day.data) + '.' + str(form.closed_season_ends_month.data))

    db.session().add(f)
    db.session().commit()

    return redirect(url_for("fish_index"))

fishId = 0

@app.route("/fish/<fish_id>/", methods=["POST"])
@login_required(role="USER")
def fish_change_or_delete(fish_id):

    global fishId
    fishId = fish_id
    fish = Fish.query.get(fish_id)
    return render_template("fish/change_or_delete.html", form = FishForm(), fish = fish)

@app.route("/fish/fishId", methods=["POST"])
@login_required(role="USER")
def fish_save():

    form = FishForm(request.form)

    if form.delete.data:
        f = Fish.query.get(fishId)
        db.session().delete(f)
        db.session().commit()

        return redirect(url_for("fish_index"))

    if not form.validate():
        fish = Fish.query.get(fishId)
        return render_template("fish/change_or_delete.html", form = form, fish = fish)


    f = Fish.query.get(fishId)
    f.name = form.name.data
    f.minimum_catch_size = form.minimum_catch_size.data
    f.closed_season_starts = str(form.closed_season_starts_day.data) + '.' + str(form.closed_season_starts_month.data)
    f.closed_season_ends = str(form.closed_season_ends_day.data) + '.' + str(form.closed_season_ends_month.data)
    db.session().commit()

    return redirect(url_for("fish_index"))
