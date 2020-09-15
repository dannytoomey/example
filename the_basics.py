# Here are a few basics of python to get your bearings
# ------------------------------------------------------
# Let's start with some variables:
a = 1               # this is an integer variable
b = 'hello'         # this is a string variable
c = 5.6             # this is a floating decimal variable

# depending on the type of variable you're using, 
# there are different things you can do with them.
# For instance, we can do:
test = a+c          # test = 6.6
# but we can't do
test = a+b          # returns an error

# one nice thing about python if that you can put variables 
# of different types into arrays together. So,
array = [a,b,c] 
# returns an array that reads [1,'hello',5.6]    

# this array can be indexed with
array[0]            # note that python starts on 0 instead of 1
array[1]
array[2]
# and these indexed values can be changed.
# For instance, writing
array[0] = 2
# changes the array to [2,'hello',5.6] and writing
array[0] = array[0] + 1
# changes the array to [3,'hello',5.6]

# There are lots of other ways to interact with variables in python, 
# but this should be enough to get started. 
# ------------------------------------------------------
# Next, let's do some logic and loop statements.
# First, a few variables to work with:
a = 0
b = 1
c = 2
array = [a,b,c]
# if statements in python are written like this:
# if <some varialbe> == <some value>:
#    do something
# so a single statement would look like:
if a == 0:
    print(True)     # this returns True and prints it to the console
# 'and' statements can be nested like this:
if a == 0 and b == 1:
    print(True)
# multiple statements can be nested like this:
if a == 0 and b == 1 or a == 0 and c == 2:      # read as: if (a == 0 and b == 1) or (a == 0 and c == 2)
    print(True)
# if and else statements can be nested like this:
if a == 1:
    print(True)
else:                   # will only execute if all preceding if statements are false
    print(False)

# next, for statements.
# for statements are written like this:
# for <variable indexing the list> in <list>:
#    do something
for value in array:
    print(value)        
# what's happening here is that the variable 'value' 
# is being assigned as each value in the array sequentially 

# one useful way to use a for loop is to create an empty array,
# do something with the values in the loop, and store the values
# in the new array. For example
new_array = []          # empty array
for value in array:
    new_array.append(array[value]+1)
    # this might look a little complicated, let's break it down:
    # new_array.append(x) = this is a 'method', which means that it's an action
    # that this particular piece of code can take. this method appends 
    # a new value  'x' to 'new_array'
    # array[value]+1 = this calls whatever is in 'array' at position 'value' 
    # and adds 1 to it. this is the 'x' in new_array.append(x)
    print(new_array)    # returns [1,2,3]

# you can nest if statements in for loops like this:
for value in array:
    if value > 0:
        print(value)    # returns 1,2

# if statements and for loops are your bread and butter!
# ------------------------------------------------------
# Now you need a way to use your variables, if statements, 
# and for loops with one another. That's where functions come in. 

# functions are written like this:
# def <name of funciton> (<something the function needs to work>):
#   do something

# so let's write a function that takes a given range of values
# and stores them in an array
def make_array(range_of_values):
    # here, 'range_of_values' is something you have to specify. it has to be an array of numbers. 
    # this text can be whatever you want, you're essentially declaring a variable
    # to be used by the function.
    new_array = []      # this is an empty array that will be created whenever the function is called
    for value in range_of_values:
        new_array.append(value)     # this works the same way as the for loop exmaple above
    return new_array    # this tells python to return this value outside of the function

new_array = make_array([1,2,3,4])   # returns [1,2,3,4]
# new_array can now be used as an array variable

# technically, this kind of a useless function because 
# the input and output values are the same.
# let's make it more useful by returning a multidimensional array
# multiplying the row value by the column value

def make_multidim_array(range_of_values):
    new_array = []      # this is only a one dimensional array, but we're going to fix that
    for row in range(len(range_of_values)):
        # here, range() and len() are methods that come with python
        # len() returns the length of an array passed to it
        # range() returns an array starting at zero and ending at the value specified (minus one because python starts at zero)
        # so, for a 4 entry array, range(len(x)) would return [0,1,2,3]
        new_array.append([])
        # here, i'm being a little tricky. i'm appending a new empty row, which makes the array multidimensional
        for column in range(len(range_of_values)):
            new_array[row].append(range_of_values[row]*range_of_values[column])     
            # here, i'm multiplying the row and column values in the array and appending it to new_array
    return new_array    # return the array 

new_array = make_multidim_array([1,3,6,9])
# this returns [[1, 3, 6, 9], [3, 9, 18, 27], [6, 18, 36, 54], [9, 27, 54, 81]]
# that's not very pretty to read, so let's make another function!

def print_array_nicely(array):   
    # this is going to print each row on a new line
    for row in range(len(array[:][0])): 
        # this is using some fancy indexing.
        # array[a][b] = value in array at row 'a' and column 'b'
        # array[:][b] = all row values in column 'b'
        # array[:][0] = all row values in column 1 (remember, 0 is the first position in python indexing)
        # len(array[:][0]) = the number of row values
        # range(len(array[:][0])) = array going from zero to the number of rows in the array (minus 1)
        print(array[row][:])    # print all the column values in the row

print_array_nicely(new_array)
# this returns 
# [1, 3, 6, 9]
# [3, 9, 18, 27]
# [6, 18, 36, 54]
# [9, 27, 54, 81]
# which is much nicer to read
# ------------------------------------------------------
# That's it for the basics! There's a lot I didn't cover, 
# but this should be enough to get started. 

# Now move on to say_hello.py to see how to make a class. 