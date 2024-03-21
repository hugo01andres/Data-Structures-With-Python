# Elimine los elementos repetidos, por ultimo mostrar la lista

"""La solucion fue convertirlo a conjunto"""

lista = [1,2,3,"Hugo", 2,2,1,"Hugo", 3]
conjunto = set(lista)

lista = list(conjunto)

print(lista)

