buffet_style = ('chicken', 'beef', 'pork')
for food in buffet_style:
    print(food)
# buffet_style[0] = 'steak' # TypeError: 
# 'tuple' object does not support item 
# assignment
# New menu
buffet_style = ('steak', 'ice cream', 'pork')
for food in buffet_style:
    print(food)