"""Text-to-speech synthesis using gTTS."""
from __future__ import annotations

import base64
import logging
import os
import tempfile

from gtts import gTTS

logger = logging.getLogger(__name__)


def synthesize(text: str, lang: str = "en") -> str:
    """Generate speech for ``text`` and return base64-encoded MP3 data.

    Raises
    ------
    ValueError
        If ``text`` is empty.
    """
    if not text or not text.strip():
        raise ValueError("No text provided")

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
            temp_path = temp_file.name

        gTTS(text=text, lang=lang, slow=False).save(temp_path)

        with open(temp_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    finally:
        if temp_path and os.path.exists(temp_path):
            os.unlink(temp_path)
