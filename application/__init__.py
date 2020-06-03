"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')
    assets = Environment(app)

    with app.app_context():
        # Import parts of our application
        from .home import home
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(home.home_bp)

        # Compile static assets
        compile_static_assets(assets)

        return app
