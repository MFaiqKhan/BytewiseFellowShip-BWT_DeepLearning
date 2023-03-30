 
try:
    with open("cats.txt") as file_object:
        contents = file_object.read()
        print(contents)

    with open("dogs.txt") as file_object:
        contents = file_object.read()
        print(contents)

except FileNotFoundError:
    pass