pizza_list = ["Pepperoni", "Cheese", "Hawaiian", "Meat Lovers", "Veggie"]

friend_pizza_list = pizza_list[:] # copy the list

pizza_list.append("Supreme")
friend_pizza_list.append("BBQ Chicken")

print("My favorite pizzas are: ")
for pizza in pizza_list:
    print(pizza)

print("My friend's favorite pizzas are: ")
for pizza in friend_pizza_list:
    print(pizza) 
    
# output: My favorite pizzas are: Pepperoni Cheese Hawaiian Meat Lovers Veggie Supreme
# My friend's favorite pizzas are: Pepperoni Cheese Hawaiian Meat Lovers Veggie BBQ Chicken
 
 