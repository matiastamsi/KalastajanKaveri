from application import db, bcrypt
from application.models import Base
from sqlalchemy.sql import text


class User(Base): #User gets id, date_created and date_modified
                  #from the Base.

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False, unique=True)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    role = db.Column(db.Integer, nullable= False) #USER: 1, ADMIN: 2, OWNER: 3

    catches = db.relationship("Catch", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.role = 1 #New user gets user priviledges at first.

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def setToAdmin(self):
        self.role = 2

    def setToOwner(self):
        self.role = 3

    def roles(self):
        response = [] # Method returns list of roles.
        if self.role == 1:
            response.append("USER")
        elif self.role == 2:
            response.append("ADMIN") # Administor has also user priviledges.
            response.append("USER")
        elif self.role == 3:
            response.append("OWNER") #Owner has all the priviledges.
            response.append("ADMIN")
            response.append("USER")
        return response
