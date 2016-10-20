# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
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
    error = ''
    try:
        form = LoginForm(request.form)
        if request.method == 'POST':
            return render_template('signin.html')

        # Verify the sign in form
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            print (user)
            # if user and check_password_hash(user.password, form.password.data):
            #     session['logged_id'] = True
            #     session['user_id'] = user.id
            #     session['user_id'] = user.role
            #     session['username'] = request.form['username']
            #     flash('You are now logged in. Welcome %s' % user.username)
            #     return redirect(url_for('Dashboard'))
            #     return redirect(url_for('index'))
            # else:
            #     error = 'Wrong email or password, please try again'
        return render_template('auth/signin.html', error=error)
    except Exception as e:
        flash(e)
        return render_template("auth/signin.html", error=error)


@mod_auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    error = ''
    try:
        form = SignupForm(request.form)

        if request.method == 'POST' and form.validate:
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
            return redirect(url_for('index'))
        return render_template('auth/signup.html', form=form)
    except Exception as e:
        flash(e)
        return render_template("auth/signup.html", error=error)


@mod_auth.route('/addbook/', methods=['GET', 'POST'])
def Addbook():
    form = BookForm(request.form)

    if request.method == 'POST':
        book = Books(
            form.title.data,
            form.author.data,
            form.prologue.data,
            form.img_url.data,
            form.category.data,
            form.quantity.data,
        )
        db.session.add(book)
        db.session.commit()
        flash('Congratulations! you have added a new Book')
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html', form=form)


@mod_auth.route('/issue/', methods=['GET', 'POST'])
def Issue():
    form = IssueForm(request.form)

    if request.method == 'POST':
        issue = Issue(
            form.uid.data,
            form.bid.data,
            form.surcharge.data
        )
        db.session.add(issue)
        db.session.commit()
        flash('Congratulations! you have added a new Book')
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html', form=form)

# @view_config( route_name="data", request_method="GET", renderer="json")
# def Books(request):
#     table = datatables.DataTable(request.GET, Books, Books.query, [
#         "id",
#         ("title", "title", lambda i: "Books: {}".format(i.title)),
#         ("title", "title.author"),
#     ])
#     table.add_data(link=lambda o: request.route_url("dashboard", id=o.id))
#
#     return table.json()
