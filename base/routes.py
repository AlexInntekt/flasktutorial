from flask import render_template
from base import base
from base.forms import LoginForm

@base.route('/')
@base.route('/index')
def index():
    user = {'username':'Alex_the_brave447'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Index home page', user=user, posts=posts)

@base.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
