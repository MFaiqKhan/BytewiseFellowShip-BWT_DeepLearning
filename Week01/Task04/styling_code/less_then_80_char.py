# Program to create two separate lists of favorite pizzas

my_pizzas = ['pepperoni', 'mushroom', 'cheese']
friend_pizzas = my_pizzas[:]

# Adding a new pizza to my list
my_pizzas.append('sausage')

# Adding a different pizza to my friend's list
friend_pizzas.append('pineapple')

# Printing both lists
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)
