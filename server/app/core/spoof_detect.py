from abc import ABC, abstractmethod
from time import time

from app.api.models import SpoofDetectRequest, SpoofDetectResponse


class SpoofDetectModel(ABC):
    @abstractmethod
    def reference(self, req: SpoofDetectRequest) -> SpoofDetectResponse:
        raise NotImplementedError


models: dict[str, SpoofDetectModel] = dict()


def _register_model(model_id: str, model: SpoofDetectModel) -> SpoofDetectModel:
    models[model_id] = model
    return model


class DummySpoofDetectModel(SpoofDetectModel):
    def reference(self, req: SpoofDetectRequest) -> SpoofDetectResponse:
        current_time = time()

        return SpoofDetectResponse(
            uuid=req.uuid,
            model=req.model,
            processing_time={
                "start": current_time,
                "end": current_time,
                "duration_ms": 0},
            result="real",
            confidence=0.9
        )


_register_model("dummy", DummySpoofDetectModel())
