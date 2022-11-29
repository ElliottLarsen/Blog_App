# Author: Elliott Larsen
# Date: 11/29/2022
# Description: Models for various forms.

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class PostForm(FlaskForm):
    """
    Post form model.
    """
    subject = StringField("Title", validators = [DataRequired()])
    content = TextAreaField("Content", validators = [DataRequired()])

class CommentForm(FlaskForm):
    """
    Comment form model.
    """
    content = TextAreaField('Content', validators=[DataRequired("This field is required.")])

class SignUpForm(FlaskForm):
    """
    Signup form model.
    """
    username = StringField("Username", validators = [DataRequired(), Length(min = 3, max = 25)])
    password_1 = PasswordField("Password", validators = [DataRequired(), EqualTo("password_2", "Passwords must match.")])
    password_2 = PasswordField("Re-enter password", validators = [DataRequired()])
    email = EmailField("Email", validators = [DataRequired(), Email()])

class LoginForm(FlaskForm):
    """
    Login form model.
    """
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('password', validators=[DataRequired()])