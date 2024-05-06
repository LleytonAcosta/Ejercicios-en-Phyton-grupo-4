import threading
import time

# Dos puertas (recursos) que no se pueden compartir
puerta_A = threading.Lock()
puerta_B = threading.Lock()

# Funcion para el primer hilo
def hilo_1():
    print("Hilo 1: Comenzando ejecucion")  # Imprimir al inicio
    # Intenta abrir las puertas en orden fijo: primero A, luego B
    puerta_A.acquire()  # Adquiere puerta A
    print("Hilo 1 abrio puerta A")

    # Espera un poco antes de intentar abrir la puerta B
    time.sleep(1)

    # Intenta abrir la puerta B
    puerta_B.acquire()  # Ahora adquiere puerta B
    print("Hilo 1 abrio puerta B")

    # Liberar ambas puertas al final
    puerta_B.release()
    puerta_A.release()
    print("Hilo 1: Finalizando ejecucion")

# Funcion para el segundo hilo
def hilo_2():
    print("Hilo 2: Comenzando ejecucion")  # Imprimir al inicio
    # Sigue el mismo orden: primero A, luego B
    puerta_A.acquire()  # Adquiere puerta A
    print("Hilo 2 abrio puerta A")

    # Espera un poco antes de intentar abrir la puerta B
    time.sleep(1)

    puerta_B.acquire()  # Luego adquiere puerta B
    print("Hilo 2 abrio puerta B")

    # Liberar ambas puertas al final
    puerta_B.release()
    puerta_A.release()
    print("Hilo 2: Finalizando ejecucion")

# Creamos dos hilos
thread_1 = threading.Thread(target=hilo_1)
thread_2 = threading.Thread(target=hilo_2)

# Iniciamos ambos hilos
print("Iniciando hilos")  # Para ver si la ejecución comienza
thread_1.start()
thread_2.start()

# Esperamos a que terminen
thread_1.join()
thread_2.join()

print("Ejemplo completado")  # Ver si el código llegó al final
