def car_info(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car_profile = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car_profile)