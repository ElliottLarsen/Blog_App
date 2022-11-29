# Author: Elliott Larsen
# Date: 11/29/2022
# Description: Views with /auth route.

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
        If g.user exists, perform the function this decorator is applied to.  Otherwise, reroute to login().
        """
        if g.user is None:
            _next = request.url if request.method == 'GET' else ''
            return redirect(url_for('auth.login', next=_next))
        return view(*args, **kwargs)
    return wrapped_view

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    """
    Perform signup if POST.  Otherwise, display the signup view.
    """
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if not user:
            try:
                user = User(username = form.username.data,
                            password = generate_password_hash(form.password_1.data),
                            email = form.email.data)
                db.session.add(user)
                db.session.commit()
                return render_template('signup_success.j2', name = user.username)
            except:
                flash('Username and/or Email has already been taken.')
        else:
            flash('Username and/or Email has already been taken.')
    return render_template('signup.j2', form=form)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    """
    Perform login if POST.  Otherwise, display login view.
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

    return render_template('login.j2', form=form)

@bp.before_app_request
def load_logged_in_user():
    """
    Get the logged in user.
    """
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

@bp.route('/logout/')
def logout():
    """
    Perform logout by clearing out the session value.
    """
    session.clear()
    return redirect(url_for('main.main_page'))
