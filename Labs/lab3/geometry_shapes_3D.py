from math import pi

class Geometry_3D:

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.center = (x, y, z)
    
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
    
    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("z must be int/float")
        self._z = value

    def __repr__(self) -> str:
        return f"Geometry_3D with a central coordinates ({self.x}, {self.y}, {self.z})."


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

# error raises when x,y,z are not int/float

#####################################################################

"""Inheritance Sphere -- Geometry_3D"""

class Sphere(Geometry_3D):

    def __init__(self, x, y, z, radius) -> None:
        super().__init__(x, y, z)
        self.radius = radius
        self.center = (x, y, z)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be int/float")
        self._radius = value
        
# Methods:

    def Surface_area(self):
        return 4*pi*self.radius**2

    def Volume(self):
        return 4/3*pi*self.radius**3

    def __repr__(self) -> str:
        return f"Sphere of radius {self.radius} at a central coordinates ({self.x}, {self.y}, {self.z}) has Surface area {self.Surface_area()} and Volume {self.Volume()}."

    def __eq__(self, other) -> bool:

# We use Volume here (Surface_area will be also OK!)

        if self.Volume() == other.Volume():
            return True
        else:
            return False

    def is_inside(self, x1, y1, z1) -> float:

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
    

"""Inheritance Cube -- Geometry_3D"""

class Cube(Geometry_3D):

    def __init__(self, x, y, z, side):
        super().__init__(x, y, z)
        self.side = side
        self.center = (x, y, z)

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("side must be int/float")
        self._side = value

# Methods:

    def Surface_area(self):
        return 6*self.side1**2

    def Volume(self):
        return self.side**3

    def __eq__(self, other) -> bool:

# can also use Surface_area as a equal method

        if self.Volume() == other.Volume():
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Cube of side {self.side} at a central coordinates ({self.x}, {self.y}) has surface area {self.Surface_area()} and volume {self.Volume()}."
    
    def is_inside(self, x1, y1, z1) -> float:

        if not isinstance(x1, (int, float)):
            raise TypeError("x1 must be int/float")
        if not isinstance(y1, (int, float)):
            raise TypeError("y1 must be int/float")
        if not isinstance(z1, (int, float)):
            raise TypeError("z1 must be int/float")

        if ((self.x-self.side/2) <= x1 <= (self.x+self.side/2) 
            and (self.y-self.side/2) <= y1 <= (self.y+self.side/2) 
            and (self.z-self.side/2) <= z1 <= (self.z+self.side/2)):
            return True
        else:
            return False
