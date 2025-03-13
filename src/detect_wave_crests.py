import cv2
import os
import numpy as np

input_folder = "data/frames_extracted"
output_folder = "data/frames_crest"

os.makedirs(output_folder, exist_ok=True)

def detect_wave_crests(image_path):
    frame = cv2.imread(image_path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detección de bordes
    edges = cv2.Canny(gray, 100, 200)

    # Encontrar contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    max_height = 0
    for cnt in contours:
        _, y, _, h = cv2.boundingRect(cnt)
        if y + h > max_height:
            max_height = y + h
    
    # Guardar solo si la ola tiene una altura significativa
    if max_height > gray.shape[0] * 0.6:
        cv2.imwrite(os.path.join(output_folder, os.path.basename(image_path)), frame)

# Aplicar a todos los frames
for img in os.listdir(input_folder):
    detect_wave_crests(os.path.join(input_folder, img))

print("✅ Detección de crestas completada.")
