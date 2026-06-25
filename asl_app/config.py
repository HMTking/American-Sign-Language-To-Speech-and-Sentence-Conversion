"""Application configuration objects.

Settings are layered: :class:`BaseConfig` holds shared defaults and the
environment-specific subclasses override them. The active config is chosen by
the ``FLASK_ENV`` environment variable (see :func:`get_config`).
"""
from __future__ import annotations

import os
from pathlib import Path

# Repository root (two levels up from this file: asl_app/config.py -> repo/)
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "keypoint_classifier"


class BaseConfig:
    """Settings shared by every environment."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "asl-detection-dev-key")

    # Model assets
    MODEL_PATH = str(MODEL_DIR / "keypoint_classifier.tflite")
    LABELS_PATH = str(MODEL_DIR / "keypoint_classifier_label.csv")

    # Inference
    MIN_LANDMARKS = 21

    # Spell-checker / autocomplete
    SUGGESTION_LIMIT = 3
    SPELL_DISTANCE = 1

    # Text-to-speech
    TTS_LANG = "en"

    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class TestingConfig(BaseConfig):
    TESTING = True


_CONFIG_MAP = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}


def get_config(name: str | None = None) -> type[BaseConfig]:
    """Return the config class for ``name`` (or the ``FLASK_ENV`` value)."""
    key = (name or os.environ.get("FLASK_ENV", "production")).lower()
    return _CONFIG_MAP.get(key, ProductionConfig)
