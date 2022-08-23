# Author: Elliott Larsen
# Date:
# Description: 

"""
Importing modules.
"""
from datetime import datetime
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from .. import db
from ..forms import PostForm, CommentForm
from blog_app.models import Post
from blog_app.forms import PostForm

bp = Blueprint('post', __name__, url_prefix = '/post')


@bp.route('/detail/<int:post_id>/')
def detail(post_id):
    """
    TODO
    """
    form = CommentForm()
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post = post, form = form)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        post = Post(subject = form.subject.data, content = form.content.data, create_date = datetime.now())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.main_page'))
    return render_template('post_form.html', form = form)