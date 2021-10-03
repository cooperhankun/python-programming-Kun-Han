from math import pi

class Geometry_2D:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.center = (x, y)
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be int/float")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be int/float")
        self._y = value

# Error raises when x or y is not valid.

    def __repr__(self) -> str:
        return f"Geometry_2D with a central coordinates ({self.x}, {self.y})."


    def translate(self, x_new, y_new) -> float:
        self.x = x_new
        self.y = y_new

        if not isinstance(x_new, (int, float)):
            raise TypeError("x_new must be int/float")
        if not isinstance(y_new, (int, float)):
            raise TypeError("y_new must be int/float")

# Error occurs if the new central point is not valid. 

#####################################################################

"""Inheritance Circle -- Geometry_2D"""


class Circle(Geometry_2D):

    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y)
        self.radius = radius
        self.center = (x, y)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be int/float")
        self._radius = value
# Error checking for Radius.
     
# Methods:

    def area(self):
        return pi*self.radius**2

    def circumference(self):
        return 2*pi*self.radius

    def __repr__(self) -> str:
        return f"Circle of radius {self.radius} at a central coordinates ({self.x}, {self.y}) has area {self.area()} and circumference {self.circumference()}."

    def __eq__(self, other) -> bool:

# We can also use circumference for comparison

        if self.area() == other.area():
            return True
        else:
            return False

    def is_inside(self, x1, y1) -> float:

        if not isinstance(x1, (int, float)):
            raise TypeError("x1 must be int/float")
        if not isinstance(y1, (int, float)):
            raise TypeError("y1 must be int/float")

# Error checking for x1, y1

        if (((x1-self.x)**2)+((y1-self.y)**2))**0.5 <= self.radius:
            return True
        else:
            return False

# With distance smaller or equal than radius, we return True(inside), otherwise False(outside)
    


"""Inheritance Rectangle -- Geometry_2D"""


class Rectangle(Geometry_2D):

    def __init__(self, x, y, side1, side2):
        super().__init__(x, y)
        self.side1, self.side2 = side1, side2
        self.center = (x, y)

    @property
    def side1(self):
        return self._side1

    @side1.setter
    def side1(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("side1 must be int/float")
        self._side1 = value

    @property
    def side2(self):
        return self._side2

    @side2.setter
    def side2(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("side2 must be int/float")
        self._side2 = value
# Error raise for not vaild side1, side2

# Methods:

    def area(self):
        return self.side1*self.side2

    def circumference(self):
        return 2*(self.side1 + self.side2)

    def __eq__(self, other) -> bool:
        if self.area() == other.area():
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Rectangle of sides {self.side1} and {self.side2} at a central coordinates ({self.x}, {self.y}) has area {self.area()} and circumference {self.circumference()}."
    
    def is_inside(self, x1, y1) -> float:

        if not isinstance(x1, (int, float)):
            raise TypeError("x1 must be int/float")
        if not isinstance(y1, (int, float)):
            raise TypeError("y1 must be int/float")

# Error checking for x1, y1

        if ((self.x-self.side1/2) <= x1 <= (self.x+self.side1/2) 
            and (self.y-self.side2/2) <= y1 <= (self.y+self.side2/2)):
            return True
        else:
            return False

# With the point coordinates smaller or equal to the half sides, will be within the rectangle.

    
    
