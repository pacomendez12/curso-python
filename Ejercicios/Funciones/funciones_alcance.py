
def genera_lista():
    participantes = ['Juan', 'Luis', "Maria"]

    print(participantes)

    return participantes

def genera_diccionario():
    diccionario = { "nombre" : 'Juan', "apellido": "perez" }
    return diccionario


part = genera_lista()

part[0] = "Mario"

print(genera_lista())

part = genera_lista


def ejecute_generator(x: function):
    return x()


print(ejecute_generator(genera_lista))
print(ejecute_generator(genera_diccionario))