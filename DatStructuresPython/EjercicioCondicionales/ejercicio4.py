# Hacer un programa que funcione como calculadora

print(""" Bienvenido a la calculadora
Suma: s
Resta: r
Multiplicacion: m
Division: d""")
operacion = input("Ingrese que operacion desea: ").lower()

a = float(input("Num1 -> "))
b = float(input("Num2 -> "))

if operacion == 's':
    print(f"La suma de {a} + {b} = {a+b}")
elif operacion == 'r':
    print(f"La resta de {a} - {b} = {a - b}")
elif operacion == 'm':
    print(f"La multiplicacion de {a} * {b} = {a * b}")
elif operacion == "d":
    print(f"La division de {a} / {b} = {a / b:.2f}")
else:
    print("No eligio que operacion")

