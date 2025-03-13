import torch
import cv2
import os

print("🔍 Verificando entorno...\n")

# Revisar GPU
print(f"🚀 CUDA Disponible: {torch.cuda.is_available()}")
print(f"🖥️ Cantidad de GPUs: {torch.cuda.device_count()}")

# Revisar OpenCV con CUDA
print(f"📷 OpenCV CUDA: {cv2.cuda.getCudaEnabledDeviceCount()}")

# Revisar FFmpeg
ffmpeg_version = os.popen("ffmpeg -version").read()
print(f"🎥 FFmpeg:\n{ffmpeg_version}")

print("✅ Entorno listo.")
