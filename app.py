"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.app_context().push()
connect_db(app)
db.create_all()

# app.config['SECRET_KEY'] = "SECRET!"
# debug = DebugToolbarExtension(app)

@app.route("/")
def user_list():
    """Displays user listing page. Main page"""

    users = User.query.all()
    return render_template('user_list.html', users=users)

@app.route("/create_user")
def enter_user():
    return render_template('create_user.html')

@app.route("/create_user", methods=["POST"])
def create_user():
    """Displays create_user page. """
    first_name = request.form['first_name']
    last_name  = request.form['last_name']
    image_url  = request.form['image_url']
    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()
    return redirect("/")

@app.route("/user_details/<int:user_id>")
def user_details(user_id):
    """Displays create_user page. """
    users=User.query.get(user_id)
    return render_template('user_details.html', users=users)

@app.route("/edit_user/<int:user_id>")
def edit_user_page(user_id):
    """Go to Edit page"""
    user=User.query.get(user_id)
    return render_template('edit_user.html', user=user)

@app.route("/edit_user/<int:user_id>", methods=["POST"])
def edit_user(user_id):
    """Edit the chosen user"""
    first_name = request.form['first_name']
    last_name  = request.form['last_name']
    image_url  = request.form['image_url']
    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()
    return redirect('/')

@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    """Edit the chosen user"""
    user=User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")