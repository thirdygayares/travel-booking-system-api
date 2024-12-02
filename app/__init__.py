from flask import Flask, jsonify
from flask_smorest import Api

from app.extension import db, migrate, bcrypt, jwt, cors
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    api = Api(app)



    @app.route('/')
    def home():
        return jsonify({"message": "Hello World"})

    return app