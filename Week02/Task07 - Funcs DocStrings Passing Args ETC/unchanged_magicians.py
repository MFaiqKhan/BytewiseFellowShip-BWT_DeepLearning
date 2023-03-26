magicians_names = ['harry houdini', 'david copperfield', 'david blaine']

def show_magicians(magicians):
    """Prints the names of the magicians in the list"""
    for magician in magicians:
        print(f'{magician.title()}')

def make_great(magicians):
    """Adds the word 'the Great' to each magician's name"""
    for i in range(len(magicians)):
        magicians[i] = f'the Great {magicians[i].title()}'
    return magicians.copy()

show_magicians(magicians_names)

great_magicians = make_great(magicians_names[:])
show_magicians(great_magicians)