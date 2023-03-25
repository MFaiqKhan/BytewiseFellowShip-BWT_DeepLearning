current_cars = {"Audi", "BMW", "Mercedes", "Volkswagen", "Skoda"}
new_cars = {"Audi", "BMW", "Mercedes", "Toyota", "Honda", "Nissan"}

# # Intersection

# # The intersection() method returns a set that contains the similarity between two or more sets.
intersection = current_cars.intersection(new_cars)
print(intersection)

intersection = new_cars.intersection(current_cars) # order does not matter
print(intersection)