from .UnivFd import Univfd
from .DIRE_model import DIRE
from .base import SpoofDetectModel, SpoofDetectResult
from app.api.models import ImageModel
from PIL import Image, UnidentifiedImageError
from urllib.request import urlopen
from io import BytesIO
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class Ensemble(SpoofDetectModel):
    def __init__(self, univfd: Univfd, dire: DIRE):
        self.univfd = univfd
        self.dire = dire
        self.weight = [0.2, 0.8]

    def inference(self, image):
        univfd_result = self.univfd.inference(image)
        dire_result = self.dire.inference(image)
        return (univfd_result * self.weight[0] + dire_result * self.weight[1])

    def reference(self, image: ImageModel) -> SpoofDetectResult:
        try:
            with urlopen(image) as temp:
                data = temp.read()
                image = Image.open(BytesIO(data))
                prob = self.inference(image)
                result = 'spoof' if prob > 0.5 else 'real'
                confidence = (prob - 0.5) * \
                    2 if result == 'spoof' else (0.5 - prob) * 2
                return SpoofDetectResult(
                    result=result,
                    confidence=confidence
                )
        except UnidentifiedImageError:
            raise Exception("Unsupported or invalid image format")
        except Exception as e:
            raise Exception("Unknown exception occured")
