import os
from moviepy.editor import VideoFileClip

# Ruta de la carpeta que contiene los archivos de video
carpeta_videos = "POM4"

# Obtener la lista de archivos en la carpeta
archivos = os.listdir(carpeta_videos)

# Filtrar solo los archivos de video
videos = [archivo for archivo in archivos if archivo.endswith(('.mp4', '.avi', '.mkv', '.mov'))]

# Recorrer cada archivo de video
for video in videos:
    # Obtener la ruta completa del archivo de video
    ruta_video = os.path.join(carpeta_videos, video)
    
    # Crear el objeto VideoFileClip
    clip = VideoFileClip(ruta_video)
    
    # Obtener el nombre del archivo sin la extensión
    nombre_sin_extension = os.path.splitext(video)[0]
    
    # Definir la ruta de salida con la extensión .mp4
    ruta_salida = os.path.join(carpeta_videos, nombre_sin_extension + ".mp4")
    
    # Escribir el archivo de salida
    clip.write_videofile(ruta_salida)
    
    # Cerrar el clip
    clip.close()

print("La conversión ha finalizado.")
