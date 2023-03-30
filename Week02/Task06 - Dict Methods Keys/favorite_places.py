favorite_places = {
    'usman': ['paris', 'london', 'new york'],
    'rabe' : ['london', 'new york', 'paris'],
    'ali'  : ['japan', 'new york', 'paris']
}

for name, places in favorite_places.items():
    print(f"{name.title()} likes the following places:")
    for place in places:
        print(f"\t{place.title()}")