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

# adding arguments to functions


def hello_function(greeting):
    return '{} Function.'.format(greeting)


print(hello_function('Hi'))

# adding defaults to be added that will show up when the argument is missing. in this case, name is the default. we can add it or not as a second argument in the function


def hello_function(greeting, name='Aaron'):
    return '{}, {}'.format(greeting, name)


print(hello_function('Hi', name='Edward'))

# NOTE these methods must be in order or you will get an error

# lets go over * and ** as arguments of our functions. this allows us to accept an abritrary number of positional or keyword arguments


def student_info(*args, **kwargs):
    print(args)  # these could be classes a student is taking
    print(kwargs)   # these could be additional facts about students


student_info('Math', 'Art', faveColor='green', faveClass='psy')
# NOTE positional args printed out here as a Tuple and our kwargs are a dictionary with keyword values.

# so here we are spreading arguments in a way that allows them to be accessed as a list or as a dictionary


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ('Math', 'Art')
info = {'faveColor': 'green', 'faveClass': 'psy'}

# adding them in like this gives us the entire list and dictionary. we just want what is inside of these things
student_info(courses, info)

student_info(*courses, **info)  # this gives us our individual list and dictionary

# NOTE conditional args vs kwargs is something to review for later
