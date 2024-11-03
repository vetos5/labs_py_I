from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

register_routes(app, mongo)

if __name__ == '__main__':
    app.run(debug=True)
