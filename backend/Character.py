from app import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.string(80), unique=True, nullable=False)
    class = db.Column(db.string(80), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    background = db.Column(db.String(300), unique=True, nullable=False)

    def __init__(self, race, class, name, background):
        self.race = race
        self.class = class
        self.name = name
        self.background = background

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))