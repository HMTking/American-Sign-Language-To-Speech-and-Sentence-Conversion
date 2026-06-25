"""Page routes."""
from __future__ import annotations

from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    """Serve the single-page web app."""
    return render_template("index.html")
