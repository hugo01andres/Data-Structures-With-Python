
def opciones():
    print("""
    1. Ingresar dinero
    2.Retirar dinero:
    3.Mostrar dinero
    4.Salir""")

print("""Bienvenido al cajero automatico
Saldo = $1000""")
opciones()
opc = input("Opcion -> ")
saldo = 1000
while opc !=4:
    if opc == '1':
       saldo_agregar = int(input("Saldo a agregar -> "))
       saldo += saldo_agregar
       saldo_agregar = 0
    elif opc == '2':
        saldo_restar = int(input("Saldo a retirar -> "))
        saldo -= saldo_restar
        saldo_restar = 0
    elif opc == '3':
        print(f"Su saldo es: {saldo}")
    elif opc == '4':
        print("Gracias por jugar")
        break
    else:
        print("No ha elegido una opcion correcta")
    opciones()
    opc = input("Opcion -> ")


