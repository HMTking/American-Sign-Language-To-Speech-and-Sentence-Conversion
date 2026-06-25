"""ASL-to-Speech Flask application package.

Exposes the :func:`create_app` application factory used by the WSGI entry
points (``wsgi.py`` / ``app.py``) and the test suite.
"""
from __future__ import annotations

from flask import Flask

from .config import BaseConfig, get_config
from .services.classifier import GestureClassifier
from .services.spelling import SpellingService


def create_app(config: type[BaseConfig] | str | None = None) -> Flask:
    """Build and configure a Flask application instance.

    Parameters
    ----------
    config:
        A config class, an environment name (``"development"`` /
        ``"production"`` / ``"testing"``), or ``None`` to use ``FLASK_ENV``.
    """
    app = Flask(__name__)

    config_class = config if isinstance(config, type) else get_config(config)
    app.config.from_object(config_class)

    # Initialize services once and attach them to the app for the blueprints.
    app.extensions["classifier"] = GestureClassifier(
        model_path=app.config["MODEL_PATH"],
        labels_path=app.config["LABELS_PATH"],
        min_landmarks=app.config["MIN_LANDMARKS"],
    )
    app.extensions["spelling"] = SpellingService(
        distance=app.config["SPELL_DISTANCE"],
    )

    # Register routes.
    from .routes.main import main_bp
    from .routes.api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    return app
