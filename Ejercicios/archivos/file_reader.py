
# leer e imprimir cada linea del archivo haciendo right-stripe a cada linea
# with open("Ejercicios/archivos/pi_digits.txt") as file_object:
#     for line in file_object:
#         print(line.rstrip())

filename = "Ejercicios/archivos/pi_million_digits1.txt"
executed = False

while not executed:
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()

        pi_string = ""
        for line in lines:
            pi_string = pi_string + line.strip()

        #print(pi_string[:10002])

        birthday = input("Ingresa tu fecha de cumpleaños en el formato ddmmaa: ")

        if birthday in pi_string:
            print(f"Tu fecha de cumpleaños {birthday}, se encuentra en el primer millón de digitos de PI")
        else:
            print(f"Tu fecha de cumpleaños {birthday}, no se encuentra en el primer millón de digitos de PI")
        executed = True
    except FileNotFoundError:
        executed = False
        print(f"El archivo {filename} no existe")
        filename = input("Ingresa la ruta de un archivo valido: ")

