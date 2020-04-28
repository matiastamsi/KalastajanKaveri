from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.search.forms import SearchForm
from application.catches.models import Catch
from application.auth.models import User
from application.fish.models import Fish

@app.route("/search")
@login_required(role="USER")
def search_form():
    return render_template("search/search.html",
                           form = SearchForm(),
                           fishes = Fish.query.all(), 
                           catches = Catch.query.all())

@app.route("/search/show", methods=["POST"])
@login_required(role="USER")
def search_show():
    form = SearchForm(request.form)

