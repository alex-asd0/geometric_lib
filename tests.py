import unittest

import square, rectangle, circle, triangle

class SquareTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    
    def test_zero_side_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)
    
    def test_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

class RectangleTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
    
    def test_one_zero_side_perimeter(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)
    
    def test_two_zero_side_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)
    
    def test_perimeter(self):
        res = rectangle.perimeter(10, 20)
        self.assertEqual(res, 60)
    
    def test_negative_area(self):
        res = rectangle.area(10, -10)
        self.assertEqual(res, -100)
    
    def test_normal_area(self):
        res = rectangle.area(5, 3)
        self.assertEqual(res, 15)

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = circle.area(1)
        self.assertAlmostEqual(res, 3.14, delta=0.01)
    
    def test_perimeter(self):
        res = circle.perimeter(1)
        self.assertAlmostEqual(res, 6.28, delta=0.01)

class TriangleTestCase(unittest.TestCase):
    def test_perimeter(self):
        res = triangle.perimeter(2, 3, 4)
        self.assertEqual(res, 9)
    
    def test_area(self):
        res = triangle.area(3, 4)
        self.assertEqual(res, 6)
