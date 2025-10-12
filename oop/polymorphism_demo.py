import math

class Shape:
    """Base class for geometric shapes, demonstrating the structure for area calculation."""
    def area(self):
        """
        Calculates the area of the shape. 
        Raises NotImplementedError to enforce overriding in derived classes.
        """
        raise NotImplementedError("Subclasses must implement the 'area()' method.")

class Rectangle(Shape):
    """Derived class for a rectangle."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Overrides the base method to calculate rectangle area."""
        return self.length * self.width

class Circle(Shape):
    """Derived class for a circle."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Overrides the base method to calculate circle area."""
        # Area formula: π * radius^2
        return math.pi * (self.radius ** 2)
