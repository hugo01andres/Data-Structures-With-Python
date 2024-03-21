# Hcer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circumferencia
from math import pi

r = float(input("R -> "))

print(f"Area: {(pi * r**2) :.2f}")
print(f"Longitud: {(2 * pi * r) :.2f}")
