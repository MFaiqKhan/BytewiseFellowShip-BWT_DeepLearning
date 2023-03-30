cities = {
    "Karachi" : {
        "country" : "Pakistan",
        "population" : 14916456,
        "fact" : "Karachi is the Sixth largest city in the world by city population."
    },

    "Lahore" : {
        "country" : "Pakistan",
        "population" : 12188000,
        "fact" : "Lahore is the second largest city in Pakistan."
    },

    "Islamabad" : {
        "country" : "Pakistan",
        "population" : 1095064,
        "fact" : "Islamabad is the capital city of Pakistan."
    }
}

for city, city_info in cities.items():
    print(f"{city.title()} is in {city_info['country']}.")
    print(f"\tIt has a population of about {city_info['population']}.")
    print(f"\t{city_info['fact']}")