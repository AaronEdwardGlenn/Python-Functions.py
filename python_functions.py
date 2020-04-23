# functions defined with the 'def' keyword
def hello_func():
    # pass allows us to define a function without yet using it. This is just to avoid errors.
    pass


print(hello_func)

# this is showing us how to get a function working


def hello_func():
    print('Hello Function')

# an example of chaining a method onto a functions


def hello_function():
    return 'Hello New Function.'


print(hello_function().upper())

# adding perameters to functions


def hello_function(greeting):
    return '{} Function.'.format(greeting)


print(hello_function())
