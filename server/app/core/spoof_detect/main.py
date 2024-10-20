from .base import SpoofDetectModel
from .dummy import DummySpoofDetectModel
from .UnivFd import Univfd
from .ensemble import Ensemble
from .DIRE_model import DIRE


models: dict[str, SpoofDetectModel] = dict()


def register_model(model_id: str, model: SpoofDetectModel) -> SpoofDetectModel:
    models[model_id] = model
    return model


# NOTE
# Remember to register your model here
register_model("dummy", DummySpoofDetectModel())
_univfd = register_model("univfd", Univfd())
_dire = register_model("dire", DIRE())
register_model("ensemble", Ensemble(_univfd, _dire))
