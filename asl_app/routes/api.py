"""JSON API routes: classification, suggestions, speech, health."""
from __future__ import annotations

import logging

from flask import Blueprint, current_app, jsonify, request

from ..services import speech

logger = logging.getLogger(__name__)

api_bp = Blueprint("api", __name__)


def _classifier():
    return current_app.extensions["classifier"]


def _spelling():
    return current_app.extensions["spelling"]


@api_bp.route("/process_frame", methods=["POST"])
def process_frame():
    """Classify an ASL gesture from 21 hand landmarks sent by the browser."""
    try:
        data = request.get_json(silent=True) or {}
        landmarks = data.get("landmarks")
        if not landmarks:
            return jsonify({"error": "No landmark data", "success": False})

        gesture, confidence = _classifier().predict(landmarks)
        return jsonify({"gesture": gesture, "confidence": confidence, "success": True})
    except Exception as exc:
        logger.error("Processing error: %s", exc)
        return jsonify({"error": str(exc), "success": False})


@api_bp.route("/suggest", methods=["POST"])
def suggest():
    """Return up to N dictionary words that start with the given prefix."""
    try:
        data = request.get_json(silent=True) or {}
        limit = current_app.config["SUGGESTION_LIMIT"]
        suggestions = _spelling().suggest(data.get("prefix", ""), limit=limit)
        return jsonify({"suggestions": suggestions, "success": True})
    except Exception as exc:
        logger.error("Suggest error: %s", exc)
        return jsonify({"suggestions": [], "success": False})


@api_bp.route("/generate_speech", methods=["POST"])
def generate_speech():
    """Synthesize speech from text, optionally spell-correcting it first."""
    try:
        data = request.get_json(silent=True) or {}
        text = (data.get("text") or "").strip()
        autocorrect = data.get("autocorrect", True)

        if not text:
            return jsonify({"error": "No text provided", "success": False})

        if autocorrect:
            text = _spelling().correct(text)

        audio = speech.synthesize(text, lang=current_app.config["TTS_LANG"])
        return jsonify({"audio": audio, "text": text, "success": True})
    except Exception as exc:
        logger.error("Speech generation error: %s", exc)
        return jsonify({"error": str(exc), "success": False})


@api_bp.route("/health")
def health():
    """Health check endpoint."""
    classifier = _classifier()
    return jsonify({
        "status": "healthy",
        "model_loaded": classifier.loaded,
        "labels_count": len(classifier.labels),
        "labels": classifier.labels[:5],
    })
