""" Getter vs Setter and Properties

"""

"""
Getter methods are to access private attributes, while setter methods are to set the values of the private variables. 

In Python, we introduce new attributes to a class as public attributes, not private attributes. 
"""

"""
To make sure data once assigned cannot be changed, we can use properties. For eg., if x is always supposed to be 
between 0 and 1000, without property and a public attribute, this is hard to achieve. 

Properties in Python work like an attribute having a certain property, e.g., attribute can take values only between
0 and 1000, can only have length <= 5, etc. Below is an example of a property.
"""


class PythonProperty:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            self._x = 0
        elif value > 1000:
            self._x = 1000
        else:
            self._x = value


p = PythonProperty(121)
p.x = 1000
print(p.x)

"""
Because of the nature of properties, in Python, it is not good to have a property for every attribute that we have in 
the class. We can create a new property based on the values of individual attributes as shown in the example below
"""


class MyRobotStatus:
    def __init__(self, robot_health=0.5, robot_oil=0.5):
        self.__rh = robot_health
        self.__ro = robot_oil

    @property
    def condition(self):
        overall_condition = self.__ro + self.__rh

        if overall_condition < 0:
            return f"I am going to die soon, need oil"
        else:
            return f"I am alive with pleasure now"


robot = MyRobotStatus()
robot.condition

#######################################################################################
"""
Property function instead of a decorator. We can also use property directly as a function instead of a decorator, with 
the following 4 functionalities for the function: get method, set method, delete method, and a docstring.

The signature of property function is as follows:
    property(fget=None, fset=None, fdel=None, doc=None)
    
fget, fset, fdel are function attributes, i.e., they are functions names without the parenthesis.

"""

"""
Property as a decorator

Decorator is a function that takes another function as an argument and returns a function with added functionality. 

@property decorator works by giving a attribute getter and setter methods, and they could be called by the instances
just like instance methods, but without a parenthesis, as the @property decorator would internally call the getter,
setter or deleter functions for us. 
"""

"""
attributes which have a property can't be changed once assigned if there is no setter for the property created, and 
trying to change them raises an AttributeError. This can we used to create 'read-only' attributes from your class. 
Below is an example.
"""


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


p = Point(12, 5)
print(p.x)
# p.x = 13  # this would raise AttributeError as no setter method set for property x and y

"""
Instead of AttributeError, we can also return a custom exception if an attribute is to be kept read only. This can be
done as follows.
"""


class CoordinateException(Exception):
    """
    Creating a custom exception
    """

    pass


class PointException:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        raise CoordinateException(f"x-coordinate is read-only")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        raise CoordinateException(f"y-coordinate is read-only")


point = PointException(12, 4)
# print(point.x)
# print(point.y)

"""
Property can be used as a common Data validation check whenever we are taking a user input. For the above example, we
could set data validation checks that verifies if x and y are integers or not. The implementation for that is as follows
"""


class PointVerified:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)

        except ValueError:
            raise ValueError(f"x should be an integer or float")


p1 = PointVerified(12, 4)
p2 = PointVerified("a", 5)
