from application import db
from application.models import Base

class Fish(Base):

    name = db.Column(db.String(144), nullable=False)
    minimum_catch_size = db.Column(db.Float, nullable=False)
    closed_season_starts = db.Column(db.String, nullable=False)
    closed_season_ends = db.Column(db.String, nullable=False)
    
    def __init__(self, name, minimum_catch_size, closed_season_starts, closed_season_ends):

        self.name = name
        self.minimum_catch_size = minimum_catch_size
        self.closed_season_starts = closed_season_starts
        self.closed_season_ends = closed_season_ends
