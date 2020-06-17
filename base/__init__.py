from flask import Flask

base = Flask(__name__)

from base import routes
