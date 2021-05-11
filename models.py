"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# user
# id [PK] (autoincrementing)
# first_name
# last_name
# image_url (profile images)

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    '''User'''

    __tablename__ = "users"

    id = db.Column(db.Integer, 
                    primary_key=True, 
                    autoincrement=True)
    first_name = db.Column(db.String(30), 
                    nullable=False, 
                    unique=False)
    last_name = db.Column(db.String(50),
                    nullable=False,
                    unique=False)
    img_url = db.Column(db.String(1000), 
                    nullable=False)

    # I could make nullable = True in case some people don't have an img