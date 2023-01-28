from flask_migrate import Migrate

from . import app, db

migrate = Migrate(app, db)
