import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "lab_equipment.db"),
    )

    if test_config is not None:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    from app.routes.item_routes import items_bp
    from app.routes.loan_routes import loans_bp

    app.register_blueprint(items_bp)
    app.register_blueprint(loans_bp)

    return app
