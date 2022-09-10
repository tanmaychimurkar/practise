""" Magic Methods

"""

"""
There are many magic methods defined in Python, and they are dunder methods. Let's first look at the __call__ magic 
method. 

We all remember the dreaded `int() object is not callable` or `dict() object is not callable` errors. Let us now 
jump into investigating why and how these error arise.

When we invoke a function, we also call the `__call__` method of that function. In Python, every function is a callable.
We also have a method by the name `callable` in Python, which checks if a particular object is callable or not. 

The __call__ method is used to turn an object which can be used like a function but is not a function. We can create
classes, whose instances can be used as callables and thus will print whatever we define in the class's __call__ 
function. 

The usage of __call__ method would be explained in more detail in other parts and will be briefed there.
"""

