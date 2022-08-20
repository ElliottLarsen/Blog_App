# Author: Elliott Larsen
# Date:
# Description: 

"""
Importing Modules.
"""
from datetime import datetime
from flask import Blueprint, url_for, request
from werkzeug.utils import redirect
from blog_app import db
from blog_app.models import Post, Reply

bp = Blueprint('reply', __name__, url_prefix = '/reply')

@bp.route('/create/<int:post_id>', methods=('POST', ))
def create(post_id):
    """
    TODO
    """
    post = Post.query.get_or_404(post_id)
    content = request.form['content']
    reply = Reply(content = content, create_date = datetime.now())
    post.reply_set.append(reply)
    db.session.commit()
    return redirect(url_for('post.detail', post_id = post_id))