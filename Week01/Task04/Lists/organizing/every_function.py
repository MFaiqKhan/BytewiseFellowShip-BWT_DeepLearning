lists = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ]

# Print the list
print(lists)

# Print the list in reverse order
lists.reverse()
print(lists)

# add an item to the list
lists.append('k')
print(lists)

# remove an item from the list
lists.remove('k')
print(lists)

# remove the last item from the list
lists.pop()
print(lists)

# remove the first item from the list
lists.pop(0)
print(lists)

# use remove to remove an item from the list
lists.remove('b')
print(lists)

# sort the list
lists.sort()
print(lists)

# sorted function
print(sorted(lists))

# len function
print(len(lists))

# del function
del lists[0]
print(lists)