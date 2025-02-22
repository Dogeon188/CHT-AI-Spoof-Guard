from openai import OpenAI
import json

from .base import TextImageRelationModel, TextImageRelationResult
from app.api.models import ImageModel


with open("api_key.txt", "r") as f:
    api_key = f.read()


class GPTTextImageRelationModel(TextImageRelationModel):
    def __init__(self):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)
        self.threshold = 0.5

    def reference(self, text: str, image: ImageModel) -> TextImageRelationResult:
        image_url = image
        text_description = text
        result, confidence = self.get_confidence_score(
            image_url, text_description)

        return TextImageRelationResult(result, confidence)

    def get_confidence_score(self, image_url, text_description):
        # Define the system and user prompts
        messages = [
            {"role": "system", "content": "You are a deepfake news detector. Please help find the content that will assess image and text relation."},
            {"role": "user", "content": [
                {"type": "text",
                    "text": "I will give you an image URL and this image's CHINESE STATEMENT. Please return two things: 1. The image and description CONFIDENCE SCORE (from 0 to 100) to show their relation 2. Why you gave this score?"},
                {"type": "image_url", "image_url": {"url": image_url}},
                {"type": "text", "text": text_description},
                {"type": "text", "text": "Output format:json with score key and reason key"},
            ]}
        ]

        # Send the prompt to the OpenAI API
        try:
            response = self.client.chat.completions.create(
                model="gpt-4-turbo",
                messages=messages,
                max_tokens=300
            )

        except Exception as e:
            raise RuntimeError("Failed to get GPT response.")

        # Extract the score using regular expression
        result_text = response.choices[0].message.content
        # print(result_text)
        data = json.loads(result_text)
        score = data['score']/100

        related_str = self.get_related_result(score)

        return related_str, score

    def get_related_result(self, score):
        return "related" if score >= self.threshold else "unrelated"
