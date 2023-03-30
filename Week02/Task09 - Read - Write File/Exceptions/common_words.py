
filename = 'guternberg.txt'

with open(filename) as file_object:
    lines = file_object.read()
    print(lines.count('the'))

