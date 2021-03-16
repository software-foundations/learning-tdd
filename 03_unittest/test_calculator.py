import unittest
from calculator import sum


class TestCalculator(unittest.TestCase):
	def test_sum_5_and_5_should_return_10(self):
		self.assertEqual(sum(5, 5), 10)

	def test_sum_5_negative_and_5_should_return_0(self):
		self.assertEqual(sum(-5, 5), 0)

	def test_sum_many_entries(self):
		x_y_outputs = (
			(10, 10, 20),
			(1.5, 3.5, 5),
			(-6, 10, 4),
			(-5, 5, 0),
			(-9, -6, -15),
			# (-9, -6, -90) # Error
		)

		for x_y_output in x_y_outputs:
			with self.subTest(x_y_output=x_y_output):
				x, y, output = x_y_output
				self.assertEqual(sum(x, y), output)

	def test_sum_x_not_int_or_float_should_return_assertionerror(self):
		with self.assertRaises(AssertionError):
			sum('a', 11)

	def test_sum_y_not_int_or_float_should_return_assertionerror(self):
		with self.assertRaises(AssertionError):
			sum(11, 'a')

unittest.main(verbosity=2)
