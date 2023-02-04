def classifytriangle(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0) or ((a >= b + c) or (b >= a + c) or (c >= a + b)):
        return "is not a triangle"
    if a == b == c:
        return "should be a equilateral triangle"
    if a == b or a == c or b == c:
            return "should be a isosceles triangle"
    if (a ^ 2 + b ^ 2 == c ^ 2) or (b ^ 2 + c ^ 2 == a ^ 2) or (a ^ 2 + c ^ 2 == b ^ 2):
        return "should be a right triangle"
    elif (a != b) and (b != c) and (a != c):
             return "should be a scalene triangle"
print (classifytriangle(2,3,4))

import unittest

class testclassifytriangle(unittest.TestCase):
    def testSet1(self):   #valid input
        self.assertEqual(classifytriangle(3, 4, 5), "should be a right triangle")
        self.assertEqual(classifytriangle(1, 1, 1), "should be a equilateral triangle")
        self.assertEqual(classifytriangle(7, 1, 7), "should be a isosceles triangle")
        self.assertEqual(classifytriangle(2, 3, 4), "should be a scalene triangle")


    def testmySet2(self):    #invalid input
        self.assertEqual(classifytriangle(0, 1, 3), "is not a triangle")
        self.assertEqual(classifytriangle(-1, -2, 3), "is not a triangle")
        self.assertEqual(classifytriangle(1, 2, 4), "is not a triangle")
        self.assertEqual(classifytriangle(0, 0, 1), "is not a triangle")
        self.assertEqual(classifytriangle(-1, -2, -3), "is not a triangle")

if __name__ == '__main__':
    unittest.main()\





