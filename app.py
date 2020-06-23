from base import base, db
from base.models import User, Post

@base.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
