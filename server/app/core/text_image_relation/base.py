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
