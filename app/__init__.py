from flask import Flask

def create_app():
    """
    Creates and configures a Flask application instance.
    """
    app = Flask(__name__)

    # Import and register routes
    from app.routes import register_routes
    register_routes(app)

    return app
