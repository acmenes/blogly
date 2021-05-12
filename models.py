"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# user
# id [PK] (autoincrementing)
# first_name
# last_name
# image_url (profile images)

#### CLASSES ####

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

    # posts = db.relationship('Post')

    def __repr__(self):
        u = self
        return f"<Users {u.id} {u.first_name} {u.last_name}>"

# class Post(db.Model):
#     '''Post'''

#     __tablename__ = "posts"

#     id = db.Column(db.Integer, 
#                     primary_key=True, 
#                     autoincrement=True)
#     title = db.Column(db.String(100), 
#                     nullable=False, 
#                     unique=False)

#     def __repr__(self):
#         p = self
#         return f"<Employee {p.id} {p.title}>"

# copying this logic from the videos, might need to use something like this?

# def get_user_posts():
#     all_user_posts = Posts.query.all()

#     for post in user_posts:

# class PostTag(db.Model):

# class Tag(db.Model):

def connect_db(app):
    '''Connect the db to our app'''

    db.app = app
    db.init_app(app)
    
if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from app import app
    connect_db(app)

    db.drop_all()
    db.create_all()
    example_data()