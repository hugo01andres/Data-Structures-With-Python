
#Revisar si los numeros son pares o no
num1 = int(input("num1 -> "))
num2 = int(input("num2 -> "))

if num1%2 == 0 and num2%2 == 0:
    print("Num1 y Num2 son pares")
elif num1%2==0 and not num2%2 == 0:
    print("Num1 es par y Num2 es impar")
elif num2%2==0 and not num1%2 == 0:
    print("Num2 es par y Num1 es impar")
else:
    print("los 2 numeros son impares")