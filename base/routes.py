from base import base

@base.route('/')
@base.route('/index')
def index():
    return "Hello world, from Flask!"
