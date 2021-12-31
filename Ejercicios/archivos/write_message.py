
filename = "Ejercicios/archivos/programming.txt"

# with open(filename, "w") as file_object:
#     file_object.write("I love programming a lot.\n")
#     file_object.write("I really love it.\n")

with open(filename, "a") as file_object:
    file_object.write("I love programming a lot.\n")
    file_object.write("I really love it.\n")
