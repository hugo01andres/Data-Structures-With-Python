# Hacer un programa que pida 3 numeros y determine cual es el mayor

num1 = int(input("num1 -> "))
num2 = int(input("num2 -> "))
num3 = int(input("num3 -> "))


if num1 == num2 and num1 > num3 :
    print("Num1 y Num2 son mayores")
elif num2 == num3 and num2 > num1:
    print("Num2 y Num3 son mayores")
elif num1 == num3 and num1 > num2:
    print("Num1 y Num3 son mayores")
elif num1 > num2 and num1 > num3:
    print(f"Num1 es el mayor")
elif num1 < num2 and num1 > num3 :
    print("Num2 es el mayor ")
else:
    print("Num3 es el mayor")