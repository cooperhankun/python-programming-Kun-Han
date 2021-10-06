from math import pi



class Geometry:
    
    """
    A main class which represent the coordinates x and y.

    translate(self, x_new, y_new) is a function for the movement x and y.
    """

    def ____(self, x, y) -> None:
        self.x = x
        self.y = y
    
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
    
# Error raises when x, y is not valid.

    def translate(self, x_new, y_new) -> float:
        self.x = x_new
        self.y = y_new

        if not isinstance(x_new, (int, float)):
            raise TypeError("x_new must be int/float")
        if not isinstance(y_new, (int, float)):
            raise TypeError("y_new must be int/float")

# Error occurs if the new central point is not valid. 

#####################################################################

### Inheritance Circle -- Geometry ### 


class Circle(Geometry):
    """
    A class which represent the Circle shape in a central coordinate(x,y).
    
    radius(self, value):
    - the radius of the circle

    area(self) -> float:
    - the area of the cirlcle

    circumference(self) -> float:
    - the circumference of the circle

    __repr__(self) -> str:
    - represent the circle values

    __eq__(self, other) -> bool:
    - check if the circle is equal to another

    is_inside(self, x1, y1) -> bool:
    - check if a point inside the circle

    """
    def __init__(self, x, y, radius) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be int/float")
        if value < 0:
            raise TypeError("Radius must be a positive value.")
        self._radius = value
     
# Methods:

    def area(self) -> float:
        return pi*self.radius**2

    def circumference(self) -> float:
        return 2*pi*self.radius

    def __repr__(self) -> str:
        return f"Circle of radius {self.radius} at a central coordinates ({self.x}, {self.y}) has area {self.area()} and circumference {self.circumference()}."

    def __eq__(self, other) -> bool:

# We can also use circumference for comparison

        if self.area() == other.area():
            return True
        else:
            return False

    def is_inside(self, x1, y1) -> bool:

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
    
    def translate(self, x_new, y_new) -> float:
        super().translate(x_new, y_new)


### Inheritance Rectangle -- Geometry ###


class Rectangle(Geometry):

    """
    A class which represent the Rectangle shape in a central coordinate(x,y).
    
    side1(self):
    - the length of the Rectangle

    side2(self):
    - the height of the Rectangle

    area(self) -> float:
    - the area of the Rectangle

    circumference(self) -> float:
    - the circumference of the Rectangle

    __repr__(self) -> str:
    - represent the Rectangle values

    __eq__(self, other) -> bool:
    - check if the Rectangle is equal to another

    is_inside(self, x1, y1) -> bool:
    - check if a point inside the Rectangle

    """

    def __init__(self, x, y, side1, side2):
        super().__init__()
        self.x = x
        self.y = y
        self.side1 = side1
        self.side2 = side2
        
    @property
    def side1(self):
        return self._side1

    @side1.setter
    def side1(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("side1 must be int/float")
        if value < 0:
            raise TypeError("Side1 must be a positive value.")
        self._side1 = value

    @property
    def side2(self):
        return self._side2

    @side2.setter
    def side2(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("side2 must be int/float")
        if value < 0:
            raise TypeError("Side2 must be a positive value.")
        self._side2 = value

# Methods:

    def area(self) -> float:
        return self.side1*self.side2

    def circumference(self) -> float:
        return 2*(self.side1 + self.side2)

    def __eq__(self, other) -> bool:
        if self.area() == other.area():
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Rectangle of sides {self.side1} and {self.side2} at a central coordinates ({self.x}, {self.y}) has area {self.area()} and circumference {self.circumference()}."
    
    def is_inside(self, x1, y1) -> bool:

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
    def translate(self, x_new, y_new) -> float:
        super().translate(x_new, y_new)

##############################################################################################  

### Inheritance Sphere -- Circle ###

class Sphere(Circle):

    """
    A class which represent the Sphere 3D-shape in a central coordinate(x,y,z).
    
    radius(self, value):
    - the radius of the Sphere

    Surface_area(self) -> float:
    - the surface area of the Sphere

    Volume(self) -> float:
    - the Volume of the Sphere

    __repr__(self) -> str:
    - represent the Sphere values

    __eq__(self, other) -> bool:
    - check if the Sphere is equal to another

    is_inside(self, x1, y1, z1) -> bool:
    - check if a point inside the Sphere

    translate(self, x_new, y_new, z_new) -> float:
    - A function for the movement x, y and z

    """

    def __init__(self, x, y, z, radius) -> None:
        super().__init__(x, y, radius)
        self.z = z

    
    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("z must be int/float")
        self._z = value
    
        
# Methods:

    def Surface_area(self) -> float:
        return 4*pi*self.radius**2

    def Volume(self) -> float:
        return 4/3*pi*self.radius**3

    def __repr__(self) -> str:
        return f"Sphere of radius {self.radius} at a central coordinates ({self.x}, {self.y}, {self.z}) has Surface area {self.Surface_area()} and Volume {self.Volume()}."

    def __eq__(self, other) -> bool:

# We use Volume here (Surface_area will be also OK!)

        if self.Volume() == other.Volume():
            return True
        else:
            return False

    def is_inside(self, x1, y1, z1) -> bool:

        if not isinstance(x1, (int, float)):
            raise TypeError("x1 must be int/float")
        if not isinstance(y1, (int, float)):
            raise TypeError("y1 must be int/float")
        if not isinstance(z1, (int, float)):
            raise TypeError("z1 must be int/float")

        if (((x1-self.x)**2)+((y1-self.y)**2)+((z1-self.z)**2))**0.5 <= self.radius:
            return True
        else:
            return False

    def translate(self, x_new, y_new, z_new) -> float:
        self.x = x_new
        self.y = y_new
        self.z = z_new

        if not isinstance(x_new, (int, float)):
            raise TypeError("x_new must be int/float")
        if not isinstance(y_new, (int, float)):
            raise TypeError("y_new must be int/float")
        if not isinstance(z_new, (int, float)):
            raise TypeError("z_new must be int/float")

### Inheritance Cube -- Rectangle ###

class Cube(Rectangle):
 
    """
    A class which represent the Cube 3D-shape in a central coordinate(x,y,z).
    
    side1(self):
    - one side of the Cube

    side2(self):
    - one side of the Cube
    Note here: side1 = side2 = side

    Surface_area(self) -> float:
    - the surface area of the Cube

    Volume(self) -> float:
    - the Volume of the Cube

    __repr__(self) -> str:
    - represent the Cube values

    __eq__(self, other) -> bool:
    - check if the Cube is equal to another

    is_inside(self, x1, y1, z1) -> bool:
    - check if a point inside the Cube

    translate(self, x_new, y_new, z_new) -> float:
    - A function for the movement x, y and z

    """

    def __init__(self, x, y, z, side1, side2):
        super().__init__(x, y, side1, side2)
        self.z = z

# side1 = side2! Because the Cube is a child-class of Rectangle, we can not remove the side1, side2

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("z must be int/float")
        self._z = value

# Methods:

    def Surface_area(self) -> float:
        return 6*self.side1*self.side2

    def Volume(self) -> float:
        return self.side1**3

    def __eq__(self, other) -> bool:

# can also use Surface_area as a equal method

        if self.Volume() == other.Volume():
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Cube of side {self.side1} at a central coordinates ({self.x}, {self.y}) has surface area {self.Surface_area()} and volume {self.Volume()}."
    
    def is_inside(self, x1, y1, z1) -> bool:

        if not isinstance(x1, (int, float)):
            raise TypeError("x1 must be int/float")
        if not isinstance(y1, (int, float)):
            raise TypeError("y1 must be int/float")
        if not isinstance(z1, (int, float)):
            raise TypeError("z1 must be int/float")

        if ((self.x-self.side1/2) <= x1 <= (self.x+self.side1/2) 
            and (self.y-self.side1/2) <= y1 <= (self.y+self.side1/2) 
            and (self.z-self.side1/2) <= z1 <= (self.z+self.side1/2)):
            return True
        else:
            return False

    def translate(self, x_new, y_new, z_new) -> float:
        self.x = x_new
        self.y = y_new
        self.z = z_new

        if not isinstance(x_new, (int, float)):
            raise TypeError("x_new must be int/float")
        if not isinstance(y_new, (int, float)):
            raise TypeError("y_new must be int/float")
        if not isinstance(z_new, (int, float)):
            raise TypeError("z_new must be int/float")