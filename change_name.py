# Let's use the function again, but this time say hello to Jordan.

# by importing the Hello class, we avoid having to start from scratch
from example import Hello
# this can be read as: 
# from the file 'example' import the class 'Hello'

def change_name():
    # now, instead of writing a whole new class, 
    # we only need to write a function that changes what we want to change. 
    new_hello = Hello()
    # create an instance of the class.
    new_hello.name = 'Jordan'
    # change the 'name' attribute of the class from 'Tom' to 'Jordan'
    return new_hello.say_hi()
    # we use the same method here ('say_hi'), but when we do it
    # with the new 'say_hello' class, it will say 'hello Jordan'
    # because that's what it has stored for 'name'

if __name__ == "__main__":
    change_name()
    # this executes the function

# If you type 'python change_name.py' into the terminal while in the directory 
# for this file, it will print 'hello Jordan' in the console. 