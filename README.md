🌊 Detección de Crestas de Olas con YOLOv8
Este proyecto utiliza YOLOv8 para detectar crestas de olas en videos capturados en Manzanillo, Colima. Se extraen fotogramas de los videos y se filtran aquellos donde la ola alcanza su punto más alto, creando así un dataset optimizado para entrenamiento.


📌 Requisitos
🖥️ Hardware
Servidor Ubuntu con RTX 3050 (CUDA habilitado)
Procesador Intel Core i5-10400 con gráficos integrados
Almacenamiento mínimo recomendado: 50GB (expandible con SSD externo)
📦 Dependencias
Antes de ejecutar los scripts, asegúrate de tener instalado:

Python 3.12
YOLOv8 (Ultralytics)
OpenCV con soporte CUDA
FFmpeg
PyTorch con CUDA
🔧 Instalación de Dependencias
Ejecuta los siguientes comandos en tu entorno virtual:


pip install ultralytics opencv-contrib-python torch torchvision torchaudio ffmpeg-python
Verifica que todo esté correctamente instalado:


python src/check_environment.py
🚀 Uso del Proyecto
1️⃣ Extraer Frames de los Videos

python src/extract_frames.py
📌 Entrada: Videos en data/videos/
📌 Salida: Frames en data/frames_extracted/

2️⃣ Filtrar Crestas de Olas

python src/detect_wave_crests.py
📌 Entrada: Frames de data/frames_extracted/
📌 Salida: Solo los frames con crestas en data/frames_crest/

3️⃣ Entrenar YOLOv8

python src/train_yolov8.py
📌 Requiere dataset etiquetado en Roboflow
📌 Salida: Modelo YOLO entrenado en models/best.pt

4️⃣ Ejecutar Inferencia con YOLO

python src/infer_yolov8.py
📌 Entrada: Frames extraídos en data/frames_extracted/
📌 Salida: Solo los frames clasificados como "olas en cresta" en data/frames_crest/

📊 Visualización de Resultados
Puedes utilizar Matplotlib o cualquier visor de imágenes para revisar los frames guardados en data/frames_crest/:

eog data/frames_crest/frame_00001.jpg
💡 Futuras Mejoras
Implementar detección en tiempo real con una cámara IP usando OpenCV y YOLO.
Optimizar la selección de frames con técnicas de procesamiento de imágenes.
Mejorar la predicción de la altura de las olas.
🤝 Contribuciones
Si deseas colaborar en este proyecto, puedes hacer un fork del repositorio y enviar un pull request con mejoras.

🏆 Créditos
Desarrollado por Axel Sandoval para su tesis en la Facultad de Ingeniería Electromecánica.

📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes utilizarlo y modificarlo libremente.

🔹 ¡Listo para entrenar y detectar crestas de olas! 🌊 🚀
