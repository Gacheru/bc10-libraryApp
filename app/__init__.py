# Import flask and  SQLAlchemy template operators
from jinja2 import Environment, PackageLoader
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI (Web server Gateway Interface) application object
# Flask uses this argument to determine the root path of the application so
# that it later can find resource files relative to the location of the application
app = Flask(__name__)
oxygen = Environment(loader=PackageLoader('app', 'templates'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# @ decorator register functions as handlers for an event
@app.route('/')
@app.route('/<username>/')
@app.route('/signin/')
def index(username=None):
    return render_template('index.html', user=username)



@app.route('/signup/')
def Registration():
    return render_template('auth/signup.html'), 404


@app.route('/dashboard/<int:id>/<int:role>/<username>')
def Dashboard(id, role,username):
    books = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6', 'Book7', 'Book8']
    return render_template('dashboard.html', id=id, role=role,username=username, books=books), 404


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
