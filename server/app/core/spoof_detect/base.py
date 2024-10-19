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
