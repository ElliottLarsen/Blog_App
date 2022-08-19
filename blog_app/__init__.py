# Author: Elliott Larsen
# Date:
# Description: 

"""
Importing modules.
"""
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """
    Application factory.
    """
    app = Flask(__name__)
    app.config.from_object(config)

    # Set Up ORM.
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    
    # Register blueprint.
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app