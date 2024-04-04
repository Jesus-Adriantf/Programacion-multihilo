import threading
import time
import random

# Función que será ejecutada por cada hilo
def tarea():
    nombre_hilo = threading.current_thread().name
    print(f"{nombre_hilo} empezó.")
    # Dormir durante un tiempo aleatorio
    time.sleep(random.randint(1, 5))
    print(f"{nombre_hilo} terminó.")

def principal():
    # Número de hilos que deseamos crear
    numero_de_hilos = 5
    # Lista para mantener las referencias a los hilos
    hilos = []
    # Creamos y ejecutamos los hilos
    for i in range(numero_de_hilos):
        hilo = threading.Thread(target=tarea, name=f"Hilo-{i+1}")
        hilo.start()
        hilos.append(hilo)
    # Esperamos a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

if __name__ == "__main__":
    principal()


