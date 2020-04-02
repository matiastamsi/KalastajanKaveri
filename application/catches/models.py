from application import db
from application.auth.models import User
from application.models import Base

from sqlalchemy.sql import text

import datetime

class Catch(Base):

    lure_or_fly = db.Column(db.String(144), nullable=False)
    length = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    spot = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)
    private_or_public = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    species_id = db.Column(db.Integer, db.ForeignKey('fish.id'))

    fisher = db.Column(db.String(144), nullable=False)

    def __init__(self, lure_or_fly, length, weight, spot, description, private_or_public):
        self.lure_or_fly = lure_or_fly
        self.length = length
        self.weight = weight
        self.spot = spot
        self.description = description
        self.private_or_public = private_or_public

    @staticmethod
    def find_name_based_on_id(id=0):
        stmt = text("SELECT Fish.name FROM Fish WHERE Fish.id = :id").params(id=id)
        res = db.engine.execute(stmt)
	
        for res in res:
            return res.name

    @staticmethod
    def find_species_catched():

        stmt = text("SELECT (SELECT Fish.name FROM Fish WHERE Fish.id = Catch.species_id), COUNT(Catch.species_id)"
                    " FROM Catch LEFT JOIN Fish ON Fish.id = Catch.species_id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "count":row[1]})

        return response
