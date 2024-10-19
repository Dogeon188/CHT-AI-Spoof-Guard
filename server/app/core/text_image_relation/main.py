from .base import TextImageRelationModel
from .dummy import DummyTextImageRelationModel

models: dict[str, TextImageRelationModel] = dict()


def register_model(model_id: str, model: TextImageRelationModel) -> TextImageRelationModel:
    models[model_id] = model
    return model


# NOTE
# Remember to register your model
register_model("dummy", DummyTextImageRelationModel())
