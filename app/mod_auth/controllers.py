# Import flask dependencies
from flask import Flask, Blueprint, request, render_template, flash, session, redirect, url_for
# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash
from passlib.hash import sha256_crypt
# Import the database object from the main app module
from app import db
# Import module forms
from app.mod_auth.forms import LoginForm, SignupForm, BookForm, IssueForm
# Import module models (i.e. User)
from app.mod_auth.models import User, Books, Issue

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
template = Blueprint('template', __name__, url_prefix='/templates')


# Set the route and accepted methods
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    print "start"
    try:
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            print "start"
            if user and check_password_hash(user.password, form.password.data):
                session['logged_id'] = True
                session['user_id'] = user.id
                session['user_id'] = user.role
                session['username'] = request.form['username']
                flash('You are now logged in. Welcome %s' % user.username)
                return redirect(url_for('auth.Dashboard'))
            print "end"
        else:
            flash('Invalid Credentials, please try again')

    except Exception as e:
        flash('Invalid Credentials')
        return render_template('index.html', form=form)

@mod_auth.route('/logout/')
def logout():
    # Tell Flask-Login to destroy the
    # session->User connection for this session.
    User()
    return redirect(url_for('index'))

@mod_auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)

    if request.method == 'POST':
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            password=sha256_crypt.encrypt((str(form.password.data)))
        )

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('Dashboard'))
    return render_template('auth/signup.html', form=form)


@mod_auth.route('/addbook', methods=['GET', 'POST'])
def addbook():
    form = BookForm(request.form)
    print form
    if request.method == 'POST':
        book = Books(
            form.title.data,
            form.author.data,
            form.category.data,
            form.quantity.data,
            form.prologue.data
        )
        db.session.add(book)
        db.session.commit()
        flash('Congratulations! you have added a new Book')
        return redirect(url_for('Dashboard'))
    return render_template('dashboard.html', form=form)


@mod_auth.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')


@mod_auth.route('/issue', methods=['GET', 'POST'])
def Issue():
    form = IssueForm(request.form)

    if request.method == 'POST' and form.validate():
        issue = Issue(form.uid.data, form.bid.data, form.surcharge.data)
        db.session.add(issue)
        db.session.commit()
        flash('Congratulations! you have added a new Book')
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html', form=form)
