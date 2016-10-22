# Import flask and  SQLAlchemy template operators
from jinja2 import Environment, PackageLoader
from flask import Flask, request, render_template, flash, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI (Web server Gateway Interface) application object
# Flask uses this argument to determine the root path of the application so
# that it later can find resource files relative to the location of the application


app = Flask(__name__)
env = Environment(loader=PackageLoader('app', 'templates'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# @ decorator register functions as handlers for an event
@app.route('/')
#@app.route('/<username>')
def index(username=None):
    return render_template('index.html', user=username)


@app.route('/signup', methods=['GET', 'POST'])
def Registration():
    return render_template('auth/signup.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def Dashboard(books=None, users=None):
    from mod_auth.models import Books,User
    books = Books.query.all() or None
    users = User.query.all() or None
    return render_template('dashboard.html', books=books, users=users)


# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
