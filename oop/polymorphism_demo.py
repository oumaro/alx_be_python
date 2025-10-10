import math

class Shape:
    """
    Base class for all shapes, defining the common interface method 'area'.
    """
    def area(self):
        """
        The area method must be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    """
    A class representing a rectangle, derived from Shape.
    """
    def __init__(self, length, width):
        """
        Initializes the Rectangle with its length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the base method to calculate the rectangle's area.
        Formula: length * width
        """
        return self.length * self.width


class Circle(Shape):
    """
    A class representing a circle, derived from Shape.
    """
    def __init__(self, radius):
        """
        Initializes the Circle with its radius.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the base method to calculate the circle's area.
        Formula: π * radius^2
        """
        return math.pi * (self.radius ** 2)

# End of polymorphism_demo.py
