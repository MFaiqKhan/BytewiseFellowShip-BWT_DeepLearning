def items_on_sandwich(*items): # *items is a tuple
    """Print the list of items that have been requested on a sandwich."""
    print("You have ordered a sandwich with the following items:")
    for item in items:
        print("- " + item)


items_on_sandwich('cheese')
items_on_sandwich('cheese', 'bacon')
items_on_sandwich('cheese', 'bacon', 'lettuce', 'tomato')