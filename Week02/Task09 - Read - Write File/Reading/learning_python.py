filename = 'learning_python.txt'

print("Reading the entire file:")

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print("Reading line by line:")

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("Reading the entire file into a list:")

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

