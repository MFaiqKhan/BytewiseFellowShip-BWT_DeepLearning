person = {
    "first_name": "Muhammad Faiq",
    "last_name": "Khan",
    "age": 21,
    "city": "Karachi"
}

person_2 = {
    "first_name": "Muhammad",
    "last_name": "Ali",
    "age": 22,
    "city": "Karachi"
}

person_3 = {
    "first_name": "Muhammad",
    "last_name": "Usman",
    "age": 23,
    "city": "Karachi"
}

people = [person, person_2, person_3]

for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")