from app.core.spoof_detect.base import SpoofDetectModel, SpoofDetectResult 
import sys
sys.path.append('../UniversalFakeDetect/')
import torch
from PIL import Image
from models import get_model

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class Univfd(SpoofDetectModel):
    def __init__(self):
        self.model = get_model("CLIP:ViT-L/14")
        self.model = self.add_fc(self.model)
    
    def add_fc(self, model):
        fc_weight = torch.load("./pretrained_weights/fc_weights.pth", map_location="cpu", weights_only=True)
        model.fc.load_state_dict(fc_weight)
        model = model.eval()
        model = model.to(device)
        return model
    
    def inference(self, image_path):
        image = Image.open(image_path)
        tensor = self.model.preprocess(image)
        batch = torch.stack([tensor])
        batch = batch.to(device)

        with torch.no_grad():
            out = self.model(batch)
            out = out.sigmoid()
        out = out.cpu()
        print(out)

        out = out[0][0]
        return out
    
    def reference(self) -> SpoofDetectResult:
        image_path = './whichfaceisreal/0_real/10286.jpeg'
        prob = self.inference(image_path)
        result = 'fake' if prob > 0.5 else 'real'
        print(f'result = {result}, confidence = {prob}')
        return SpoofDetectResult(
            result=result,
            confidence=prob
        )
    
if __name__ == '__main__':
    model = Univfd()
    model.reference()





        
