"""Blogly application."""

from flask import Flask, redirect, request, render_template
from models import db, connect_db, User, Post
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
    new_posts= Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template('home.html', new_posts=new_posts)

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
    '''Display the user profile'''
    idnum = user_id - 1
    user = User.query.all()
    return render_template('userprofile.html', user=user[idnum])

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    '''Edit the user's profile'''
    idnum = user_id - 1
    user = User.query.get_or_404(user_id)
    # user.first_name=request.form['first_name']
    # user.last_name=request.form['last_name']
    # user.img_url=['img_url']
    return render_template('edituserprofile.html', user=user[idnum])

@app.route('/users/<int:user_id>/delete')
def delete_user():
    idnum = user_id - 1
    return 'delete user'

@app.route('/users/<int:user_id>/posts')
def user_posts(user_id):
    idnum = user_id - 1
    user = User.query.get_or_404(user_id)
    return render_template('userposts.html',user=user)

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def user_new_post():
    return 'make new post'

# POSTING ROUTES

@app.route('/users/<int:user_id>/posts/new', methods=["GET"])
def new_post(user_id):
    user = User.query.get_or_404(user_id)
    idnum = user_id - 1
    user = User.query.get_or_404(user_id)
    return render_template('createpost.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def create_post(user_id):
    '''Adds a user post to the db'''
    user = User.query.get_or_404(user_id)
    new_post=Post(
        title=request.form['title'],
        content=request.form['content'],
        user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    return redirect('/users/<int:user_id>', user=user)

@app.route('/posts/<int:post_id>')
def show_posts(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@app.route('/posts<int:post_id>/edit')
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    return 'edit this post' 

@app.route('/posts<int:post_id>/delete')
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    return 'delete this post' 


#### OTHER NOTES

# get_or_404() could be useful too

# db.session.query(User.full_name)
# db.session.query(User.id)