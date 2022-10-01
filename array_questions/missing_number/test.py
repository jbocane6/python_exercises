# Python code to demonstrate working of unittest
# !/usr/bin/python3
import unittest
import random
import missing_number as m


class TestMissingNumber(unittest.TestCase):

    # check with a ten item list removing number 6
    def testTen(self):
        self.assertEqual(m.missing_number([1, 2, 3, 4, 5, 7, 8, 9, 10]),
                         "The missing number is: 6")

    # check with a for list removing random number
    def testRandom(self):
        for n in [100, 253, 5235, 800000]:
            miss = random.randrange(1, n)
            list = [x for x in range(1, n+1)]
            self.assertEqual(m.missing_number([y for y in list if y != miss]),
                             f"The missing number is: {miss}")

    # check if contains bool value inside list
    def testBool(self):
        self.assertEqual(m.missing_number([1, 2, True]),
                         "Error, there are not int values in list")

    # check if contains string value inside list
    def testString(self):
        self.assertEqual(m.missing_number([1, 2, ""]),
                         "Error, there are not int values in list")

    # check if contains a list as argument inside list
    def testInnerList(self):
        self.assertEqual(m.missing_number([1, 2, []]),
                         "Error, there are not int values in list")


if __name__ == '__main__':
    unittest.main()
