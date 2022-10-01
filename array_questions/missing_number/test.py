# Python code to demonstrate working of unittest
# !/usr/bin/python3
import unittest
import random
import missing_number as m
import validate as v


class TestMissingNumber(unittest.TestCase):

    # check with a ten item list removing number 6.
    def testTen(self):
        self.assertEqual(m.missing_number([1, 2, 3, 4, 5, 7, 8, 9, 10]),
                         "The missing number is: 6")

    # check with a for list removing random number.
    def testRandom(self):
        for n in [100, 253, 5235, 800000, 3, 15416154]:
            miss = random.randrange(1, n)
            self.assertEqual(m.missing_number([y for y in [x for x in range(
                1, n+1)] if y != miss]), f"The missing number is: {miss}")

    # check if contains bool value inside list.
    def testBool(self):
        self.assertEqual(m.missing_number([1, 2, True, -3]),
                         "Error, there are not-int values in list")

    # check if contains string value inside list.
    def testString(self):
        self.assertEqual(m.missing_number([1, 2, ""]),
                         "Error, there are not-int values in list")

    # check if contains a list as argument inside list.
    def testInnerList(self):
        self.assertEqual(m.missing_number([1, 2, []]),
                         "Error, there are not-int values in list")

    # check if all list items are int.
    def testIsInstance(self):
        message = "Given object is not int."
        for i in [1, 3, 4, 5, 6, 7, 8, 9, 10]:
            self.assertIsInstance(i, int, message)

    # check if some list items aren't int.
    def testIsNotInstance(self):
        message = "Given object is int."
        for i in [{}, [5], "8", ""]:
            self.assertNotIsInstance(i, int, message)

    # check if all list items are int through a boolean return.
    def testallInt(self):
        message = "there are not-int values in list"
        self.assertTrue(v.validate([1, 2, 3, 5, 6, 7, 8, 9, 10]), message)

    # check if some list items aren't int through a boolean return.
    def testNotallInt(self):
        message = "All values in list are int"
        self.assertFalse(v.validate([1, 2, "3", 5, 6, 7, 8, 9, 10]), message)


if __name__ == '__main__':
    unittest.main()
