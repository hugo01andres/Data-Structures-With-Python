# 2 listas y que a continuacion cree las

a = [1,2,3,"Hugo",1,3,9,"Alejandro"]
b = [3,1,9,6,"Itzel",1,"Emilio",8]
# Lista de palabras que aparecen en las 2 listas
union = list(set(a) | set(b))
print(f"Union: {union}")
# Lista de palabras que aparecen en la primera lista, pero no en la segunda
print(list(set(a) - set(b) ))

# Lista de palabras que aparecen en la segunda lista, pero no en la primera
print(list(set(b) - set(a) ))
# Lista de palabras que aparecen en ambas listas
interseccion = list( set(a) & set(b))
print(f"Interseccion: {interseccion}")
