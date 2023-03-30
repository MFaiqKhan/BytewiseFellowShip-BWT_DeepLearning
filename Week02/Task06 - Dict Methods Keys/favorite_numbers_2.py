favorite_numbers = {
    'hanzu': [1, 3, 5],
    'rabe': [2, 4, 6],
    'hamza': [7, 9, 11],
    'usman': [8, 10, 12],
    'faiq': [13, 15, 17]
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"\t{number}")