import os

# Paths relativos
video_path = "data/videos/Manzanillo_2025-03-07_OlasAltas_01.MOV"
output_folder = "data/frames_extracted"

# Crear carpeta si no existe
os.makedirs(output_folder, exist_ok=True)

# Comando FFmpeg para extraer frames
command = f"ffmpeg -i {video_path} -vsync 0 -q:v 2 {output_folder}/frame_%05d.jpg"

# Ejecutar comando
os.system(command)

print("✅ Extracción de frames completada.")
