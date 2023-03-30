# If Conditionals

cars = [ "Ford", "Volvo", "BMW" ]

for car in cars:
    if car == "Volvo":
        print(car.upper())
    else:
        print(car.lower())

# Conditional Tests

# Equality
car = "Audi" # set car to Audi
print(car == "Audi") # True
print(car == "audi") # False - case sensitive
print(car == "Audi".lower()) # True - case insensitive
print(car.lower() == "audi") # True - case insensitive


# Inequality
print(car != "Audi") # False
print(car != "audi") # True - case sensitive
if car != "Audi":
    print("Not Audi")


# Numerical Comparisons
age = 18
print(age == 18) # True

print(age < 21) # True


# Multiple Conditions
age = 18
print(age >= 18 and age < 21) # True


# using 'or'
age = 18
age2 = 21
print(age >= 18 or age2 >= 21) # True
print(age >= 18 or age2 > 22) # True
print(age > 18 or age2 > 22) # False

# checking if a value is in a list
cars = [ "Ford", "Volvo", "BMW" ]
print("Ford" in cars) # True
print("Audi" in cars) # False

# checking if a value is not in a list
cars = [ "Ford", "Volvo", "BMW" ]
print("Ford" not in cars) # False
print("Audi" not in cars) # True
