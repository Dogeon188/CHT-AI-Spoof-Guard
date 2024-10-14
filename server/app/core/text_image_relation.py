from abc import ABC, abstractmethod
from time import time

from app.api.models import TextImageRelationRequest, TextImageRelationResponse


class TextImageRelationModel(ABC):
    @abstractmethod
    def reference(self, req: TextImageRelationRequest) -> TextImageRelationResponse:
        raise NotImplementedError


models: dict[str, TextImageRelationModel] = dict()


def _register_model(model_id: str, model: TextImageRelationModel) -> TextImageRelationModel:
    models[model_id] = model
    return model


class DummyTextImageRelationModel(TextImageRelationModel):
    def reference(self, req: TextImageRelationRequest) -> TextImageRelationResponse:
        current_time = time()

        return TextImageRelationResponse(
            uuid=req.uuid,
            model=req.model,
            processing_time={
                "start": current_time,
                "end": current_time,
                "duration_ms": 0},
            result="related",
            confidence=0.9
        )


_register_model("dummy", DummyTextImageRelationModel())


# TODO
# Add actual model(s) here
