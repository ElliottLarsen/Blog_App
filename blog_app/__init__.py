# Author: Elliott Larsen
# Date:
# Description: 

"""
Importing modules.
"""
from flask import Flask

def create_app():
    """
    Application factory.
    """
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app