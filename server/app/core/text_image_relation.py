from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.api.models import ImageModel


@dataclass
class TextImageRelationResult:
    result: str
    confidence: float


class TextImageRelationModel(ABC):
    @abstractmethod
    def reference(self, text: str, image: ImageModel) -> TextImageRelationResult:
        raise NotImplementedError


models: dict[str, TextImageRelationModel] = dict()


def _register_model(model_id: str, model: TextImageRelationModel) -> TextImageRelationModel:
    models[model_id] = model
    return model


class DummyTextImageRelationModel(TextImageRelationModel):
    def reference(self, text: str, image: ImageModel) -> TextImageRelationResult:
        # Do processing here
        return TextImageRelationResult(result="related", confidence=0.9)


_register_model("dummy", DummyTextImageRelationModel())


# TODO
# Add actual model(s) here
