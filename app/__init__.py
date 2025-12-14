from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'change-this-later'

    from app import routes
    routes.init_app(app)

    return app


