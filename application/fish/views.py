from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.fish.models import Fish
from application.fish.forms import FishForm
from application.auth.models import User

@app.route("/fish", methods=["GET"])
def fish_index():
    #If current user is authenticated
    #there will be "Change or delete" -button
    #next to the species.
    return render_template("fish/list.html",
                           fishes = Fish.query.all(),
                           authenticated = current_user.is_authenticated)

@app.route("/fish/new/")
@login_required(role="USER")
def fish_form():

    return render_template("fish/new.html", form = FishForm())

@app.route("/fish/", methods=["POST"])
@login_required(role="USER")
def fish_create():

    form = FishForm(request.form)

    if Fish.query.filter(Fish.name == form.name.data.lower().strip()).first():
        return render_template("fish/new.html", form=form,
                               error = "The species already exists!")

    minimumCatchSize = form.minimum_catch_size.data
    closedSeasonStarts = (str(form.closed_season_starts_day.data) + '.'
                          + str(form.closed_season_starts_month.data) + '.')
    closedSeasonEnds = (str(form.closed_season_ends_day.data) + '.'
                        + str(form.closed_season_ends_month.data) + '.')
    #Only some of the fishes have minimum catch size or
    #closed season. For those who do not have, lets set it to 'None'.
    if form.noMinimumCatchSize.data:
        minimumCatchSize = None
    if form.noClosedSeason.data:
        closedSeasonStarts = None
        closedSeasonEnds = None

    f = Fish(form.name.data.lower().strip(),
             minimumCatchSize,
             closedSeasonStarts,
             closedSeasonEnds)
    db.session().add(f)
    db.session().commit()

    return redirect(url_for("fish_index"))

@app.route("/fish/<fish_id>", methods=["POST"])
@login_required(role="USER")
def fish_change_or_delete(fish_id):

    fish = Fish.query.get(fish_id)
    return render_template("fish/change_or_delete.html",
                           form = FishForm(),
                           fish = fish)

@app.route("/fish/<fish_id>/", methods=["POST"])
@login_required(role="USER")
def fish_save(fish_id):

    form = FishForm(request.form)

    if form.delete.data:
        f = Fish.query.get(fish_id)
        db.session().delete(f)
        db.session().commit()

        return redirect(url_for("fish_index"))
    #Current fish already exists so check if count is more than one.
    if Fish.query.filter(Fish.name == form.name.data.lower().strip()).count() > 1:
        fish = Fish.query.get(fish_id)
        return render_template("fish/change_or_delete.html",
                               form=form,
                               fish=fish,
                               error = "The species already exists!")

    minimumCatchSize = form.minimum_catch_size.data
    closedSeasonStarts = (str(form.closed_season_starts_day.data) + '.'
                          + str(form.closed_season_starts_month.data) + '.')
    closedSeasonEnds = (str(form.closed_season_ends_day.data) + '.'
                        + str(form.closed_season_ends_month.data) + '.')

    #Only some of the fishes have minimum catch size or
    #closed season. For those who do not have, lets set it to 'None'
    if form.noMinimumCatchSize.data:
        minimumCatchSize = None
    if form.noClosedSeason.data:
        closedSeasonStarts = None
        closedSeasonEnds = None

    f = Fish.query.get(fish_id)
    f.name = form.name.data.lower().strip()
    f.minimum_catch_size = minimumCatchSize
    f.closed_season_starts = closedSeasonStarts
    f.closed_season_ends = closedSeasonEnds
    db.session().commit()

    return redirect(url_for("fish_index"))
