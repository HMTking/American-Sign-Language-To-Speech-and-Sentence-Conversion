"""Hand-gesture classification using the trained TFLite keypoint model."""
from __future__ import annotations

import copy
import csv
import itertools
import logging

import numpy as np

logger = logging.getLogger(__name__)

# Load the TFLite interpreter. Prefer the lightweight LiteRT runtime
# (ai-edge-litert) and fall back to full TensorFlow if it isn't available.
try:
    from ai_edge_litert.interpreter import Interpreter as TFLiteInterpreter
except ImportError:  # pragma: no cover - depends on the installed runtime
    from tensorflow.lite import Interpreter as TFLiteInterpreter

_FALLBACK_LABELS = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
]


class GestureClassifier:
    """Loads the keypoint model and classifies hand landmarks into letters."""

    def __init__(self, model_path: str, labels_path: str, min_landmarks: int = 21):
        self.min_landmarks = min_landmarks
        self.labels = self._load_labels(labels_path)
        self._interpreter = None
        self._input_details = None
        self._output_details = None
        self.loaded = self._load_model(model_path)

    # ------------------------------------------------------------------ #
    #  Loading
    # ------------------------------------------------------------------ #
    def _load_model(self, model_path: str) -> bool:
        try:
            self._interpreter = TFLiteInterpreter(model_path=model_path)
            self._interpreter.allocate_tensors()
            self._input_details = self._interpreter.get_input_details()
            self._output_details = self._interpreter.get_output_details()
            logger.info("TensorFlow Lite model loaded from %s", model_path)
            return True
        except Exception as exc:
            logger.error("Could not load TFLite model: %s", exc)
            return False

    @staticmethod
    def _load_labels(labels_path: str) -> list[str]:
        try:
            with open(labels_path, encoding="utf-8-sig") as f:
                labels = [row[0] for row in csv.reader(f) if row]
            logger.info("Loaded %d gesture labels", len(labels))
            return labels
        except Exception as exc:
            logger.error("Could not load labels: %s", exc)
            return list(_FALLBACK_LABELS)

    # ------------------------------------------------------------------ #
    #  Inference
    # ------------------------------------------------------------------ #
    def predict(self, landmarks: list[list[float]]) -> tuple[str | None, float]:
        """Return ``(label, confidence)`` for a list of 21 ``[x, y]`` points."""
        if not self.loaded or not landmarks or len(landmarks) < self.min_landmarks:
            return None, 0.0

        processed = self._preprocess(landmarks)
        class_id, confidence = self._classify(processed)
        label = self.labels[class_id] if class_id < len(self.labels) else "Unknown"
        return label, confidence

    @staticmethod
    def _preprocess(landmark_list: list[list[float]]) -> list[float]:
        """Convert to wrist-relative coordinates, flatten, and normalize."""
        try:
            temp = copy.deepcopy(landmark_list)

            base_x, base_y = temp[0][0], temp[0][1]
            for point in temp:
                point[0] -= base_x
                point[1] -= base_y

            flat = list(itertools.chain.from_iterable(temp))
            max_value = max(map(abs, flat)) if flat else 1
            if max_value == 0:
                return [0.0] * 42
            return [n / max_value for n in flat]
        except Exception as exc:
            logger.error("Preprocessing error: %s", exc)
            return [0.0] * 42

    def _classify(self, landmarks: list[float]) -> tuple[int, float]:
        try:
            input_data = np.array([landmarks], dtype=np.float32)
            self._interpreter.set_tensor(self._input_details[0]["index"], input_data)
            self._interpreter.invoke()
            output = self._interpreter.get_tensor(self._output_details[0]["index"])[0]

            # Convert logits to probabilities if the model doesn't already.
            if output.min() < 0 or abs(float(output.sum()) - 1.0) > 1e-3:
                exp = np.exp(output - np.max(output))
                probs = exp / np.sum(exp)
            else:
                probs = output

            prediction = int(np.argmax(probs))
            return prediction, float(probs[prediction])
        except Exception as exc:
            logger.error("Classification error: %s", exc)
            return 0, 0.0
