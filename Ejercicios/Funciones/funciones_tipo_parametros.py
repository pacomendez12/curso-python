valor = 15
lista = [1, 2, 3]

def otra_mas(y):
    y.append(15)

def haz_algo(x):
    x = 25

def haz_algo_mas(x):
    otra_mas(x)
    x.append(10)


haz_algo(valor)
haz_algo_mas(lista)




print(valor)
print(lista)


