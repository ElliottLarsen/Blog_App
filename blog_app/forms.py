# Author: Elliott Larsen
# Date:
# Description: 

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    """
    TODO
    """
    subject = StringField("Title", validators = [DataRequired()])
    content = TextAreaField("Content", validators = [DataRequired()])

class CommentForm(FlaskForm):
    """
    TODO
    """
    content = TextAreaField('Content', validators=[DataRequired("This field is required.")])