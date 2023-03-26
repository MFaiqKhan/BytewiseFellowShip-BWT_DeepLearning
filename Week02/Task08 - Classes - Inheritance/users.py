class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and can be contacted at {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")


user1 = User("John", "Doe", 30, "abx@abc.com")
user2 = User("Jane", "Doe", 25, "jane@abc.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()