"""Programa que recibe como input un parrafo de texto y al final va a mostrarnos cuantas veces
se repite cada letar en ese texto"""

"""
    input = "anita lava la tina"

    La letra 'a' aparecio 6 veces 
    La letra 'n' aparecio 2 veces 
    ...

"""

paragraph = """Two earlier campaigning organisations founded in 1885, the Selborne League and the Plumage League, had amalgamated in the following year as the Selborne Society,[16] but were soon outstripped by the SPB because of the latter organisation's extensive network of local branches[17] and its single-issue focus"""


# ocurences = {}

# for character in paragraph:
#     if character in ocurences:
#         ocurences[character] += 1
#     else:
#         #ocurences[character] = 1
#         ocurences.update({character: 1})


# for k in ocurences:
#     print(f"El caracter '{k}' aparece {ocurences[k]} veces")


# dic.items() -> retorna una lista de tuplas
# [('T', 1), ('w', 4)...]
# for key, value in ocurences.items():
#     print(f"El caracter '{key}' aparece {value} veces")

# for im_a_tuple in ocurences.items():
#     print(f"El caracter '{im_a_tuple[0]}' aparece {im_a_tuple[1]} veces")


# Destructuring tuples
# t = (1, 2, 3)
# x, y, z = t



#dict.setdefault(character[i], []).append(character) 

ocurences = {}


# 1 - La key si existe -> retorna el valor actual
# 2 - La key no existe -> inserta un nuevo elemento con la llave y el valor indicados

for character in paragraph:
    counter = ocurences.setdefault(character, 0)
    ocurences[character] = counter + 1

for key, value in ocurences.items():
    print(f"El caracter '{key}' aparece {value} veces")



