from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from app.config import Config
from app.extension import db

from app.routes.marca.routes import marca_blueprint

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(marca_blueprint, url_prefix="/marca")

    return app
