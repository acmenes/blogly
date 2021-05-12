"""Seed file to make sample data for db."""

from models import User
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Make some users

user1 = User(first_name="Some", last_name="Guy", img_url="https://picsum.photos/100/100")
user2 = User(first_name="Cat", last_name="Lady", img_url="https://picsum.photos/100/100")
user3 = User(first_name="Millie", last_name="The Cat", img_url="https://picsum.photos/100/100")

db.session.add_all([user1, user2, user3])
db.session.commit()