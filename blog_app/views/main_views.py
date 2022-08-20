# Author: Elliott Larsen
# Date:
# Description: 

"""
Importing modules.
"""
from flask import Blueprint, url_for
from werkzeug.utils import redirect
from blog_app.models import Post

bp = Blueprint('main', __name__, url_prefix = '/')

@bp.route('/')
def main_page():
    """
    TODO
    """
    return redirect(url_for('post.post_list'))

@bp.route('/about')
def about_page():
    """
    TODO
    """
    return "About page."