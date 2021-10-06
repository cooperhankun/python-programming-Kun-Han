from geometry_shapes import Geometry
from geometry_shapes import Circle
from geometry_shapes import Rectangle
from geometry_shapes import Sphere
from geometry_shapes import Cube
from math import pi
import unittest

##### Tests for parents class: Geometry #####

class TestGeometry(unittest.TestCase):

    def setUp(self) -> None:
        self.x, self.y = 1,1

    def test_geometry(self) -> None:
        shape = Geometry(1,1)
        self.assertEqual((shape.x, shape.y),(self.x, self.y))

    def test_translate(self):
        shape = Geometry(1,1)
        shape.translate(-2,3)
        self.assertEqual((shape.x, shape.y), (-2,3))

    def test_validation(self):
        with self.assertRaises(TypeError):
            Geometry(1, "two")

##### Tests for Cirlcle #####

class TestCircle(unittest.TestCase):

    def setUp(self) -> None:
        self.x, self.y, self.radius = 1,1,1

    def test_circle(self) -> None:
        shape = Circle(1,1,1)
        self.assertEqual((shape.x, shape.y, shape.radius),(self.x, self.y, self.radius))
    
    def test_validation_y_Cirlcle(self):
        with self.assertRaises(TypeError):
            Circle(2,"two", 2)
    
    def test_validation_r_Cirlcle(self):
        with self.assertRaises(TypeError):
            Circle(2,1, "Three")

    def test_validation_neg_Cirlcle(self):
        with self.assertRaises(TypeError):
            Circle(2,1, -3)
    
    def test_area_Cirlcle(self):
        shape = Circle(1,1,1)
        area = shape.area()
        self.assertEqual(area, pi*self.radius**2)
    
    def test_circumference_Cirlcle(self):
        shape = Circle(2,2,2)
        circumference = shape.circumference()
        self.assertEqual(circumference, pi*4)

    def test__eq__Cirlcle(self):
        circle1 = Circle(1,3,2)
        circle2 = Circle(4,5,2)
        self.assertEqual(circle1,circle2)

    def test_is_inside_Cirlcle(self):
        shape = Circle(2,2,1)
        point = shape.is_inside(8,9)
        self.assertFalse(point)
    

##### Tests for Rectangle #####

class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.x, self.y, self.side1, self.side2 = 0,0,1,2

    def test_rectangle(self) -> None:
        shape = Rectangle(0,0,1,2)
        self.assertEqual((shape.x, shape.y, shape.side1, shape.side2),(self.x, self.y, self.side1, self.side2))
    
    def test_validation_x_Rectangle(self):
        with self.assertRaises(TypeError):
            Rectangle("two",2,2,1)
    
    def test_validation_side2(self):
        with self.assertRaises(TypeError):
            Rectangle(2,1, 2,"Three")

    def test_validation_neg_Rectangle(self):
        with self.assertRaises(TypeError):
            Rectangle(2,1, 2, -3)
    
    def test_area_Rectangle(self):
        shape = Rectangle(1,0,1,2)
        area = shape.area()
        self.assertEqual(area, 2)
    
    def test_circumference_Rectangle(self):
        shape = Rectangle(2,2,2,1)
        circumference = shape.circumference()
        self.assertEqual(circumference, 6)

    def test__eq__Rectangle(self):
        Rectangle1 = Rectangle(1,3,2,3)
        Rectangle2 = Rectangle(4,5,2,5)
        self.assertNotEqual(Rectangle1,Rectangle2)

    def test_is_inside_Rectangle(self):
        shape = Rectangle(0,0,2,2)
        point = shape.is_inside(1,1)
        self.assertTrue(point)


##### Tests for Sphere #####

class TestSphere(unittest.TestCase):

    def setUp(self) -> None:
        self.x, self.y, self.z, self.radius = 0,0,0,1

    def test_Sphere(self) -> None:
        shape = Sphere(0,0,0,1)
        self.assertEqual((shape.x, shape.y, shape.z, shape.radius),(self.x, self.y, self.z, self.radius))
    
    def test_validation_z_Sphere(self):
        with self.assertRaises(TypeError):
            Sphere(2,1,"two", 2)
    
    def test_validation_r_Sphere(self):
        with self.assertRaises(TypeError):
            Sphere(2,1,1, "Three")

    def test_validation_neg_r_Sphere(self):
        with self.assertRaises(TypeError):
            Sphere(2,1,2, -3)
    
    def test_Surface_area_Sphere(self):
        shape = Sphere(1,1,1,1)
        area = shape.Surface_area()
        self.assertEqual(area, 4*pi)
    
    def test_Volume_Sphere(self):
        shape = Sphere(2,2,2,2)
        Volume = shape.Volume()
        self.assertEqual(Volume, pi*32/3)

    def test__eq__Sphere(self):
        Sphere1 = Sphere(1,1,0,2)
        Sphere2 = Sphere(0,1,3,2)
        self.assertEqual(Sphere1,Sphere2)

    def test_is_inside_Sphere(self):
        shape = Sphere(2,2,1,3)
        point = shape.is_inside(1,1,1)
        self.assertTrue(point)

    def test_translate_sphere(self):
        shape = Sphere(1,1,1,4)
        shape.translate(2,3,4)
        self.assertEqual((shape.x, shape.y, shape.z,shape.radius), (2,3,4,4))
    
    def test_translate_sphere_valid(self):
        with self.assertRaises(TypeError):
            Sphere.translate(2,3,"four")

##### Tests for Cube #####

class TestCube(unittest.TestCase):

    def setUp(self) -> None:
        self.x, self.y, self.z, self.side = 0,0,0,1

    def test_Cube(self) -> None:
        shape = Cube(0,0,0,1)
        self.assertEqual((shape.x, shape.y, shape.z, shape.side),(self.x, self.y, self.z, self.side))
    
    def test_validation_y_Cube(self):
        with self.assertRaises(TypeError):
            Cube(2,"t1",1, 2)
    
    def test_validation_side_Cube(self):
        with self.assertRaises(TypeError):
            Cube(2,1,1, "Three")

    def test_validation_neg_side_Cube(self):
        with self.assertRaises(TypeError):
            Cube(2,1,1, -3)
    
    def test_Surface_area_Cube(self):
        shape = Cube(1,1,1,1)
        area = shape.Surface_area()
        self.assertEqual(area, 6)
    
    def test_Volume_Cube(self):
        shape = Cube(2,2,2,2)
        Volume = shape.Volume()
        self.assertEqual(Volume, 8)

    def test__eq__Cube(self):
        Cube1 = Cube(1,1,0,2)
        Cube2 = Cube(0,1,3,3)
        self.assertNotEqual(Cube1,Cube2)

    def test_is_inside_Cube(self):
        shape = Cube(2,2,1,3)
        point = shape.is_inside(5,6,7)
        self.assertFalse(point)

    def test_translate_cube(self):
        shape = Cube(1,1,1,4)
        shape.translate(2,3,4)
        self.assertEqual((shape.x, shape.y, shape.z, shape.side), (2,3,4,4))



if __name__ == "__main__":
    unittest.main()