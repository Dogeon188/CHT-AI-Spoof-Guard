from .base import SpoofDetectModel
from .dummy import DummySpoofDetectModel
from .UnivFd import Univfd


models: dict[str, SpoofDetectModel] = dict()


def register_model(model_id: str, model: SpoofDetectModel) -> SpoofDetectModel:
    models[model_id] = model
    return model


# NOTE
# Remember to register your model here
register_model("dummy", DummySpoofDetectModel())
register_model("univfd", Univfd())
