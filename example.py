# This class uses a 'name' attribute and returns 'Hello <name>' with the 'say_hi()' method
class Hello():
    # 'classes' are pieces of code that has attributes (properties they posess) 
    # and methods (things they can do)
    def __init__(self):
        # initialize the class and give it a name to say hi to
        self.name = 'Tom'
        # 'self' means that the class is referring to itself here. 
        # if you only put 'name = 'Tom'' the script what not know 
        # what the 'name' attribute is in reference to. 

    def say_hi(self):
        # this is a method. here the anatomy of the method declaration: 
        # 'def' = define a function
        # 'say_hi' = the name the function
        # '(self)' = the inheritance of the function. inheritence is how you pass 
        # qualities between different peieces of code. so, here, 'self' means 
        # that the 'say_hi' function needs the qualities of its class ('Hello')
        # in order to work properly. 
        return print(f'hello {self.name}')
        # this is what the method does. here's the breakdown of what's going on:
        # 'print' = print to the console (the terminal)
        # 'f' = this tells python that i'm formatting the string 
        # with a variable i'm going to call in the string 
        # 'hello' = this is a string that will be printed
        # '{self.name}' = this is the attribute we defined above ('Tom')
        # it's formatted in such a way that python knows I'd like it 
        # to be printed as a string


if __name__ == '__main__':
    # this is a convention in python used to execute scripts.
    # put anything here that you want to run.
    hello = Hello()
    # this creates an instance of the class Hello. 
    # Hello() is shorthand for Hello.init(), which creates the class
    hello.say_hi()
    # this says hello to Tom. 

# If you type 'python example.py' into the terminal while in the directory 
# for this file, it will print 'hello Tom' in the console. 