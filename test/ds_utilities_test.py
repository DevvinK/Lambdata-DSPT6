# python -m test.ds_utilities_test

# Python native
import unittest

# Third party dependencies
import pandas as pd

# My libraries and utilities
from my_lambdata.ds_utilities import enlarge, date_divider

class TestDsUtilities(unittest.TestCase):

    def test_enlarge(self):
       self.assertEqual(enlarge(3), 300)

    def test_date_divider(self):
       raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
                  'age': [20, 19, 22, 21],
                  'favorite_color': ['blue', 'red', 'yellow', "green"],
                  'grade': [88, 92, 95, 70],
                  'birth_date': ['01-02-1996', '08-05-1997', '04-28-1996', '12-16-1995']}
       df = pd.DataFrame(raw_data, index = ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])
       date_col = 'birth_date'

       current_shape = df.shape[1]
       expected_shape = current_shape + 3
       
       converted_df = date_divider(df, date_col)      

       self.assertEqual(expected_shape, converted_df.shape[1])

       
if __name__ == '__main__':
    unittest.main()


# Generally with classes:
# test = TestStringMethods()
# test.test_upper()