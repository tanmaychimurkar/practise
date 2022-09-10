"""  Descriptors in Python

"""

"""
Descriptors are objects where we have set a get, set, or delete method. Usually, when we have a class object, when we 
try a retrieve a property from the class, we access the classes __dict__ lookup for that property. This is demonstrated 
in the example below.
"""


class A:
    ca_a = f"Class attribute of A"

    def __init__(self):
        self.ia_a = f"I am an instance attribute of class A"


class B(A):
    ca_b = f"Class attribute of B"

    def __init__(self):
        super().__init__()
        self.ia_b = f"I am an instance attribute of class B"


x = B()
print(x.ca_a)
print(x.ia_a)
print(x.ca_b)
print(x.ia_b)

"""
In the above example, we can see the __dict__ object that both x and type(x) contain. x.__dict__ contains all the 
instance attributes, whereas the type(x) contains all the class attributes and module information. 

If the retrieval method of attributes is the default but we override these methods with descriptor methods, then 
the one that we defined will be used to retrieve/write the attribute. 
"""

"""
The general descriptor protocol consists of get, set and delete methods. We can create a descriptor as shown below. 
"""

class MyDescriptor(object):
    def __init__(self, initval=None):
        print(f'The init method is called with initval: {initval}')
        self.__set__(self, initval)

    def __get__(self, instance, owner):
        print(f'Instance: {instance}, owner: {owner}')
        print(f'getting the self.val: {self.val}')
        return self.val

    def __set__(self, instance, value):
        print(f'Setting the value to', value)
        self.val = value

class SimpleClass(object):
    x = MyDescriptor('green')

m = SimpleClass()
print(m.x)

"""
Descriptors act as a way of applying some sort of checks or pre-processing to attributes once they are defined. This
is similar to define a property, and in-fact property uses descriptors inside it's source code.

In the above code, instance is the object on which the attribute was accessed, and the owner is the class on which the
descriptor method was defined as an attribute (as a method for example)

Only the __get__ method gets the owner, while the __set__ and the __delete__ method get the instance and the values. 
This is because descriptors are defined in the class and not the instance. Instance can be None for the get method, 
since attributes can also be accessed by the class itself.
"""

##########################################################################################
"""
Special method names: Python Documentation (https://docs.python.org/3/reference/datamodel.html#special-method-names)

This section will explore the special methods defined in Python for `operator overloading`. These are inbuilt methods,
which when defined in classes, override the normal retrieval method of classes. 

Most of the in-built methods are linked to the `object` type, so classes defining such methods should inheret from the
`object` type.

##################### Basic customization: general methods, can be applied to the instance or the attributes ##########

1) object__new__: This is called everytime a new instance is created

2) object.__init__: This is called before the instance of a class is returned. If the class is inheriting from a subclass, 
then the subclasse's __init__ method would need to be called with `super().__init__

3) object.__del__: deletes an instance of an object

4) object.__repr__: official best possible string representation of an object, used for debugging, is always used is 
__str__ is not defined

5) object.__str__: nicer string return for the object, can override __repr__ if possible

############################### Attribute access customization: Customize meaning of attribute access ###############

1) object.__getattr__: This is called only if the default attribute access method (__getattribute__) returns 
AttributeError. 

2) object.__getattribute__: This is the default method for attribute access. 

3) object.__setattr__(self, name, value): Called when attribute assignment is called. Name is name of the attribute,
and value is the value that we want to set for the attribute

4) object.__delattr__: deletes an attribute of an object

5) object.__dir__: shows the list of local variables in the scope of the current instance. 

############################################### Container magic methods ###############################################

1) __getitem__: Subscripting of an object will usually call this method. Similar to calling self[key]. 

In container types, the `in` method searches for value in the keys of the object when the container is a sequence, 
or searches for the value when the container is a list. There is a similar behaviour for iter() in sequences and lists.

2) __setitem__ and __delitem__: Similar to the __getitem__, but does their intended functionality. 





"""
