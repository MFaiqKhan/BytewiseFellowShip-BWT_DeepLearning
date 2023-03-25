rex = {
    'animal': 'dog',
    'owner': 'Ali',
}

catija = {
    'animal': 'cat',
    'owner': 'Faiq',
}

pets = [rex, catija]

for pet in pets:
    print(pet['owner'].title())
    print(pet['animal'].title(),'\n')