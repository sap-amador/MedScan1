import torch
import pydicom
import numpy as np
import cv2
from monai.transforms import Resize, ScaleIntensity
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget

class DummyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 3, padding=1)
        self.pool = torch.nn.AdaptiveAvgPool2d(1)
    def forward(self, x):
        return self.pool(self.conv(x)).view(-1, 1)

model = DummyModel()
model.eval()

def predict_with_cam(file):
    ds = pydicom.dcmread(file)
    img = ds.pixel_array.astype(np.float32)
    img_resized = Resize((224, 224))(img)
    img_norm = ScaleIntensity()(img_resized)
    input_tensor = torch.tensor(img_norm).unsqueeze(0).unsqueeze(0)

    cam = GradCAM(model=model, target_layers=[model.conv], use_cuda=False)
    grayscale_cam = cam(input_tensor=input_tensor, targets=[ClassifierOutputTarget(0)])[0]
    rgb_img = np.stack([img_norm]*3, axis=-1)
    visualization = show_cam_on_image(rgb_img / np.max(rgb_img), grayscale_cam, use_rgb=True)

    heatmap_path = "backend/outputs/heatmap.png"
    cv2.imwrite(heatmap_path, visualization[:, :, ::-1])
    return torch.sigmoid(model(input_tensor)).item(), heatmap_path
