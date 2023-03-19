buffet_style = ('chicken', 'beef', 'pork', 'fish', 'vegetables')

for food in buffet_style:
    print(food)

# buffet_style[0] = 'steak' # TypeError: 'tuple' object does not support item assignment

# New menu
buffet_style = ('steak', 'ice cream', 'pork', 'fish', 'vegetables')

for food in buffet_style:
    print(food)