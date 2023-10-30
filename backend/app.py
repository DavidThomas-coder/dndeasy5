from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import User, Character

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://davidthomas@localhost/dndeasy_development'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello Worldddd!'

if __name__ == '__main__':
    app.run(debug=True)