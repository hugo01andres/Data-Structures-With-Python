# FIFO
# First In First Out

cola = ["Maria", "Alejandro", "Jose", "Mario"]

#A gregamos elemento al final de la cola
cola.append("Carla")
cola.append("Flor")

print(cola)

# Sacando elemtnos por el principio de la cola
n = cola.pop(0)

print(f"Estan atendiendo a: {n}")
print(cola)
