from ast import Str
import unittest
from classtest import testClass


class Tests(unittest.TestCase):

    def testClasType(self):
        cTest = testClass("First Test Object")
        if type(cTest.myClassName) != str:
            raise TypeError("Name must be of type string")

    def testEquals(self):
        cTest = testClass("First Test Object")
        self.assertEquals("First Test Object", cTest.myClassName, "Class name did not match") 

    def testClass(self):
        cTest = testClass("First Test Object")
        self.assertIsInstance(cTest, testClass, "class must be of type testCLass")


if __name__ == '__main__':
    unittest.main()
