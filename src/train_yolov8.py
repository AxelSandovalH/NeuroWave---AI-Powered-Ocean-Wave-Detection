from ultralytics import YOLO

# Cargar modelo preentrenado
model = YOLO("yolov8n.pt")

# Entrenar con dataset propio
model.train(data="config.yaml", epochs=50, imgsz=640, batch=16, device="cuda")

# Guardar modelo
model.save("models/best.pt")

print("✅ Entrenamiento finalizado. Modelo guardado en 'models/best.pt'")
