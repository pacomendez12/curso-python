

lista = ["uno", "dos", "tres"]

#lista2 = lista
lista2 = lista[:]

lista.append("cuatro")
lista2.append("diez")


print(lista) # 1, 2, 3, 4, 10
print(lista2) # 1, 2, 3, 4, 10
