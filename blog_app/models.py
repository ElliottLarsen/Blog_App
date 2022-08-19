# Author: Elliott Larsen
# Date:
# Description: 

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

class Reply(db.Model):
    """
    Reply data model.
    """
    id = db.Column(db.Integer, primary_key = True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete = "CASCADE"))
    reply = db.relationship('Post', backref = db.backref('reply_set'))
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)