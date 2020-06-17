from flask import render_template
from base import base

@base.route('/')
@base.route('/index')
def index():
    return render_template('index.html', title='Index home page')
