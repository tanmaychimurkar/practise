""" Metaclasses

"""

"""
If we have many classes who have the same method defined in them, we can leverage metaclasses. For example, if we have
different class definitions but all of them still have a same method defined inside them multiple times, this could get
error prone and harder to maintain as time goes by. 

We can still avoid the repetition of the same method by a class that only has that method, and creating subclasses 
that all inherit from the same parent class, giving each of the subclass the same method whenever used. 

While it is possible to achieve what we want by subclassing and inheritance, we can also use metaclasses to solve this
problem. 
"""

""" 
Metaclasses are classes whose instances are also classes. They are defined as `solutions waiting or looking for 
problems`. 

In Python, metaclasses have the same structure as a class, except that they inherit from the `type` object. In Python,
user-defined classes are all of type `type`. There is no difference between the `classes` and `types` in Python.

Metaclass is defined as class of a class. It is of the type `type`, and takes the following arguments:
    type(classname, superclasses, attributes_dict)

If for a particular class definition, if there is no metaclass definition, then the usual type function is called as
shown above. However, if a metaclass is passed for the class, then the type is replace by the metaclass that is passed.


"""
