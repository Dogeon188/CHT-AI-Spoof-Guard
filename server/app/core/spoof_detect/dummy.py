# You should copy this file and implement your own model

from .base import SpoofDetectModel, SpoofDetectResult
from app.api.models import ImageModel


# Implement your model here
class DummySpoofDetectModel(SpoofDetectModel):
    def reference(self, image: ImageModel) -> SpoofDetectResult:
        # Do processing here
        return SpoofDetectResult(result="real", confidence=0.9)
