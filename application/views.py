from flask import render_template
from application import app
from application.catches.models import Catch

@app.route('/')
def index():
    return render_template("index.html", species_catched=Catch.find_species_catched(), biggest_catch=Catch.find_biggest_catch())
