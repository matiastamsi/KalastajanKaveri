from application import db
from application.models import Base

from sqlalchemy.sql import text

class Fish(Base):

    name = db.Column(db.String(144), nullable=False, unique=True)
    minimum_catch_size = db.Column(db.Integer)
    closed_season_starts = db.Column(db.String)
    closed_season_ends = db.Column(db.String)

    catches = db.relationship("Catch", lazy=True)
    
    def __init__(self, name, minimum_catch_size, closed_season_starts, closed_season_ends):

        self.name = name
        self.minimum_catch_size = minimum_catch_size
        self.closed_season_starts = closed_season_starts
        self.closed_season_ends = closed_season_ends

    @staticmethod
    def find_id_based_on_name(name=0):
        stmt = text("SELECT Fish.id FROM Fish WHERE Fish.name = :name").params(name=name)
        res = db.engine.execute(stmt)
	
        for res in res:
            return res.id

    #Function to get only day.
    def getDay(self, dateToSplit):
        return dateToSplit.split('.')[0]
    #Function to get only month.
    def getMonth(self, dateToSplit):
        return dateToSplit.split('.')[1]
