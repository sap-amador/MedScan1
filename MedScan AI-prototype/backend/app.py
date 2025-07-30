from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from inference import predict_with_cam
import os

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    os.makedirs("backend/outputs", exist_ok=True)
    result, heatmap_path = predict_with_cam(file.file)
    return {
        "prediction": result,
        "heatmap": "/heatmap"
    }

@app.get("/heatmap")
def get_heatmap():
    return FileResponse("backend/outputs/heatmap.png", media_type="image/png")
