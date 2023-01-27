from flask import Flask

# factory
def create_app():
    app = Flask(__name__)

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