# Import Form and RecaptchaField (optional)
# Import Form elements such as TextField and BooleanField (optional)
# Import Form validators
from wtforms import Form, PasswordField, BooleanField, StringField, validators

# Define the login form (WTForms)
class LoginForm(Form):
    email = StringField('Email Address', [validators.DataRequired(message='Forgot your email address?')])
    password = PasswordField('Password', [validators.DataRequired(message='Must provide a password!')])


class SignupForm(Form):
    first_name = StringField('First_name', [validators.Length(min=4, max=20)])
    last_name = StringField('Last_name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password',[validators.DataRequired(),
                              validators.EqualTo('confirm', message='Passwords must match.')])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the <a href="/tos/">Terms Of Service</a> and the <a href="/tos/">Privarcy Notice</a> (Last updated Oct 20 2016)', [validators.DataRequired()])

class BookForm(Form):
    title = StringField('Title', [validators.Length(min=10, max=15)])
    prologue = StringField('Prologue', [validators.Length(min=10, max=100)])
    author = StringField('Author', [validators.Length(min=4, max=25)])
    img_url = StringField('Image', [validators.Length(min=6, max=35)])
    category = StringField('Category', [validators.Length(min=6, max=35)])
    quantity = StringField('Quantity', [validators.Length(min=6, max=35)])

class IssueForm(Form):
    uid = StringField('User', [validators.Length(min=10, max=15)])
    bid = StringField('Book', [validators.Length(min=10, max=100)])
    surcharge = StringField('Surcharge', [validators.Length(min=4, max=25)])