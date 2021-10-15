carros = ['bMw', "subaru", 'audi', 'toyota']

"""Imprimir Todos los carros con la inicial en mayuscula, excepto BMW que todas las letras son en minuscula"""
# for carro in carros:
#     if carro.lower() == 'bmw':
#         print(carro.upper())
#         print("Es mi marca favorita")
#     else:
#         print(carro.title())


"""Imprimir todos los carros excepto audi"""
# for carro in carros:
#     if carro != 'audi':
#         print(carro)


"""Comparaciones con numeros"""
# edad = 25
# print(edad == 18)

# numero_favorito = input("Ingresa mi numero favorito: ")
# if int(numero_favorito) == 15:
#     print("Correcto ese es mi numero favorito")
# else:
#     print("Fallaste, ese no es")

"""Operadores booleanos"""
# edad = 25
# print(edad < 25)
# print(edad > 25)
# print(edad <= 25)
# print(edad >= 25)

"""Multiples condiciones"""
"""Operador and"""
# edad = 15
# if edad >= 12 and edad <= 18:
#     print("Eres un adolescente")

# """Operador or"""
# if edad < 12 or edad > 18:
#     print("No eres un adolescente")


"""Busqueda dentro de una lista"""
# numeros = [23, 44, 21, 95, 5]
# busqueda = 5

# if busqueda in numeros:
#     print("Si se encuentra")
# else:
#     print("No se encuentra")

"""Calcular el costo del ticket en selva magica"""
edad = 2

# El siguiente codigo no funciona
if edad < 4:
    costo = 0
if edad < 18:
    costo = 80
if edad >= 18:
    costo = 150


costo = 0
if edad < 4:
    costo = 0
elif edad < 18:
    costo = 80
elif edad < 50:
    costo = 150
else:
    costo = 20




if edad < 4:
    costo = 0
else:
    if edad < 18:
        costo = 80
    else:
        if edad < 65:
            costo = 150
        else:
            costo = 20

print(f"Debes pagar {costo} pesos")


