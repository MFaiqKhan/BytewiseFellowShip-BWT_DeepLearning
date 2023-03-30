def make_shirt(size="Large", text="I love Python"):
    print(f"Size: {size}, Text: {text}")

make_shirt() # Positional Arguments, order matters
make_shirt(size="Medium") # Keyword Arguments, order doesn't matter
make_shirt(text="I love C++") # Keyword Arguments, order doesn't matter