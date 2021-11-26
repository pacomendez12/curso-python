
"""2 Positional parameters"""
def describe_animal(tipo_de_animal, nombre_de_animal):
    print(f"Tengo un animal de tipo {tipo_de_animal}")
    print(f"Mi {tipo_de_animal} se llama {nombre_de_animal}")

"""2 keyword parameters"""
def describe_animal_argumentos_keyword(tipo_de_animal = "Perro", nombre_de_animal = "Perry"):
    print(f"Tengo un animal de tipo {tipo_de_animal}")
    print(f"Mi {tipo_de_animal} se llama {nombre_de_animal}")


#describe_animal("perro", "perry")
#describe_animal("perro", "firulais")


# mascotas = [("Gato", "Garfield"), ("Conejo", "Bugs Bunny"), ("perro", "Perry")]

# for mascota_nombre in mascotas:
#     describe_animal(mascota_nombre[0], mascota_nombre[1])

# describe_animal("Conejo", "Bugs Bunny")

#describe_animal_argumentos_keyword("Conejo")
# """Llamar funciones desde otras funciones"""
# def x():
#     y()
#     print("Estoy en la funcion x")

# def y():
#     z()
#     print("Estoy en la funcion y")
    

# def z():
#     print("Estoy en la funcion z")

# x()


#Invocacion de funciones con valor de retorno de otras funciones
def suma(a, b):
    return a + b

def factorial(x):
    if (x == 1): return 1
    return x * factorial(x - 1)


# suma 4 y 6 = 10
# factorial 5 = 5 * 4 * 3 * 2 * 1
# factorial 10 = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

x, y, z = 15, 8, 3

print(suma(x, suma(x, suma(z, factorial(y)))))