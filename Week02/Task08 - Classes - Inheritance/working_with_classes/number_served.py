class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # Add an attribute called number_served with a default value of 0.

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


Restaurant1 = Restaurant("Restaurant1", "Italian")
print(Restaurant1.number_served)

Restaurant1.set_number_served(10)
print(Restaurant1.number_served)

Restaurant1.increment_number_served(5)
print(Restaurant1.number_served)
