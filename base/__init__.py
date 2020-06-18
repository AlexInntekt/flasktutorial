from flask import Flask
from .config import Config

base = Flask(__name__)
base.config.from_object(Config)

from base import routes
