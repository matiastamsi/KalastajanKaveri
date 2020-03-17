from application import db

class Catch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    specie = db.Column(db.String(144), nullable=False)
    lure_or_fly = db.Column(db.Boolean, nullable=False)
    length = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    spot_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(144), nullable=False)
    private_or_public = db.Column(db.Boolean, nullable=False)

    def __init__(self, specie, lure_or_fly, length, weight, spot_id, user_id, description, private_or_public):
        self.specie = specie
        self.lure_or_fly = lure_or_fly
        self.length = length
        self.weight = weight
        self.spot_id = spot_id
        self.user_id = user_id
        self.description = description
        self.private_or_public = private_or_public
