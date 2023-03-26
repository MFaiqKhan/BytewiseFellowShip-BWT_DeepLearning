# Dry means Don't Repeat Yourself
# It is a principle of software development aimed at reducing repetition of software patterns,
# replacing it with abstractions or using data normalization to avoid redundancy.

# The DRY principle is stated as "Every piece of knowledge must have a single, unambiguous, 
# authoritative representation within a system."

# Example of DRY code

def add(a, b):
    return a + b

# The above function is DRY because it is only one line of code and it is not repeated anywhere else in the program.

# Opposite of DRY code

print(1 + 2)
print(3 + 4)
print(5 + 6)

# The above code is not DRY because it is repeated three times.

# DRY code is easier to maintain and less error-prone.


# Example using loops instead of printing the same thing over and over again

for i in range(1, 10):
    print(i) # This is the same thing as print(1), print(2), print(3), etc.

# The above code is DRY because it is not repeated.



