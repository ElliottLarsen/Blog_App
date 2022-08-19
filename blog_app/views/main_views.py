# Author: Elliott Larsen
# Date:
# Description: 

"""
Importing modules.
"""
from flask import Blueprint, render_template
from blog_app.models import Post

bp = Blueprint('main', __name__, url_prefix = '/')

@bp.route('/')
def main_page():
    post_list = Post.query.order_by(Post.create_date.desc())
    return render_template('post_list.html', post_list = post_list)

@bp.route('/about')
def about_page():
    return "About page."

@bp.route('/post/<int:post_id>/')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post = post)