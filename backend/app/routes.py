# Import the 'app' instance from the 'app' package (This import is necessary)
from app import app

# Define your routes and view functions here

# Example route
@app.route('/')
def hello_world():
    return 'Hello Worldddd!'
