# Author: Elliott Larsen
# Date: 11/29/2022
# Description: Main views.

"""
Importing modules.
"""
from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect
from blog_app.models import Post

bp = Blueprint('main', __name__, url_prefix = '/')

@bp.route('/')
def main_page():
    """
    Main view with the list of posts.
    """
    post_list = Post.query.order_by(Post.create_date.desc())
    return render_template('post_list.j2', post_list = post_list)

@bp.route('/about')
def about_page():
    """
    About page.
    """
    return render_template('about_page.j2')

