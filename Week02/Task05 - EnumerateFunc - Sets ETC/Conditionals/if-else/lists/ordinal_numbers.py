numbers = list(range(1, 10)) # Create a list of numbers from 1 to 9

# Print the ordinal version of each number
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

