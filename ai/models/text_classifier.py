"""Placeholder text classifier for initial AI integration wiring."""


class TextClassifier:
    """A tiny rule-based placeholder for future ML model integration."""

    def predict(self, text: str) -> tuple[str, float]:
        normalized = text.lower()
        if any(token in normalized for token in ("error", "risk", "urgent")):
            return "high_priority", 0.86
        if any(token in normalized for token in ("help", "question", "request")):
            return "support", 0.74
        return "general", 0.61
