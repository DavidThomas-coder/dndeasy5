# models.py

# Import the db object from the 'app' package
from app import db

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Define the relationship between User and Character
    characters = db.relationship('Character', backref='user', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

# Define the Character model
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(80), nullable=False)
    char_class = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    background = db.Column(db.String(300), nullable=False)

    # Define the foreign key to link each character to a user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, race, char_class, name, background):
        self.race = race
        self.char_class = char_class
        self.name = name
        self.background = background
