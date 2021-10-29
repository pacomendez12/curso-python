
def es_primo(x):
    for divisor in range(2, x):
        if x % divisor == 0:
            return False
    return True

def genera_primos(n):
    res = []
    for x in range(2, n + 1):
        if es_primo(x):
            res.append(x)
    return res

print(genera_primos(1000))
