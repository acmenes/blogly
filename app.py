"""Blogly application."""

from flask import Flask, redirect, request, render_template
# from models import db, connect_db, User
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MissMillieIsGood'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# connect_db(app)
# db.create_all()

@app.route('/')
def point_users():
    return redirect('/users')

@app.route('/users')
def user_directory():
    return render_template('users.html')

@app.route('/users/new', methods=["POST"])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url']

    user = User(first_name=first_name, last_name=last_name, img_url=img_url)

    db.session.add(user)
    db.session.commit()

    return render_template('newuser.html')

@app.route('/users/<int:user_id>/edit')
def edit_user():
    return 'edit user'


@app.route('/users/<int:user_id>/delete')
def delete_user():
    return 'delete user'

@app.route('/users/<int:user_id>')
def user_profile(user_id):
    return 'user profile'