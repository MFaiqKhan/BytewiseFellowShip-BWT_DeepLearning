class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is open!")\
        

restaurant = Restaurant("The Restaurant", "Italian")
restaurant.describe_restaurant()
restarurant_2 = Restaurant("The Restaurant 2", "Italian")
restarurant_2.describe_restaurant()
restarurant_3 = Restaurant("The Restaurant 3", "Italian")
restarurant_3.describe_restaurant()