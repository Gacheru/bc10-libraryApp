# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app.mod_auth.controllers import db


# Define a base model for other database tables to inherit
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, )
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


# Define a User model
class User(Base):
    __tablename__ = 'auth_user'

    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(128), nullable=False)
    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)
    # Authorisation Data: role & status
    role = db.Column(db.SmallInteger, nullable=True)
    status = db.Column(db.SmallInteger, nullable=True)

    # New instance instantiation procedure
    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return int(self.id)

    def __repr__(self):
        return '<User %r>' % self.username


# Define a Books model
class Books(Base):
    __tablename__ = 'books'

    title = db.Column(db.String(128), nullable=False, unique=True)
    prologue = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(128), nullable=False, unique=True)
    category = db.Column(db.String(128), nullable=False)
    issue_status = db.Column(db.SmallInteger, nullable=True)
    quantity = db.Column(db.SmallInteger, nullable=True)

    # New instance instantiation procedure
    def __init__(self, title, prologue, author, category,  quantity):
        self.title = title
        self.prologue = prologue
        self.author = author
        self.category = category
        self.quantity = quantity

    def get_id(self):
        return int(self.id)

    def __repr__(self):
        return '<Book %r>' % self.title


# Define a Issue model
class Issue(Base):
    __tablename__ = 'issue'

    uid = db.Column(db.Integer, nullable=True)
    bid = db.Column(db.Integer, nullable=True)
    surchange = db.Column(db.Integer, nullable=True)
    issue_status = db.Column(db.SmallInteger, nullable=True)

    # New instance instantiation procedure
    def __init__(self, uid, bid, surcharge, issue_status):
        self.uid = uid
        self.bid = bid
        self.surcharge = surcharge
        self.issue_status = issue_status

    def get_id(self):
        return int(self.id)
