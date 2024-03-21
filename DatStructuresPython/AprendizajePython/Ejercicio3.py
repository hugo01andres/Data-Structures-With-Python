# Hacer un programa para intercambiar el valor de 2 variables

a = float(input("Ingresa valor A: "))
b = float(input("Ingresa valor B: "))

print(f"El valor de A es: {a}")
print(f"El valor de B es {b}")
aux = 0

#Hacemos la logica del cambio
aux = a
a = b
b = aux


print(f"\n\nEl nuevo valor de A es: {a}")
print(f"El nuevo valor de B es {b}")


