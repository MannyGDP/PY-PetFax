from flask import Flask

def create_app():
    app = Flask(__name__)

    # index route
    @app.route('/')
    def index(): 
        return 'Hello, Pet Facts!'

    from . import pet 
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    return app