magicians_names = ['harry houdini', 'david copperfield', 'david blaine']

def show_magicians(magicians):
    """Prints the names of the magicians in the list"""
    for magician in magicians:
        print(magician.title())


show_magicians(magicians_names)