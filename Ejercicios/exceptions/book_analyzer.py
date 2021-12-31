import sys

if (len(sys.argv)) <= 1:
    print("You should pass a file path")
    exit()


for filename in sys.argv[1:]:
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")