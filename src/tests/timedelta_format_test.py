import unittest
from datetime import timedelta
from services.timedelta_format import format_timedelta

class TestTimedeltaFormat(unittest.TestCase):
  def test_positive_delta(self):
    delta = timedelta(0, 8167, 580561)
    self.assertEqual(format_timedelta(delta), "02:16:07.6")

  def test_negative_delta(self):
    delta = timedelta(0, -3281.964185)
    self.assertEqual(format_timedelta(delta), "-00:54:42.0")
