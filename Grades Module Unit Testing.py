import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):

    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")


    def test_total_returns_0(self): # tests that it will return a zero when list with no items are passed

        result = Grades.total([])
        self.assertEqual(result, 0)

    def test_average_one(self): # test the average will return 5.33333

        result = Grades.average([2, 5, 9])
        comparison = 5.33333
        decimal_places = 5
        self.assertAlmostEqual(result, comparison, decimal_places)

    def test_average_two(self): #checks for 4 decimals close to 12.0000

        result = Grades.average([2, 15, 22, 9])
        comparison = 12.0000
        decimal_places = 4
        self.assertAlmostEqual(result, comparison, decimal_places)

    def test_average_returns_nan(self): #tests that the average returns math.nan when the average is passed a list with no items in it.

        result = Grades.average([])
        self.assertIs(result, math.nan)

    def test_median_one(self):

        result = Grades.median([2, 5, 1])
        self.assertEqual(result, 2)

    def test_median_two(self):

        result = Grades.median([5, 2, 1, 3])
        self.assertEqual(result, 2.5)

    def test_median_returns_ValueError(self):
        
        with self.assertRaises(ValueError):
            result = Grades.median([])

if __name__=='__main__':
    unittest.main()

    
