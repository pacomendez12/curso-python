def dame_un_juego_al_azar():
    return "Ir por la pelota"



class Perro:
    """Una clase basica que representa a un perro"""

    def __init__(self, nombre, edad, raza):
        """Inicializando el nombre y la edad del perro"""
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.color = None
        self.orejas = None
        self.numero_de_juegos_restantes = 3

    def ladrar(self):
        print(f"Hola soy {self.nombre} y digo guaaauu")

    def jugar(self):
        if self.numero_de_juegos_restantes > 0:
            juego = dame_un_juego_al_azar()
            print(f"Hola soy un perro de la raza {self.raza} y por tanto cuado juego me divierto y ahora estoy jugando {juego}")
            self.numero_de_juegos_restantes = self.numero_de_juegos_restantes - 1
            #self.numero_de_juegos_restantes -= 1
        else:
            print(f"{self.nombre} tu ya no puedes jugar")

    def saludar_a_otro_perro(self, otro_perro):
        print(f"Hola soy {self.nombre} y estoy saludando a mi amigo {otro_perro.nombre}")
        print(f"Hola soy {self.nombre} y estoy saludando a mi amigo que tiene {otro_perro.edad} anios")

    def dame_nombre(self):
        return self.nombre
    
    def escribe_nombre(self, nombre):
        if nombre != None:
            self.nombre = nombre
    
    def dame_edad(self):
        return self.edad

    


# Crear una instancia
mi_primer_perro = Perro("Perry", 2, "Snausher")
mi_segundo_perro = Perro("Polo", 3, "Golder")

#print(mi_primer_perro.orejas)


mi_primer_perro.ladrar()

mi_primer_perro.escribe_nombre("Firulais")
mi_primer_perro.escribe_nombre(None)

mi_primer_perro.ladrar()

for i in range(5):
    mi_primer_perro.jugar()

print(mi_segundo_perro.numero_de_juegos_restantes)

#mi_primer_perro.saludar_a_otro_perro(mi_segundo_perro)

