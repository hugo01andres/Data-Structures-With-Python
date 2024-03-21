# Una tienda ofrece un descuento del 15 % sobre el total de la compra y un cliente desea saber cunato
# debera pagar finalmente por su compra

precio = float(input("Digite el precio: "))

descuento = precio * .15
precio_final = precio - descuento

print(f"El precio final a pagar es de ${precio_final:.2f}")