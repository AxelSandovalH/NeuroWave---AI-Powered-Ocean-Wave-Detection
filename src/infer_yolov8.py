from ultralytics import YOLO
import torch
import cv2
import glob
import os

# Cargar modelo YOLO entrenado
model = YOLO("models/best.pt")

# Verificar si CUDA está disponible
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Ruta de imágenes a analizar
images = glob.glob("data/frames_extracted/*.jpg")

# Crear carpeta para guardar los frames detectados
output_folder = "data/frames_crest"
os.makedirs(output_folder, exist_ok=True)

# Detectar olas en cresta
for img_path in images:
    results = model(img_path, device=device)  # Inferencia con GPU o CPU
    
    # Si se detecta una ola en cresta, guardar la imagen
    if len(results[0].boxes) > 0:
        frame = cv2.imread(img_path)
        cv2.imwrite(f"{output_folder}/{os.path.basename(img_path)}", frame)

print("✅ Inferencia completada. Frames clasificados y guardados.")
