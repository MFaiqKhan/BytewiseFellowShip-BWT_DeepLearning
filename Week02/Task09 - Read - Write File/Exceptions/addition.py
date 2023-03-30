try:
        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
        answer = number1 + number2
        result = number1 + number2
        print("The answer is :", (result))
except ValueError:
        print("You must enter a number!")