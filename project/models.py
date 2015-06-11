# project/models.py


import datetime

from project import db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    scorecards = db.relationship("ScoreCard", backref="user")


    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {0}>'.format(self.email)



class Hole(db.Model):
    """ June 7th: not going to use this for now"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hole_number = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer, nullable=False)


class Score(db.Model):
    """ every time a player plays a hole, add one of these
    June 7th: will do basic ScoreCard for now.
    """
    __tablename__ = "scores"
    # Number of Strokes
    # Amount Over or Under Par

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num_strokes = db.Column(db.Integer)

class ScoreCard(db.Model):
    """ A collection of Score's """
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    __tablename__ = "scorecards"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # saving scores just as a string for now
    # ex. 1-3,2-4,3-9
    # Hole 1: 3 strokes, Hole 2: 4 strokes, Hole 3: 9 strokes. etc.
    scores = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))



"""
ScoreCard-
id
User (in future can add other User's to the card)
Date (when it was created)
Course Name (String - in future can be a selection of all real courses or whatever)
Location (not mandatory)


"""