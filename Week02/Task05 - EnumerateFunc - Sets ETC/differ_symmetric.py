current_cars = {"Audi", "BMW", "Mercedes", "Volkswagen", "Skoda"}
new_cars = {"Audi", "BMW", "Mercedes", "Toyota", "Honda", "Nissan"}

# Difference also called aSymmetric Difference 

# nothing from new_cars
# The difference() method returns a set that contains the difference between two sets.
difference = current_cars.difference(new_cars) # current_cars - new_cars = difference , order does matter
print(difference) # {'Volkswagen', 'Skoda'}, nothing in new_cars that is not in current_cars

# nothing from current_cars
difference = new_cars.difference(current_cars) # new_cars - current_cars = difference , order does matter
print(difference) # {'Honda', 'Toyota', 'Nissan'} , nothing in current_cars that is not in new_cars

# Symmetric Difference, from a and b, but not from both
symmetric_difference = current_cars.symmetric_difference(new_cars) # current_cars ^ new_cars = symmetric_difference , order does not matter
print(symmetric_difference) # {'Honda', 'Toyota', 'Nissan', 'Volkswagen', 'Skoda'}, nothing in current_cars that is not in new_cars and vice versa