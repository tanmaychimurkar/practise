""" Builder design

This design pattern is useful when we have certain configuration for creating a large object.
"""

"""
We can create object in multiple steps via the builder design instead of creating multiple subclasses or by creating a
very large class definition. 

We also use the builder pattern when we want the class to different object representations of the same product. For eg.
a wooden house and a modern house could be built via builder class.

This class mostly creates a smaller abstract class, who the subclasses inherit to create the complex objects they want
to create
"""