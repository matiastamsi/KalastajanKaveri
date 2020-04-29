from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.search.forms import SearchForm
from application.catches.models import Catch
from application.auth.models import User
from application.fish.models import Fish

from sqlalchemy.sql import text
from sqlalchemy import desc

import datetime

@app.route("/search", methods=["GET"])
@login_required(role="USER")
def search_form():
    return render_template("search/search.html",
                           form = SearchForm(),
                           fishes = Fish.query.all(), 
                           catches = Catch.query.all(),
                           year = datetime.date.today().year)

@app.route("/search/", methods=["POST"])
@login_required(role="USER")
def search_show():
    form = SearchForm(request.form)
    catches = []

    if form.species.data == 'All' and form.spot.data == 'All':

        if form.orderBySize.data:
            catches = Catch.query.filter().order_by(desc(Catch.weight), desc(Catch.length))
        else:
            catches = Catch.query.filter().order_by(desc(Catch.date_created))

    elif form.species.data != 'All' and form.spot.data == 'All':

        fishId = Fish.query.filter(Fish.name==form.species.data).first().id

        if form.orderBySize.data:
            catches = Catch.query.filter(Catch.species_id==fishId).order_by(desc(Catch.weight), desc(Catch.length))
        else:
            catches = Catch.query.filter(Catch.species_id==fishId)

    elif form.spot.data != 'All' and form.species.data == 'All':

        if form.orderBySize.data:
            catches = Catch.query.filter(Catch.spot==form.spot.data).order_by(desc(Catch.weight), desc(Catch.length))
        else:
            catches = Catch.query.filter(Catch.spot==form.spot.data)

    elif form.spot.data != 'All' and form.species.data != 'All':

        fishId = Fish.query.filter(Fish.name==form.species.data).first().id

        if form.orderBySize.data:
            catches = Catch.query.filter(Catch.species_id==fishId, Catch.spot==form.spot.data).order_by(desc(Catch.weight), desc(Catch.length))
        else:
            catches = Catch.query.filter(Catch.species_id==fishId, Catch.spot==form.spot.data)

    return render_template("search/show.html", catches = catches)

