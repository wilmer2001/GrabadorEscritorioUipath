import pyautogui
import cv2
import numpy as np
import threading
import time
import os
import sys
from datetime import datetime

# Función para crear el archivo detener_grabacion.txt si no existe
def crear_archivo_detener_grabacion():
    if not os.path.exists("detener_grabacion.txt"):
        with open("detener_grabacion.txt", "w") as f:
            f.write("")

# Función para reducir la calidad de la imagen
def reducir_calidad_imagen(img, calidad):
    # Convertir imagen a formato JPEG con calidad específica
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), calidad]
    _, img_encoded = cv2.imencode('.jpg', img, encode_param)
    return cv2.imdecode(img_encoded, 1)

# Función para grabar el escritorio
def grabar_escritorio(directorio:str):
    crear_archivo_detener_grabacion()
    pantalla = pyautogui.size()
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    fecha_hora = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    ruta_archivo = os.path.join(directorio, f"{fecha_hora}.mp4")
    
    # Establecer el número de fotogramas por segundo (fps) del video
    fps = 3
    
    salida = cv2.VideoWriter(ruta_archivo, codec, fps, pantalla)
    grabando = True
    
    # Iniciar la grabación
    while grabando:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # Reducir calidad de la imagen al 30%
        frame = reducir_calidad_imagen(frame, calidad=30)
        
        salida.write(frame)

        time.sleep(2.0)  # Ajustar la velocidad del video aquí

        with open("detener_grabacion.txt", "r") as f:
            contenido = f.read().strip()
            if contenido == "Detener grabación":
                grabando = False

    salida.release()

if len(sys.argv) >= 2:
    directorio = sys.argv[1]
#else:
#    directorio = "D:/Reportes/"
hilo_grabacion = threading.Thread(target=grabar_escritorio, args=(directorio,))
hilo_grabacion.start()
