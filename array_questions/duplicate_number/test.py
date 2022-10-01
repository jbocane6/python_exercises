# Python code to demonstrate working of unittest
# !/usr/bin/python3
import unittest
import duplicateNumber as d
import validateIntList as v


class TestMissingNumber(unittest.TestCase):

    # check when there aren't numbers duplicated.
    def testNoDuplicate(self):
        self.assertEqual(d.duplicateNumber([1, 2, 3, 6, 4, 5, 7, 8, 9, 10]),
                         "There aren't duplicate numbers")
        self.assertEqual(d.duplicateNumber([25, 58, 91, 99, 94]),
                         "There aren't duplicate numbers")
        self.assertEqual(d.duplicateNumber(
            [3, 27, 58, 75, 53, 98, 81, 60, 24, 70, 18, 38, 91, 42, 94, 36, 78]
        ), "There aren't duplicate numbers")

    # check when there is only one number duplicated.
    def testOneDuplicate(self):
        self.assertEqual(d.duplicateNumber([1, 2, 3, 8, 4, 5, 7, 8, 9, 10]),
                         "There is a duplicate number: 8")
        self.assertEqual(d.duplicateNumber([89, 60, 24, 35, 32, 60, 18]),
                         "There is a duplicate number: 60")
        self.assertEqual(d.duplicateNumber([7, 13, 51, 14, 46, 56, 50, 58, 79,
                                            4, 51, 26, 65, 74, 70, 97, 85, 12,
                                            91, 10]),
                         "There is a duplicate number: 51")

    # check when there are many numbers duplicated.
    def testManyDuplicate(self):
        self.assertEqual(d.duplicateNumber([1, 2, 3, 3, 8, 4, 5, 7, 8, 9, 10]),
                         "There are duplicate numbers: [8, 3]")
        self.assertEqual(d.duplicateNumber([99, 61, 16, 14, 22, 58, 37, 87, 3,
                                            67, 31, 68, 62, 10, 79, 88, 30, 58,
                                            67, 17, 86, 68, 60, 50, 17, 82, 27,
                                            76, 72, 74, 21, 58, 57, 7, 23, 92,
                                            94, 90, 10, 86, 7, 44, 48, 83, 33,
                                            14, 86, 6, 56, 40, 61, 52, 18, 41,
                                            27, 43, 48, 60, 65, 48, 86, 38, 94,
                                            72, 85, 61, 94, 63, 17, 34, 8, 50,
                                            12, 12, 95, 34, 1, 36, 20, 88, 96,
                                            94, 92, 19, 22, 59, 61, 17, 15, 85,
                                            41, 29, 65, 34]),
                         "There are duplicate numbers: [7, 10, 12, 14, 17, 22,"
                         " 27, 34, 41, 48, 50, 58, 60, 61, 65, 67, 68, 72, 85,"
                         " 86, 88, 92, 94]")
        self.assertEqual(d.duplicateNumber([42, 4, 32, 22, 81, 30, 86, 48, 73,
                                            33, 95, 64, 62, 88, 84, 47, 50, 94,
                                            72, 8, 52, 60, 85, 74, 97, 66, 65,
                                            36, 61, 39, 26, 91, 69, 80, 5, 18,
                                            9, 65, 17, 88, 79, 80, 25, 8, 47,
                                            63, 76, 52, 80, 63, 43, 60, 4, 60,
                                            33, 82, 87, 90, 81, 42, 12, 70, 40,
                                            16, 57, 47, 35, 28, 68, 35, 65, 10,
                                            36, 64, 52, 69, 9, 71, 69, 79, 92,
                                            94, 63, 74]),
                         "There are duplicate numbers: [4, 8, 9, 33, 35, 36,"
                         " 42, 47, 52, 60, 63, 64, 65, 69, 74, 79, 80, 81, 88,"
                         " 94]")
        self.assertEqual(d.duplicateNumber([21, 46, 3, 49, 64, 55, 76, 41, 26,
                                            21, 53, 1, 7, 55, 30, 18, 18, 60,
                                            61, 50, 84, 59, 21, 24, 73, 13, 4,
                                            3, 16, 46, 38, 31, 4, 66, 50, 1,
                                            48, 18, 24, 27, 36, 63, 48, 14, 37,
                                            47, 66, 66, 30, 36, 11, 98, 94,
                                            98]),
                         "There are duplicate numbers: [1, 66, 3, 4, 36, 98,"
                         " 46, 48, 18, 50, 21, 55, 24, 30]")

    # check if contains a bool value inside list.
    def testBool(self):
        self.assertEqual(d.duplicateNumber([1, 2, True, -3]),
                         "Error, there are not-int values in list")

    # check if contains string value inside list.
    def testString(self):
        self.assertEqual(d.duplicateNumber([1, 2, ""]),
                         "Error, there are not-int values in list")

    # check if contains a list as argument inside list.
    def testInnerList(self):
        self.assertEqual(d.duplicateNumber([1, 2, []]),
                         "Error, there are not-int values in list")

    # check if all list items are int.
    def testIsInstance(self):
        message = "Given object is not int."
        for i in [1, 3, 95, 7, 8, 9, 10, 122, 9]:
            self.assertIsInstance(i, int, message)

    # check if some list items aren't int.
    def testIsNotInstance(self):
        message = "Given object is int."
        for i in [{}, [5], "8", ""]:
            self.assertNotIsInstance(i, int, message)

    # check if all list items are int through a boolean return.
    def testallInt(self):
        message = "there are not-int values in list"
        self.assertTrue(v.validate([1, 3, 95, 7, 8, 9, 10, 122, 9]), message)

    # check if some list items aren't int through a boolean return.
    def testNotallInt(self):
        message = "All values in list are int"
        self.assertFalse(v.validate(
            [1, 3, 95, 7, 8, 9, "Hello", 122, 9]), message)


if __name__ == '__main__':
    unittest.main()
