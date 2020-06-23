from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

base = Flask(__name__)
base.config.from_object(Config)
db = SQLAlchemy(base)
migrate = Migrate(base, db)


from base import routes, models
