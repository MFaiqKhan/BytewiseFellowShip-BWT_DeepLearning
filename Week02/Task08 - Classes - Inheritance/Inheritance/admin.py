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


class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin {self.first_name} {self.last_name} has the following privileges: {', '.join(self.privileges)}")


admin = Admin("Admin", "Dude", 30, "admin@admin.com")
admin.describe_user()
admin.show_privileges()