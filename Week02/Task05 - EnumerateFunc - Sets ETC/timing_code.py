import timeit

# timing the list function
# List

def create_list():
    A = []

D = list(range(1,11)) # list of 1 to 10


""" 
The number argument in the timeit.timeit() method specifies the number of times to execute the given statement. 
When you don't pass any value for number, timeit runs the statement one million times by default.
On the other hand, passing a smaller number to number means that the statement will be executed fewer times. 
This can lead to a lower total execution time because it takes less time to execute the statement fewer times.
"""

print("Creating Empty list with []")

print(timeit.timeit(create_list))
print(timeit.timeit(create_list, number=10000)) # faster than the default, as default is 1 million




def create_non_empty_list():
    B= [1,2,3,4,5,6,7,8,9,10]


print("\nCreating Non Empty list with [1,2,3,4,5,6,7,8,9,10]")

print(timeit.timeit(create_non_empty_list))
print(timeit.timeit(create_non_empty_list, number=10000))


# create a list with list function

def create_list_with_list():
    C = list()


print("\nCreating Empty list with list()")

print(timeit.timeit(create_list_with_list))
print(timeit.timeit(create_list_with_list, number=10000))


# create a list with list function and range

def create_list_with_list_range():
    E = list(range(1,11))


print("\nCreating Non Empty list with list(range(1,11))")

print(timeit.timeit(create_list_with_list_range))
print(timeit.timeit(create_list_with_list_range, number=10000))


# Output: 
""" 
Creating Empty list with []
0.15768969999771798
0.001109000004362315

Creating Non Empty list with [1,2,3,4,5,6,7,8,9,10]
0.1602857000034419
0.0014580999995814636

Creating Empty list with list()
0.15696490000118501
0.0014426999987335876

Creating Non Empty list with list(range(1,11))
0.45283480000216514
0.0038727999999537133

"""