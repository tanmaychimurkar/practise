""" Avoid Dynamic Attribute Creation

"""


"""
We can create attributes dynamically as we please to instances of classes. However, we will not be able to do this for
in-built object types like int, list, etc. This is shown below
"""

class A:
    def __init__(self):
        pass

a = A()
a.x = f'This is a dynamically created attribute x'
a.y = f'This is a dynamically created attribute y'
random_number = 10
# random_number.x = f'I am an attribute for the in-built type int'

"""
As an alternative, we can define all the allowed attributes for an instance in the __slots__ variable before the 
__init__ method of a class. 
"""