from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.api.models import ImageModel


@dataclass
class SpoofDetectResult:
    result: str
    confidence: float


class SpoofDetectModel(ABC):
    @abstractmethod
    def reference(self, image: ImageModel) -> SpoofDetectResult:
        raise NotImplementedError


models: dict[str, SpoofDetectModel] = dict()


def _register_model(model_id: str, model: SpoofDetectModel) -> SpoofDetectModel:
    models[model_id] = model
    return model


class DummySpoofDetectModel(SpoofDetectModel):
    def reference(self, image: ImageModel) -> SpoofDetectResult:
        # Do processing here
        return SpoofDetectResult(result="real", confidence=0.9)


_register_model("dummy", DummySpoofDetectModel())


# TODO
# Add actual model(s) here
