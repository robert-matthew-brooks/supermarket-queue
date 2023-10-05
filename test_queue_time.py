import unittest
from unittest import mock
from queue_time import queue_time

class TestQueueTime(unittest.TestCase):
  @mock.patch('queue_time.report')
  def test_returns_a_number(self, mocked):
    self.assertEqual(type(queue_time([1], 1)), int)
    self.assertEqual(type(queue_time([2, 2, 2], 1)), int)
  
  @mock.patch('queue_time.report')
  def test_returns_longest_time_for_no_queue(self, mocked):
    self.assertEqual(queue_time([2, 10], 2), 10)
    self.assertEqual(queue_time([4, 3], 2), 4)
    self.assertEqual(queue_time([1, 7, 4], 3), 7)

  @mock.patch('queue_time.report')
  def test_returns_sum_of_times_for_one_checkout(self, mocked):
    self.assertEqual(queue_time([2], 1), 2)
    self.assertEqual(queue_time([2, 2], 1), 4)
    self.assertEqual(queue_time([2, 2, 2], 1), 6)
    self.assertEqual(queue_time([10, 10, 10, 10, 10], 1), 50)
  
  @mock.patch('queue_time.report')
  def test_tills_become_free_at_same_time(self, mocked):
    self.assertEqual(queue_time([2, 2, 3, 3, 4], 2), 9)
    self.assertEqual(queue_time([1, 1, 2, 3, 4], 3), 5)
  
  @mock.patch('queue_time.report')
  def test_multiple_tills_multiple_customers(self, mocked):
    self.assertEqual(queue_time([2, 3, 10], 2), 12)
    self.assertEqual(queue_time([1, 2, 3, 4, 5, 6, 7, 8], 2), 20)
    self.assertEqual(queue_time([1, 2, 3, 4, 5, 6, 7, 8], 3), 15)
    self.assertEqual(queue_time([1, 2, 3, 4, 5, 6, 7, 8], 4), 12)
  
  @mock.patch('queue_time.report')
  def test_more_tills_than_customers(self, mocked):
    self.assertEqual(queue_time([3], 5), 3)
  
  @mock.patch('queue_time.report')
  def test_purity(self, mocked):
    customers = [1, 2, 3, 4, 5, 6, 7, 8]
    customers_clone = [1, 2, 3, 4, 5, 6, 7, 8]

    queue_time(customers, 2)

    self.assertEqual(customers, customers_clone)

if __name__ == '__main__':
  unittest.main()