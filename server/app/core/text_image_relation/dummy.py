# You should copy this file and implement your own model

from .base import TextImageRelationModel, TextImageRelationResult
from app.api.models import ImageModel


# Implement your model here
class DummyTextImageRelationModel(TextImageRelationModel):
    def reference(self, text: str, image: ImageModel) -> TextImageRelationResult:
        # Do processing here
        return TextImageRelationResult(result="related", confidence=0.9)
