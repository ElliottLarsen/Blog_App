# Author: Elliott Larsen
# Date:
# Description: 

"""
Importing modules.
"""
from datetime import datetime
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect
from .. import db
from ..forms import PostForm, CommentForm
from blog_app.models import Post
from blog_app.forms import PostForm
from blog_app.views.auth_views import login_required

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
@login_required
def create():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        post = Post(subject = form.subject.data, content = form.content.data, create_date = datetime.now(), user = g.user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.main_page'))
    return render_template('post_form.html', form = form)

@bp.route('/edit/<int:post_id>', methods=('GET', 'POST'))
@login_required
def edit(post_id):
    """
    TODO
    """
    post = Post.query.get_or_404(post_id)
    if g.user != post.user:
        flash('You do not have access to edit.')
        return redirect(url_for('post.detail', post_id = post_id))
    if request.method == 'POST':  
        form = PostForm()
        if form.validate_on_submit():
            form.populate_obj(post)
            post.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('post.detail', post_id = post_id))
    else:  
        form = PostForm(obj = post)

    return render_template('post_form.html', form=form)

@bp.route('/delete/<int:post_id>')
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if g.user != post.user:
        flash('You do not have access to delete.')
        return redirect(url_for('post.detail', post_id = post_id))
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.main_page'))