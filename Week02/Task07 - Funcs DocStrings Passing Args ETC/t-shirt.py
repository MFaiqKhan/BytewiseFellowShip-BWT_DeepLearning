def make_shirt(size, text):
    print(f"Size: {size} Text: {text}")

make_shirt("Large", "I love Python") # Positional Arguments, order matters
make_shirt(text="I love Python", size="Large") # Keyword Arguments, order doesn't matter