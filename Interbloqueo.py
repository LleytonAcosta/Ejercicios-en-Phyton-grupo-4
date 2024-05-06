import threading
import time

# Dos puertas (recursos) que no se pueden compartir
puerta_A = threading.Lock()
puerta_B = threading.Lock()


# Función para el primer hilo
def hilo_1():
    print("Hilo 1: Comenzando ejecucion")  # Imprimir al inicio
    # Intenta abrir la puerta A
    puerta_A.acquire()
    print("Hilo 1 abrio puerta A")

    # Espera un poco antes de intentar abrir la puerta B
    time.sleep(1)

    # Intenta abrir la puerta B
    print("Hilo 1 intenta abrir puerta B")
    puerta_B.acquire()  # Aquí podría quedarse atascado si la puerta B está ocupada

    # Si consigue abrir la puerta B, cierra ambas puertas al final
    puerta_B.release()
    puerta_A.release()
    print(" Hilo 1: Finalizando ejecucion")

# Función para el segundo hilo
def hilo_2():
    print("Hilo 2: Comenzando ejecucion")  # Imprimir al inicio
    # Intenta abrir la puerta B
    puerta_B.acquire()
    print("Hilo 2 abrio puerta B")

    # Espera un poco antes de intentar abrir la puerta A
    time.sleep(1)

    # Intenta abrir la puerta A
    print("Hilo 2 intenta abrir puerta A")
    puerta_A.acquire()  # Aquí podría quedarse atascado si la puerta A está ocupada

    # Si consigue abrir la puerta A, cierra ambas puertas al final
    puerta_A.release()
    puerta_B.release()
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
