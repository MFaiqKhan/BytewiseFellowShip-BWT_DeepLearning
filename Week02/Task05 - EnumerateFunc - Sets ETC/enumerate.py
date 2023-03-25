# enumerate func is used to get the index of the element in the list


listt = ["apple", "banana", "cherry"]
print(listt)

print(enumerate(listt))

object = enumerate(listt) # convert to object
print(type(object)) # <class 'enumerate'>
print(type(enumerate(listt))) # <class 'enumerate'>

print(list(enumerate(listt))) # convert to list 

for index, value in enumerate(listt): # print index and value of the list , enumerate func is used to get the index of the element in the list
    print(index, value) 