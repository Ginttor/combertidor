import os
from moviepy.editor import VideoFileClip

def convertir_mp4_a_gif(archivo_mp4, duracion=5):
    nombre_sin_extension = os.path.splitext(archivo_mp4)[0]
    clip = VideoFileClip(archivo_mp4)
    clip_duration = clip.duration
    if clip_duration < duracion:
        duracion = clip_duration
    clip.subclip(0, duracion).write_gif(nombre_sin_extension + ".gif", fps=10)

def convertir_todos_los_mp4_en_carpeta(carpeta):
    archivos_mp4 = [archivo for archivo in os.listdir(carpeta) if archivo.endswith(".mp4")]
    for archivo_mp4 in archivos_mp4:
        convertir_mp4_a_gif(os.path.join(carpeta, archivo_mp4))

carpeta_pogf = "POGF"
convertir_todos_los_mp4_en_carpeta(carpeta_pogf)
