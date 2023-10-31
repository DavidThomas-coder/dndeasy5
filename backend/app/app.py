# app.py

# Import the Flask framework
from flask import Flask

# Import the SQLAlchemy extension for database operations
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application
app = Flask(__name)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://davidthomas@localhost/dndeasy_development'

# Create an instance of the SQLAlchemy extension and associate it with the app
db = SQLAlchemy(app)

# Import your routes and models after initializing the db
from app import routes
from app.models import User, Character

# Define a route and view function
@app.route('/')
def hello_world():
    return 'Hello Worldddd!'

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
