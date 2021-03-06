
"""This program does not accept actual audio file in the form of formdata, it just emulates its CRUD operations on the server"""


from flask import Flask, app
from dotenv import load_dotenv
from flask_mongoengine import MongoEngine
import os
from api.routes import create_routes
from flask_restful import Api#install

load_dotenv()

default_config = {
    "MONGODB_SETTINGS": {
        'db': os.environ["APP"],
        'host': os.environ["HOST"],
        'port': 0,
    }
}


flask_app = Flask(__name__)


flask_app.config.update(default_config)

mongo = MongoEngine(flask_app)





""" Initializing the flask app with configurations and connection to the database"""
def main_flask_app():

    api = Api(app=flask_app)
    
    create_routes(api=api)


    return flask_app


if __name__ == '__main__':
    app = main_flask_app()
    app.run()
    

