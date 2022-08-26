""" OOP introduction

"""

"""
Open access: User has all the freedom he wants to access and replace any entity in the functionality
Closed access: User doesn't have direct access to the element that he wants to access

OOP is closed access control. Access to the data is restricted in closed access case, and all communications has to
be done via a medium.
Putting the data behind a shell is called 'Encapsulation'

All things in python are class objects, 'first-class' motto
"""


def f():
    return 42


print(type(f))

"""In the definition of the class, we can pass another class, which is 'inheritance', as we will inherit methods 
from the passed class in our main class 

The passed classes can be called superclasses, base classes or parent classes
"""

#################################################################################
"""
properties and attributes are two different things in Python. 
"""

"""
attributes can be created on the fly for a class object as demonstrated below
"""


class Robot:
    pass


x = Robot()
x.name = "Jarvis"
print(f"Hey there, I am {x.name}")

"""
Every class instance has a dict in which it stores values
"""
print(x.__dict__)
print(Robot.__dict__)

"""
Every attribute access first checks the attribute at the instance level, if not found then checks at the class level. 
Accessing attributes that are not in either the instance dict or the class dict raise an 'AttributeError' in Python

Eg. x.energy would raise AttributeError
"""
############################################################

""" 
methods are functions defined inside the class declaration itself. Method is just a function defined inside the class.
"""


""""self" means referencing the class object itself. In our case, it would mean accessing the Robot object when it is 
instantiated 

If we instantiate a variable x for the class Robot(), then we can use a method 'say_hi' as either:

x.say_hi() or Robot().say_hi(). To use the former, we need that the "self" argument is present in the method definition, 
otherwise the instantiated variable would not be able to directly use the class method
"""


"""
The __init__ method is used to create attributes for the class as soon as it is instantiated. This way, we won't have to
manually assign individual attributes to the instantiated class variable, as they are already created via the __init__
method.

Thus the arguments in the __init__ method are the ones we want the class to have automatically when it is created, and
we can pass them in that order when we instantiate a variable from the class
"""


class RobotNew:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print(f"Hey there, my Master named me {self.name}")
        else:

            print(f"Hey there, my hasn't given me a name yet")


x1 = RobotNew()
x2 = RobotNew("Jarvis")

print(x1.say_hi(), x2.say_hi())


"""The getter and setter methods in python are not magic methods. They just mean that for the class object, 
the getter method will get the object, while the setter method will set the attribute of the class. Below is an 
example: """


class RobotAgain:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print(f"Hey there, my Master named me {self.name}")
        else:
            print(f"Hey there, my hasn't given me a name yet")

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name


x = RobotAgain("Jarvis")
x.set_name("JARVIS")
print(x.get_name())

################################################
"""the __repr__ and __str__ methods are used to almost equal, the str method should be favoured if possible. The goal 
is that str method is readable, whereas the repr method is used for internal representation of the object. More 
reading about these methods is needed to get a clearer understanding of how they work """
################################################

"""
Private attributes should only be used by the owner, inside the class definition only
Protected attributes should only be used under certain circumstances
Public attributes are freely usable

Normal named attributes are public, can be used inside or outside of a class definition. 

sunder is for protected attributes, dunder is for fully restricted attributes. Sunder attributes can still be 
updated, but is advised to do so via subclasses. Dunder attributes can't be updated from outside the class. 

Accessing dunder attributes raise an AttributeError, giving us back a lie, since such a dunder attribute already exists.
This is perfect information hiding.

Further data encapsulation means that attributes which we might have set public should only be accessible via the getter
and setter methods, much like a publicly available book is only accessible via the staff of the library!
"""


"""
Just like constructors, we have destructors as well. They are called when an instance is about to be destroyed. 

Deletion is very problematic. More in the future.
"""
