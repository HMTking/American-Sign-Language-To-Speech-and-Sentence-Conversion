"""Development entry point.

Run with ``python app.py`` for a local server. Production deployments use a
WSGI server pointing at :mod:`wsgi` (``gunicorn wsgi:app``).
"""
import logging
import os

from asl_app import create_app

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=app.config["DEBUG"])
