"""WSGI entry point for production servers (e.g. ``gunicorn wsgi:app``)."""
import logging

from asl_app import create_app

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

app = create_app()
