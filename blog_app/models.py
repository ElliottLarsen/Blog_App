# Author: Elliott Larsen
# Date: 11/29/2022
# Description: Various data models for ORM.

"""
Importing modules.
"""
from blog_app import db

class Post(db.Model):
    """
    Post data model.
    """
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'), nullable = False)
    user = db.relationship('User', backref=db.backref('post_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

class Comment(db.Model):
    """
    Comment data model.
    """
    id = db.Column(db.Integer, primary_key = True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete = "CASCADE"))
    post = db.relationship('Post', backref = db.backref('comment_set'))
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'), nullable = False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

class User(db.Model):
    """
    User data model.
    """
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)