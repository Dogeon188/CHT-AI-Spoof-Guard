import torch
from PIL import Image, UnidentifiedImageError
from .UniversalFakeDetect.models.clip_models import CLIPModel
import os
from urllib.request import urlopen
from io import BytesIO

from .base import SpoofDetectModel, SpoofDetectResult
from app.api.models import ImageModel

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class Univfd(SpoofDetectModel):
    def __init__(self):
        self.model = CLIPModel("ViT-L/14")
        self.model = self.add_fc(self.model)

    def add_fc(self, model):
        cur_dir = os.path.dirname(__file__)
        weight_path = os.path.join(
            cur_dir, "UniversalFakeDetect/pretrained_weights/fc_weights.pth")
        fc_weight = torch.load(
            weight_path, map_location="cpu", weights_only=True)
        model.fc.load_state_dict(fc_weight)
        model = model.eval()
        model = model.to(device)
        return model

    def inference(self, image):
        tensor = self.model.preprocess(image)
        batch = torch.stack([tensor])
        batch = batch.to(device)

        with torch.no_grad():
            out = self.model(batch)
            out = out.sigmoid()
        out = out.cpu()

        out = out[0][0]
        return out

    def reference(self, image: ImageModel) -> SpoofDetectResult:
        # with tempfile.NamedTemporaryFile() as temp:
        #     temp.write(image)
        #     temp.seek(0)
        try:
            with urlopen(image) as temp:
                data = temp.read()
                image = Image.open(BytesIO(data))
                prob = self.inference(image)
                result = 'spoof' if prob > 0.5 else 'real'
                confidence = (prob - 0.5) * 2 if result == 'spoof' else (0.5 - prob) * 2
                return SpoofDetectResult(
                    result=result,
                    confidence=confidence
                )
        except UnidentifiedImageError:
            raise Exception("Unsupported or invalid image format")
        except Exception as e:
            raise Exception("Unknown exception occured")


# if __name__ == '__main__':
#     model = Univfd()
#     model.reference()
