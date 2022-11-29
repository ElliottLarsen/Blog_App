# Author: Elliott Larsen
# Date: 11/29/2022
# Description: Views with /create route.

"""
Importing Modules.
"""
from datetime import datetime
from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect
from ..forms import CommentForm
from blog_app import db
from blog_app.models import Post, Comment
from .auth_views import login_required

bp = Blueprint('comment', __name__, url_prefix = '/comment')

@bp.route('/create/<int:post_id>', methods=('POST', ))
@login_required
def create(post_id):
    """
    Create a comment to a post.
    """
    form = CommentForm()
    post = Post.query.get_or_404(post_id)
    if form.validate_on_submit():
        content = request.form['content']
        comment = Comment(content = content, create_date = datetime.now(), user = g.user)
        post.comment_set.append(comment)
        db.session.commit()
        return redirect(url_for('post.detail', post_id = post_id))
    return render_template('post_detail.j2', post = post, form = form)

@bp.route('/edit/<int:comment_id>', methods=('GET', 'POST'))
@login_required
def edit(comment_id):
    """
    Edit a post.
    """
    comment = Comment.query.get_or_404(comment_id)
    if g.user != comment.user:
        flash('You do not have access to edit')
        return redirect(url_for('post.detail', post_id = comment.post.id))
    if request.method == "POST":
        form = CommentForm()
        if form.validate_on_submit():
            form.populate_obj(comment)
            comment.modify_date = datetime.now()  
            db.session.commit()
            return redirect(url_for('post.detail', post_id = comment.post.id))
    else:
        form = CommentForm(obj=comment)
    return render_template('comment_form.j2', form=form)

@bp.route('/delete/<int:comment_id>')
@login_required
def delete(comment_id):
    """
    Delete a post.
    """
    comment = Comment.query.get_or_404(comment_id)
    post_id = comment.post.id
    if g.user != comment.user:
        flash('You do not have access to delete.')
    else:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('post.detail', post_id = post_id))