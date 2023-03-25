glossary_2 = {
    'list': 'A list is a collection which is ordered and changeable. Allows duplicate members.',
    'tuple': 'A tuple is a collection which is ordered and unchangeable. Allows duplicate members.',
    'set': 'A set is a collection which is unordered and unindexed. No duplicate members.',
    'dictionary': 'A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.',
    'list comprehension': 'A list comprehension is a way to create a list in one line of code.',
}

for key, value in glossary_2.items():
    print(f"\n{key.title()}: {value}")


# add a new key-value pair
glossary_2['for loop'] = 'A for loop is a way to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).'
glossary_2['while loop'] = 'A while loop is used to iterate over a block of code as long as the test expression (condition) is true.'
glossary_2['if statement'] = 'An if statement is used to test for a condition and execute a block of code if the condition is true.'

for key, value in glossary_2.items():
    print(f"\n{key.title()}: {value}")