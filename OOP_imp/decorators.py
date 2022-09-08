""" Decorators in Python

"""

"""
Decorators are useful when calling higher-order functions, which take one or more functional arguments, i.e., they take
another function as an input. Decorators are functions that take another function and extends their behaviour without
modifying the input function. 
"""

"""
In Python, functions can be passed around as arguments, instead of callables. This is Functional programming, more 
about this in later tutorials. 

For now, we can check how a function can be passed as an argument to another function. The below example demonstrates 
that.
"""


def say_hello(name):
    return f"Hey there {name}"


def greet_me(name):
    return f"Greetings there {name}"


def call_another_function(func):
    return func("Harry potter")


hello_func = call_another_function(say_hello)
gree_func = call_another_function(greet_me)

"""
This is how we can pass one function as an argument to another function. Notice how say_hello and greet_me are without
paranthesis, i.e., they are not called when passed to the `call_another_function` function.

We can also define a function inside another function. This is demonstrated below. 
"""


def outer_function():
    def inner_function1():
        print(f"I am inner function 1")

    def inner_function2():
        print(f"I am inner function 2")

    inner_function2()
    inner_function1()


outer_function()

"""
The order of the inner functions does not matter. However, just like arguments, they cannot be accessed outside the 
parent function. 

We can also create functions that return functions as return arguments. Below is an example of such a function
"""


def parent(number):
    def first_child():
        return f"Hi I am child1"

    def second_child():
        return f"Hi I am child2"

    if number == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)

"""
The first and the second variables in the above example shows that if we print either one, we see that they are locals
reference to the parent function. Printing them only gives us back a reference, even though it's type is a function. 
Only after they are invoked do we get to see what their return values are, in this case the print functions. 
"""

"""
Decorators in Python: We can see an example decorator below. It calls a function inside another function, just like the
above case. 
"""


def custom_decorator(func):
    def wrapper():
        print(f"I just entered the wrapper")
        func()
        print(f"The function is invoked and the wrapper will return")

    return wrapper


"""
just like the case of first_child or second_child example above, we return the wrapper function, this only acts as a 
reference, while the real function say_whee will invoke it once called.
"""


def say_whee():
    print("whee!")


my_variable = custom_decorator(say_whee)
my_variable()

"""
decorators wrap a function, modifying it's behaviour. Calling say_whee will only print what is inside it, calling it
as a functional argument for custom_decorator will create a locals map, which will only be invoked once the variable 
that stores it invokes it. 

Instead of calling a decorator as a function with a functional argument, it can be called with the `@` symbol. Using 
this symbol above the function declaration does the same thing as shown in line 111. However, it can't be assigned to
a new variable now, we just invoke say_wheel_again() and it will go inside the custom_decorator. 
"""


@custom_decorator
def say_wheel_again():
    print("whee!")


object = (
    say_wheel_again()
)  # this will not work if we are decorating our function using `@` symbol. Instead invoke it!
say_wheel_again()

"""
We can put decorators as functions in separate files and import them as modules. Let's not look at that here.

Let's instead create one more decorator below.
"""


def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
        print(f"This is the end")

    return wrapper_do_twice


@do_twice
def greet_me_again(name):
    return f"Hello {name}"


# greet_me_again("Bob")

# this gives an error, since the wrapper_do_twice takes no arguments, but we want it to use name. We could let it
# take name as an argument, but then the say_whee decorator would break since there is no name required there.

"""
The solution is to use *args and **kwargs as arguments, as they allow for variable number of arguments to be passed to
a function when we do not know what we need to pass beforehand. (check *args and **kwargs file in the project)

Thus, the above implementation can be changed with the wrapper as follows
"""


def do_twice_with_args(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        print(f"This is the end")

    return wrapper_do_twice


@do_twice_with_args
def greet_me_again_with_args(name):
    print(f"Hello {name}")


greet_me_again_with_args("Bob")
print("done")

"""
So far we have invoked only prints from decorator functions. How can we use returns from decorated functions?

We could try adding a return in the function itself to check if that works
"""


@do_twice_with_args
def greet_with_return(name):
    print(f"Hello {name}")
    return f"returned {name}"


object1 = greet_with_return("Bob")
print(
    object1
)  # this is going to be None, since the wrapper inside the decorator has no return value. We need to


# change the decorator to return values and store them in vars


def do_twice_with_args_return(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        print(f"This is the end")
        return func(*args, *kwargs)

    return wrapper_do_twice


@do_twice_with_args_return
def say_my_name(name):
    print(f"Hello {name}")
    return f"returned {name}"


object_definition = say_my_name("Bob")
print(object_definition)

"""
It seems like decorator act an an intermediate function to apply some steps on the function it is called on and then
pass it along the normal flow of the function once the preprocessing has been done. More needed to verify this.
"""

help(say_my_name)

"""
Seeking help on teh say_my_name function will tell us that it is a function that is a reference to the wrapper_do_twice
function inside the do_twice_with_args_return function. We can change the response of the help function, so that it is
more useful, by using functools.wraps from Python. 

Let's see how this modifies the function definition
"""

import functools


def functools_wrapped_decorator(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        print(f"This is the end")
        return func(*args, *kwargs)

    return wrapper_do_twice


@functools_wrapped_decorator
def say_my_name(name):
    print(f"Hello {name}")
    return f"returned {name}"


object_definition = say_my_name("Bob")
print(object_definition)
help(say_my_name)

#########################################################################################

"""
Let's look at some useful decorators that we can use. 

The basic boilerplate code for setting up decorators is below
"""

import functools


def custom_decorator(func):
    @functools.wraps(func)
    def wrapper():
        value = func()
        return value

    return wrapper


"""
Let's create a wrapper that computes the time it takes to run a function call
"""

import time


def time_decorator(func):
    @functools.wraps(func)
    def timer_func(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f"Time taken for function {func.__name__} is {end_time:.4f}")
        return value

    return timer_func


@time_decorator
def random_useless_function(upper_range):
    for i in range(upper_range):
        sum([i**2 for i in range(upper_range)])


small_call = random_useless_function(10)
# large_call = random_useless_function(
#     10000
# )  # maybe don't run this if you get the gist, or reduce the number of calls made to func1

"""
We can also just register functions using decorators if we do not want to wrap a function. We can do this as follows.
"""

import random

FUNCTIONS_REGISTERED = dict()


def register(func):
    if func not in FUNCTIONS_REGISTERED.keys():
        FUNCTIONS_REGISTERED[func.__name__] = func
        return func


@register
def say_hello(name):
    return f"Hey there {name}"


print(FUNCTIONS_REGISTERED)


@register
def greet_me(name):
    return f"Hey there, {name}!!!!!!"


"""
Using the above structure, we can keep track of the registered functions as their reference in the FUNCTIONS_REGISTERED
dictionary. This is the same that the `globals()` functions keeps as a local scope of all the functions that are defined
"""
