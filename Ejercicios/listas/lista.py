"""Lista con algunos presidentes de Mexico"""
presidentes = ["Andres Manuel", "Enrique Pena", "Felipe Calderon", "Vicente Fox"]


"""Utilizamos for para iterar sobre la lista de presidentes e imprimimos un mensaje para cada
uno de ellos.
NOTA: en Python el bloque de codigo que pertenece al for esta indentado"""
for presidente in presidentes:
    print(f"Hola {presidente}, cuanto dinero te robaste?")
    print("Devuelve el dinero... no seas ratero!!!")

# --- Rangos ---

"""Trabajando con rangos, Nos permiten crear secuncia de numeros enteros, desde un numero
de inicio hasta uno de fin.
NOTA1: El numero de inicio es inclusivo y el de fin es exclusivo, por tanto el siguiente ejemplo
genera un rango desde 0(inclusivo) hasta 14(Exclusivo).

NOTA2: El orden de ejecucion de esta linea es:
    1 - Genera el rango y devuelve un objeto de tipo rango
    2 - Ese objeto se convierte en una lista usando 'list'
    3 - Se imprime la lista con los numeros desde el 0 hastael 14
"""
print(list(range(0, 15)))


"""Podemos utilizar for para iterar sobre los elementos del rango, entonces el siguiente codigo
imprime los valores del rango (una linea para cada valor) desde el 0 hasta el 4"""
for valor in range(0, 5):
    print(valor)


"""Podemos usar rangos para acceder a los elementos de una lista de forma indexada. Podemos crear
un rango que vaya desde 0 hasta el numero de elementos de la lista.

Si solo pasamos un valor a range se asume que este valor es el valor de fin y el valor de inicio 
se considera que es 0. Es por esto que el siguiente for itera desde 0 (implicitamente) hasta la
longitud de la lista de presidentes, como la longitud de la lista es 4 entonces este rango va
desde 0 hasta 3. Entonces con estos indices podemos acceder a cada elemento de la lista en
el cuerpo del for."""
for indice in range(len(presidentes)):
    print(presidentes[indice])


"""range tambien pude recibir un tercer parametro que le indica el incremento a la secuencia
asi en el siguiente ejemplo se genera un rango que va desde 0 hasta 19 pero con incrementos de 2"""
for valor in range(0, 20, 2):
    print(valor)


"""Generando una lista del cuadrado de los numeros del 1 al 10
1 - Creamos una lista vacia donde guardamos los resultados
2 - Iteramos sobre un rago que va desde 1 hasta 10
3 - Por cada valor del rango, calculamos su cuadrado (value ** 2)
4 - Guardamos el valor calculado al final de la lista de resultados
5 - Imprimimos las lista
"""
cuadrados = []
for value in range(1, 11):
    cuadrado = value ** 2
    cuadrados.append(cuadrado)
print(cuadrados)


# --- Funcions utiles para listas (Muy usadase en analisis de datos y estadistica) ---

"""Creamos una lista con enteros del 0 hasta el 9 (los digitos)"""
digitos = list(range(10))

"""Para obtener el mayor de los elementos de la lista"""
print(max(digitos))
"""Para obtener el menor de los elementos de la lista"""
print(min(digitos))
"""Para sumar todos los elementos de la lista"""
print(sum(digitos))
"""Con la suma podemos obtener el promedio (AVG) simplemente dividiendo entre la longitud de la lista"""
print(sum(digitos) / len(digitos))

# --- Listas de comprension (comprehension list)

"""COPIADO DE LA LINEA 51: Codigo para generar la lista de cuadrados de un rago version 1"""
cuadrados = []
for value in range(1, 11):
    cuadrado = value ** 2
    cuadrados.append(cuadrado)
print(cuadrados)

"""Codigo para generar la lista de cuadrados de un rago version 2 usando listas de comprension.
Syntaxis:
    [ <operacion o expresion por cada elemento de la lista o rango> for <variable> in <lista o rango> ]"""
cuadrados = [value ** 2 for value in range(1, 11)]
print(cuadrados)


# --- iterando con while ---

"""De la semana pasa, un ejercicio pedia eliminar elementos de una lista hasta quedarnos 
solamente con 2 (invitados). esto lo podiamos hacer de forma manual haciendo pop n - 2 veces.
Esto es impractivo y en la vida real no podemos asumir cuantos elementos tendra una lista."""

"""Nuestra lista de invitados"""
invitados = ["Luis", "Jose", "Adriana", "Fernanda", "Juan", "Maria"]


"""Iteramos mientras el tamanio de nuestra lista sea mayor a 2, una vez que la lista tenga solo 2 
elementos, el ciclo se detiene y continua con la ejecucion de la siguiente linea. En el cuerpo de la 
funcion hacemos pop del ultimo elemento y mostramos el mensaje que diga que ya no es invitado.
NOTA: Aqui empezamos a usar el depurador (debuger) de python, si tienen dudas pregunten."""
while len(invitados) > 2:
    invitado = invitados.pop()
    print(f"{invitado} tu ya no estas invitado")

"""Imprimir la lista con los unicos 2 elementos restantes"""
print(invitados)

# --- Slicing ---
"""Es una operacion que nos permite obtener sub-listas de una lista, el operador que nos permite
usar esta funcionalidad es el operador ':' dentro de los corchetes en una lista. Los valores que 
se indican en esta operacion funcionan exactamente igual que los parametros que usabamos en range.
Tenemos el valor de inicio (inclusivo), el valor de fin(exclusivo) y el incremento"""

"""De la lista de presidentes, creamos una sublista (y la guardamos en 'ultimos_presidentes' desde
el primer elemento de la lista original hasta el 2 (recordemos que el valor de fin es exclusido y por 
tanto devuelve el elemento 0 y el 1)."""
ultimos_presidentes = presidentes[0:2]
print(ultimos_presidentes)

"""Podemos omitir el valor de inicio y se asume que este valor es 0 (o el primer elemento de la lista)"""
ultimos_presidentes = presidentes[:2]
print(ultimos_presidentes)

"""Podemos omitir el valor de fin y se asume que este valor es len(list) o el ultimo de la lista"""
ultimos_presidentes = presidentes[2:]
print(ultimos_presidentes)

"""Tambien podemos usar indices negativos"""
ultimos_presidentes = presidentes[-1:]
print(ultimos_presidentes)

ultimos_presidentes = presidentes[-2:]
print(ultimos_presidentes)


"""Como podemos imprimir unicamente los expresidentes usando slicing? evitar imprimr al presidente actual"""
for presidente in presidentes[1:]:
    print(f"{presidente}, tu ya no eres presidente jaja")
