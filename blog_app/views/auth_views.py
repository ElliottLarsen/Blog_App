# Author: Elliott Larsen
# Date:
# Description: 

"""
Importing Modules
"""

from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from blog_app import db
from blog_app.forms import SignUpForm
from blog_app.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
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