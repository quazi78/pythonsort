import unittest
from app.sortstuff import Sortstuff

class SortTest(unittest.TestCase):


  def test_sort_returns_correct_result(self):
    sort = Sortstuff()
    result = sort.sortlist([7,5,1])
    self.assertEqual ([1,5,7], result)

  def test_sort_returns_sorted_array(self):
    sort = Sortstuff()
    result = sort.sortlist([1,2,3])
    self.assertEqual([1,2,3], result)

  def test_sort_returns_single_item_array(self):
    sort = Sortstuff()
    result = sort.sortlist([1])
    self.assertEqual([1], result)

  def test_sort_returns_empty_list(self):
    sort = Sortstuff()
    result = sort.sortlist([])
    self.assertEqual([],result)
