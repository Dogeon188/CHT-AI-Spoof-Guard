import torch
from torch import nn
import torchvision.transforms as transforms
import torchvision.transforms.functional as TF
from app.api.models import ImageModel
from PIL import Image, UnidentifiedImageError
from urllib.request import urlopen
from tqdm import tqdm
from io import BytesIO
import os
import glob

from DIRE.utils import get_network, to_cuda
from .base import SpoofDetectModel, SpoofDetectResult  # Ensure proper import paths

# Set the device (GPU if available, else CPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class DIRE(SpoofDetectModel):
    def __init__(self, model_path="DIRE/lsun_adm.pth", arch='resnet50', aug_norm=True):
        """Initialize the model, load weights, and set up image transformations."""
        self.model = self.load_model(arch, model_path)
        self.aug_norm = aug_norm
        self.transform = self.get_transform()

    def load_model(self, arch, model_path):
        """Load the model architecture and its weights."""
        model = get_network(arch)  # Initialize model (e.g., ResNet50)
        state_dict = torch.load(model_path, map_location=device)

        # Handle cases where state_dict is wrapped under a 'model' key
        if 'model' in state_dict:
            state_dict = state_dict['model']

        model.load_state_dict(state_dict)
        model.eval()  # Set the model to evaluation mode
        model.to(device)  # Move the model to the appropriate device
        return model

    def get_transform(self):
        """Define the image transformations."""
        return transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
        ])

    def preprocess_image(self, image_path):
        """Load and preprocess an image for model inference."""
        image = Image.open(image_path).convert('RGB')
        img_tensor = self.transform(image)

        if self.aug_norm:
            img_tensor = TF.normalize(img_tensor, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

        return img_tensor.unsqueeze(0).to(device)  # Add batch dimension

    def inference(self, image_path):
        """Run inference on a single image and return the result."""
        img_tensor = self.preprocess_image(image_path)

        with torch.no_grad():
            prob = self.model(img_tensor).sigmoid().item()

        print(f"Probability of being synthetic: {prob:.4f}")
        confidence=prob
        return confidence
    
    def reference(self, image: ImageModel) -> SpoofDetectResult:
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

    def run_on_files(self, file_path):
        """Run inference on a single image or all images in a directory."""
        if os.path.isfile(file_path):
            file_list = [file_path]
            print(f"Testing on image: '{file_path}'")
        elif os.path.isdir(file_path):
            file_list = sorted(
                glob.glob(os.path.join(file_path, "*.jpg")) +
                glob.glob(os.path.join(file_path, "*.png")) +
                glob.glob(os.path.join(file_path, "*.JPEG"))
            )
            print(f"Testing images from directory: '{file_path}'")
        else:
            raise FileNotFoundError(f"Invalid file path: '{file_path}'")
        fake_num = 0
        for img_path in tqdm(file_list, dynamic_ncols=True, disable=len(file_list) <= 1):
            result, confidence = self.inference(img_path)
            if result == "fake":
                fake_num += 1
            # print(f"Image: {img_path}, Result: {result}, Confidence: {confidence:.4f}")

# # Example usage
# if __name__ == '__main__':
#     model = DIREInference()
#     model.run_on_files('UniversalFakeDetect/whichfaceisreal/AiArtData/AiArtData')
