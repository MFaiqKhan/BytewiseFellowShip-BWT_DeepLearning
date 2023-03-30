# Sets in Python :

# Sets are unordered collections of unique elements. We can construct them by using the set() function.
# Sets are iterable. We can loop over the elements in a set using a for loop.
# Set are unindexed. We cannot access elements in a set using indexing or slicing.
# Sets are Unchangeable. We cannot change the elements in a set, but we can add or remove elements.
# Sets are UnOrdered. We cannot change the order of elements in a set.

# Creating a set

car_set = { "BMW", "Audi", "Mercedes", "Toyota", "Honda", "Nissan" }
print(car_set)
print(type(car_set))

# Accessing elements in a set
# We cannot access elements in a set using indexing or slicing.

for car in car_set:
    print(car)

