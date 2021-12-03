"""Genera los numeros primos entre el 2 y el 1000 e imprime la lista"""

res = []
for x in range(2, 1001):
    es_primo = True
    for divisor in range(2, x):
        if x % divisor == 0:
            es_primo = False
    
    if es_primo:
        res.append(x)

print(res)
