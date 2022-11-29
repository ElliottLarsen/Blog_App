# Author: Elliott Larsen
# Date: 11/29/2022
# Description: Configuration for the application

import os

BASE_DIR = os.path.dirname(__file__)

# Database access address.
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'blog_app.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "this_is_not_a_secret_key"