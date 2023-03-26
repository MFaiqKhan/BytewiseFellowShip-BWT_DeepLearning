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

class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        """Initialize the privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Print a statement showing the admin's privileges."""
        print("Admin privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


class Admin(User):
    """A class to represent an admin user."""

    def __init__(self, first_name, last_name, age, email):
        """
        Initialize the admin.
        Then initialize the privileges attribute.
        """
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges([
            "can add post",
            "can delete post",
            "can ban user",
        ])


admin = Admin("Admin", "Dude", 30, "asdsadeqw@adsa.com")
admin.privileges.show_privileges()