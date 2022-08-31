# Author: Elliott Larsen
# Date:
# Description: 

"""
Importing Modules
"""

from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from blog_app import db
from blog_app.forms import SignUpForm, LoginForm
from blog_app.models import User

import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        """
        TODO
        """
        if g.user is None:
            _next = request.url if request.method == 'GET' else ''
            return redirect(url_for('auth.login', next=_next))
        return view(*args, **kwargs)
    return wrapped_view

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    """
    TODO
    """
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if not user:
            user = User(username = form.username.data,
                        password = generate_password_hash(form.password_1.data),
                        email = form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.main_page'))
        else:
            flash('The user already exists.')
    return render_template('signup.html', form=form)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    """
    TODO
    """
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username = form.username.data).first()
        if not user:
            error = "The user does not exist."
        elif not check_password_hash(user.password, form.password.data):
            error = "This is an incorrect password."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            _next = request.args.get('next', '')
            if _next:
                return redirect(_next)
            else:
                return redirect(url_for('main.main_page'))
        flash(error)

    return render_template('login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    """
    TODO
    """
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

@bp.route('/logout/')
def logout():
    """
    TODO
    """
    session.clear()
    return redirect(url_for('main.main_page'))
