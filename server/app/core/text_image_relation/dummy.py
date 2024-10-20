# You should copy this file and implement your own model
from time import sleep
from random import random

from .base import TextImageRelationModel, TextImageRelationResult
from app.api.models import ImageModel


# Implement your model here
class DummyTextImageRelationModel(TextImageRelationModel):
    def reference(self, text: str, image: ImageModel) -> TextImageRelationResult:
        # Do processing here
        sleep(0.2)
        confidence = random()
        return TextImageRelationResult(
            result="related" if confidence > 0.5 else "unrelated",
            confidence=confidence
        )
