# Author: Elliott Larsen
# Date:
# Description: 

"""
Importing modules.
"""
from flask import Blueprint, render_template
from blog_app.models import Post

bp = Blueprint('post', __name__, url_prefix = '/post')

@bp.route('/list/')
def post_list():
    """
    TODO
    """
    post_list = Post.query.order_by(Post.create_date.desc())
    return render_template('post_list.html', post_list = post_list)

@bp.route('/detail/<int:post_id>/')
def detail(post_id):
    """
    TODO
    """
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post = post)