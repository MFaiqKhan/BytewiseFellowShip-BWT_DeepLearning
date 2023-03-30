# The finally block is optional and is always executed, regardless of whether an exception was raised or not.
# The purpose of this block is to clean up any resources used by the program, 
#such as closing files or network connections, or releasing locks. 
#It is often used to release resources that were acquired in the try block.

try:
    f = open("demofile.txt") # Open a file that does not exist, and raise an error
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    print("The 'try except' is finished")
