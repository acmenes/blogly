"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://picsum.photos/100/100"

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
                    nullable=False, default=DEFAULT_IMAGE_URL)

    posts = db.relationship('Post', backref='user', cascade='all, delete-orphan')

    # @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}>"

class Post(db.Model):
    '''Post'''

    __tablename__ = "posts"

    id = db.Column(db.Integer, 
                    primary_key=True, 
                    autoincrement=True)
    title = db.Column(db.String(100), 
                    nullable=False, 
                    unique=False)
    content = db.Column(db.String(10000), 
                    nullable=False)
    created_at = db.Column(db.DateTime, 
                    nullable=False, 
                    default=datetime.datetime.now)
    user_id = db.Column(db.Integer, 
                    db.ForeignKey('users.id'), 
                    nullable=False)

    def __repr__(self):
        p = self
        return f"<post {p.id} {p.title}>"

class Tag(db.Model):
    '''Tags'''

    __tablename__ = "tags"

    id = db.Column(db.Integer, 
                    primary_key=True)
    name = db.Column(db.String(15), 
                    nullable=False, 
                    unique=True)

    posts = db.relationship('Post', 
                            secondary='posts_tags', 
                            cascade="all, delete", 
                            backref="tags")

class PostTag(db.Model):
    '''Tag that is added to posts'''

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, 
                        db.ForeignKey('posts.id'), 
                        primary_key=True)
    tag_id = db.Column(db.Integer, 
                        db.ForeignKey('tags.id'), 
                        primary_key=True)

def connect_db(app):
    '''Connect the db to our app'''

    db.app = app
    db.init_app(app)
    
# if __name__ == "__main__":
#     # As a convenience, if we run this module interactively, it will leave
#     # you in a state of being able to work with the database directly.

#     # So that we can use Flask-SQLAlchemy, we'll make a Flask app

#     from app import app
#     connect_db(app)

#     db.drop_all()
#     db.create_all()
#     example_data()