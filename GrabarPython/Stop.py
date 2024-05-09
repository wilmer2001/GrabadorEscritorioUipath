import os
import time

def detener_grabador():
    ruta_archivo = "detener_grabacion.txt"
    with open(ruta_archivo, "w") as f:
        f.write("Detener grabación")
    print("Se ha enviado la señal para detener la grabación.")
    time.sleep(2)
    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)
        print("Archivo 'detener_grabacion.txt' eliminado.")

detener_grabador()
