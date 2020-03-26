from application import db
from application.auth.models import User

class Catch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    species = db.Column(db.String(144), nullable=False)
    lure_or_fly = db.Column(db.String(144), nullable=False)
    length = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    spot = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)
    private_or_public = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    fisher = db.Column(db.String(144), nullable=False)

    def __init__(self, species, lure_or_fly, length, weight, spot, description, private_or_public):
        self.species = species
        self.lure_or_fly = lure_or_fly
        self.length = length
        self.weight = weight
        self.spot = spot
        self.description = description
        self.private_or_public = private_or_public
