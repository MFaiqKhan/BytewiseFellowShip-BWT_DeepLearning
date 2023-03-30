current_cars = {"Audi", "BMW", "Mercedes", "Volkswagen", "Skoda"}
new_cars = {"Audi", "BMW", "Mercedes", "Toyota", "Honda", "Nissan"}

# # Union

# # The union() method returns a set that contains all items from the original set, and all items from the specified sets.
union = current_cars.union(new_cars)
print(union)