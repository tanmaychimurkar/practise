""" Class vs Instance Attributes

"""

"""
Class attributes are attributes that are common across all the instances created from a class. They are variables 
above the init function. 
"""

"""
If we want to count the total number of instances created from a class object, we can maintain a counter to keep track
of how many instances are being created via the __init__ method, and decrement the counter by the __del__ method. 
"""


class Robot:
    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1


"""
However, we can also make the counter variable as a private variable by changing the name with dunder-name and a access 
method. However, the access method should not depend on defining an instance and then using the access method. The 
access method itself should be callable independently of whether an instance is defined or not when calling it. 

############ Static method ############
The solution to this is to create the method itself as a static method, so that even if new instances are created, the 
latest changes can be fetched from the class independently via this static method. 

############ Class method ############
Class methods are bound to a class. The first argument class methods take is a reference to the class. They can be 
called via the instance or the class name. Class methods are often used when one static method has to call other static
methods
"""


class RobotNew:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def __del__(self):
        type(self).__counter -= 1

    @classmethod
    def Robotinstances(cls):
        return cls, RobotNew.__counter


"""
######################## class methods vs static methods vs instance methods ##############################
All references are made to the MyMethod example below.

Instance methods: Methods we use most of the time in our classes. The first parameter, self, that they use indicate that
the method points to the 'instance' of the class created, and also has access to all the attributes that are created in
that instance. Instance methods have access to the object instance 'and' the class as well 

Class methods: These methods only have access to the 'class' itself and not the 'instance'. Since there is no reference
to the instance that is created, these methods cannot modify the instance that is created from the class definition. 
But, class methods can modify the class state, which applies to all the instances that are created.

Static methods: Normal functions that are inside the namespace of the class definition. They cannot modify either the 
class state or the instance state.  
"""


class MyClass:
    def instance_method(self):
        print(f"This is a instance method, bound as {type(self), self}")
        return f"This is a instance method, bound as {type(self), self}"

    @classmethod
    def class_method(cls):
        print(f"This is a class method, bound as {type(cls), cls}")

    @staticmethod
    def static_method():
        print(f"This is a static method, bound to nothing")


obj = MyClass()
# obj.instance_method()
# obj.class_method()
# obj.static_method()

"""
Class methods are good for inheritance from another class. Below examples highlight the usage of classmethods when there
is inheritance from once class into another.
"""


class Pet:
    _class_info = "pet animals"

    def about(self):
        print(f"This is a class about {self._class_info}")


class Cat(Pet):
    _class_info = "cats"


class Dog(Pet):
    _class_info = "dogs"


c = Cat()
c.about()
d = Dog()
d.about()

"""
the above implementation, while correct, is not tidy, since we first need to create an instance and then use the about 
method to be able to get the class info output correctly. This can be changed by instead creating about as a classmethod
as it will be bound to the class itself.
"""


class PetClass:
    _class_info = "pet animals"

    @classmethod
    def about(cls):
        print(f"This is a class about {cls._class_info}")


class Cat(PetClass):
    _class_info = "cats"


class Dog(PetClass):
    _class_info = "dogs"


Cat.about()
Dog.about()
a = Cat()
a.about()
