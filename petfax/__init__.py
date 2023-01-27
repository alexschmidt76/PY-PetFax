# config
from flask import Flask
from flask_migrate import Migrate

# factory
def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True # for flask run --reload to update templates without needing to restart server in terminal

    # sqlalchemy database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Aborted5732@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # landing page
    @app.route('/')
    def hello():
        return 'Hello, PetFax'

    # register pet blueprint
    from . import pet, fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    # return the app
    return app