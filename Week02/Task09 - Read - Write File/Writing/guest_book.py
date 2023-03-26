filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
    while True:
        name = input("What is your name? (q to quit) ")
        if name == 'q':
            break
        else:
            file_object.write("Greetings, " + name + "!")
            file_object.write(" You are now in the guest book. \n")


