# Author: Elliott Larsen
# Date:
# Description: 

"""
Importing modules.
"""
from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix = '/')

@bp.route('/')
def main_page():
    return "Hello, World!"

@bp.route('/about')
def about_page():
    return "About page."

@bp.route('/post')
def post_page():
    return "Post page."