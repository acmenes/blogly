"""Seed file to make sample data for db."""

from models import User, Post, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Make some users

user1 = User(first_name="Some", last_name="Guy", img_url="https://picsum.photos/100/100")
user2 = User(first_name="Cat", last_name="Lady", img_url="https://picsum.photos/100/100")
user3 = User(first_name="Millie", last_name="The Cat", img_url="https://picsum.photos/100/100")
user4 = User(first_name="Hairdresser", last_name="Octopus", img_url="https://picsum.photos/100/100")
user5 = User(first_name="delet", last_name="me pls", img_url="https://picsum.photos/100/100")

db.session.add_all([user1, user2, user3, user4, user5])
db.session.commit()

# Create sample posts

post1 = Post(id= 1, title="Wow Pokemon Go Is Fun", content="Pokemon Go is super fun, it gets you outside to walk around. Slowpoke is the best Pokemon!", user_id=1)
post2 = Post(id= 2, title="Why Do Kids Love The Taste of Cinnamon Toast Crunch", content="CTC is great, not just for kids, but adults love it too! I could sure go for a bowl of CTC right now with some oat milk! Yum!", user_id=1)
post3 = Post(id=3, title="What About CatCoin?", content="Now there's a cryptocurrency to go wtih every cat meme you have seen on the internet!", user_id=2)

db.session.add_all([post1, post2, post3])
db.session.commit()