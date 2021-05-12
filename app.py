"""Blogly application."""

from flask import Flask, redirect, request, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'MissMillieIsGood'

connect_db(app)
db.create_all()

@app.route('/')
def point_users():
    return redirect('/users')

@app.route('/users')
def user_directory():
    '''Shows all the users'''
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/new', methods=["GET"])
def user_form():
    return render_template('newuser.html')

@app.route('/users/new', methods=["POST"])
def add_user():
    '''Adds a new user to the db'''
    new_user= User(
    first_name = request.form['first_name'],
    last_name = request.form['last_name'],
    img_url = request.form['img_url'] or None)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

# USER ROUTES 

@app.route('/users/<int:user_id>')
def user_profile(user_id):
    user = User.query.all()
    return render_template('userprofile.html', user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user():
    return 'edit user'

@app.route('/users/<int:user_id>/delete')
def delete_user():
    return 'delete user'

@app.route('/users/<int:user_id>/posts')
def user_posts(user_id):
    return 'user posts'

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def user_new_post():
    return 'make new post'

# POSTING ROUTES

# @app.route('posts<int:post_id>')
# def show_posts():
#     return 'posts'

# @app.route('posts<int:post_id>/edit')
# def edit_post():
#     return 'edit this post' 

# @app.route('posts<int:post_id>/delete')
# def delete_post():
#     return 'delete this post' 


#### OTHER NOTES

# get_or_404() could be useful too