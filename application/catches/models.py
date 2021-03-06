from application import db
from application.auth.models import User
from application.models import Base

from sqlalchemy.sql import text

import datetime

class Catch(Base): #Catch gets id, date_created and date_modified
                   #from the Base.
    lure_or_fly = db.Column(db.String(144), nullable=False)
    length = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    spot = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)
    private_or_public = db.Column(db.String(144), nullable=False)

    #Catch refers to both user and fish.
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    species_id = db.Column(db.Integer, db.ForeignKey('fish.id'))

    def __init__(self, lure_or_fly, length, weight, spot, description, private_or_public):
        self.lure_or_fly = lure_or_fly
        self.length = length
        self.weight = weight
        self.spot = spot
        self.description = description
        self.private_or_public = private_or_public

    def getDate(self): #Include only day, month and year (no hours etc.)
        d = self.date_created
        return (str(d.day) + '.' + str(d.month) + '.' + str(d.year))

    @staticmethod
    def find_fisher_based_on_id(id=0):
        stmt = text("SELECT name "
                    "FROM account "
                    "WHERE id = :id").params(id=id)
        res = db.engine.execute(stmt)
        for res in res:
            return res.name

    @staticmethod
    def find_name_based_on_id(id=0):
        stmt = text("SELECT Fish.name "
                    "FROM Fish "
                    "WHERE Fish.id = :id").params(id=id)
        res = db.engine.execute(stmt)
        for res in res:
            return res.name

    @staticmethod
    def find_species_catched(): #One of those raw SQL-queries that needed.
        stmt = text("SELECT Fish.name, "
                    "COUNT(Catch.species_id) as count "
                    "FROM Fish "
                    "LEFT JOIN Catch ON Fish.id = Catch.species_id "
                    "GROUP BY Fish.name "
                    "ORDER BY count DESC")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "count":row[1]})
        return response

    @staticmethod
    def find_biggest_catch(): #One of those raw SQL-queries that needed.
        stmt = text("SELECT Fish.name, Catch.weight, account.name "
                    "FROM Catch "
                    "LEFT JOIN Fish ON Catch.species_id = Fish.id "
                    "LEFT JOIN account ON Catch.account_id = account.id "
                    "WHERE Catch.private_or_public ='public' "                  
                    "ORDER BY Catch.weight DESC").params(id=id)
        res = db.engine.execute(stmt)
        for row in res:
            if row[0] == None or row[1] == None or row[2] == None:
                return None
            else:
                return (row[0] + ", as heavy as " + str(row[1])
                        + " kg and the lucky fisher was " + row[2] + "!")
