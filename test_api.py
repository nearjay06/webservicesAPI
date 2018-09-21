import unittest
from api import NewsSources
import requests

class TestNewsSource(unittest.TestCase):
    
    def setUp(self):
        self.newSources = NewsSources()
        # self.NewsSources = get_headlines()

    def test_get_headlines(self):
        returnedValue = self.newSources.get_headlines()
        self.assertEqual(returnedValue[0], 200)

    #  def test_add_two_numbers(self):
    #     returnedValue =  self.newSources.addnumbers(4, 5)
    #     self.assertEqual(returnedValue, 9)   
   
    
   
if __name__ == "__main__":
        unittest.main()

# import unittest
# from api import and_numbers

# class AndNumbers(unittest.TestCase):
#         def setUp(self):
#                 self.result = and_numbers(-6)
#         def test_and_numbers(self):
#                 self.assertEqual(self.result, 6)