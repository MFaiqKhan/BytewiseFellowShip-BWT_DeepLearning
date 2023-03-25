number = input("Enter a number, and I'll tell you if it's a multiple of ten: ")

number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of ten.")
else:
    print(f"{number} is not a multiple of ten.")