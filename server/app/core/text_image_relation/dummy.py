# You should copy this file and implement your own model

from .base import TextImageRelationModel, TextImageRelationResult
from app.api.models import ImageModel
from GPT_prompt import DeepFakeDetector


# Implement your model here
class DummyTextImageRelationModel(TextImageRelationModel):
    def reference(self, text: str, image: ImageModel) -> TextImageRelationResult:
        # Do processing here


        detector = DeepFakeDetector()
        image_url = image
        text_description = text
        result, confidence = detector.get_confidence_score(image_url, text_description)

        
        return TextImageRelationResult(result, confidence)
