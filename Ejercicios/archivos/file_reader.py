
# leer e imprimir cada linea del archivo haciendo right-stripe a cada linea
# with open("Ejercicios/archivos/pi_digits.txt") as file_object:
#     for line in file_object:
#         print(line.rstrip())


with open("Ejercicios/archivos/pi_million_digits1.txt") as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string = pi_string + line.strip()

print(pi_string[:10002])