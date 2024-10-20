# You should copy this file and implement your own model
from time import sleep
from random import random

from .base import SpoofDetectModel, SpoofDetectResult
from app.api.models import ImageModel


# Implement your model here
class DummySpoofDetectModel(SpoofDetectModel):
    def reference(self, image: ImageModel) -> SpoofDetectResult:
        # Do processing here
        sleep(0.2)
        confidence = random()
        return SpoofDetectResult(
            result="spoof" if confidence > 0.5 else "real",
            confidence=confidence)
