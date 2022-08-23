# Author: Elliott Larsen
# Date:
# Description: 

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
    TODO
    """
    post_list = Post.query.order_by(Post.create_date.desc())
    return render_template('post_list.html', post_list = post_list)

@bp.route('/about')
def about_page():
    """
    TODO
    """
    return render_template('about_page.html')

