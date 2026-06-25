"""Spell-checking: word autocomplete and pre-speech correction."""
from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class SpellingService:
    """Wraps :mod:`pyspellchecker` for suggestions and corrections."""

    def __init__(self, distance: int = 1):
        self.available = False
        self._spell = None
        try:
            from spellchecker import SpellChecker

            self._spell = SpellChecker(distance=distance)
            self.available = True
            logger.info("Spell checker loaded")
        except Exception as exc:  # pragma: no cover - optional dependency
            logger.error("Spell checker unavailable: %s", exc)

    def suggest(self, prefix: str, limit: int = 3) -> list[str]:
        """Return up to ``limit`` dictionary words starting with ``prefix``,
        ranked by frequency and returned uppercase."""
        prefix = (prefix or "").strip().lower()
        if not prefix or not self.available:
            return []

        freq = self._spell.word_frequency
        matches = [w for w in freq.dictionary if w.startswith(prefix)]
        matches.sort(key=lambda w: freq.dictionary[w], reverse=True)
        return [w.upper() for w in matches[:limit]]

    def correct(self, text: str) -> str:
        """Spell-correct each word while preserving the original casing."""
        if not self.available or not text:
            return text

        corrected = []
        for word in text.split():
            lower = word.lower()
            if self._spell.known([lower]):
                corrected.append(word)
                continue
            guess = self._spell.correction(lower)
            if guess:
                corrected.append(guess.upper() if word.isupper() else guess)
            else:
                corrected.append(word)
        return " ".join(corrected)
