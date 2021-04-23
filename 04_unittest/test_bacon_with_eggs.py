"""
TDD - Test Driven Development

Red
Part 01 -> Create test and see the test fails

Green
Part 02 -> Create the code and see the test fails

Refactor
Part 03 -> Improve the code
"""

import unittest
from bacon_with_eggs import bacon_with_eggs

class TestBaconWithEggs(unittest.TestCase):
    def test_bacon_with_eggs_should_raises_assertion_error_if_not_receive_int(self):
        """
        1 -> Receive an integer number
        """
        with self.assertRaises(AssertionError):
            bacon_with_eggs('')

    def test_bacon_with_eggs_should_return_bacon_with_eggs_if_n_is_multiple_of_3_and_5(self):
        """
        2 -> know if the humber is multiple of 3 and 5:
            Bacon and eggs
        """
        entries = (15, 30, 45, 60)
        output = "Bacon with eggs"

        for entry in entries:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(
                    bacon_with_eggs(entry), 
                    output,
                    msg=f"{entry} not returns {output}"
                )

    def test_bacon_with_eggs_should_return_bacon_if_n_is_multiple_of_3(self):
        """
        3 -> Know if the number is multiple of 3:
            Bacon
        """
        entries = (3, 6, 9, 12, 18, 21)
        output = "Bacon"

        for entry in entries:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(
                    bacon_with_eggs(entry), 
                    output,
                    msg=f"{entry} not returns {output}"
                )

    def test_bacon_with_eggs_should_return_eggs_if_n_is_multiple_of_5(self):
        """
        4 -> Know if the number is multiple of 5:
            Eggs
        """
        entries = (5, 10, 20, 25, 35, 40)
        output = "Eggs"

        for entry in entries:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(
                    bacon_with_eggs(entry), 
                    output,
                    msg=f"{entry} not returns {output}"
                )

    def test_bacon_with_eggs_should_return_pass_hungry_if_n_is_not_multiple_of_3_and_5(self):
        """
        5 -> Know if the number is not multiple of 3 and 5:
            Pass Hungry
        """
        entries = (1, 2, 4, 7, 8)
        output = "Pass hungry"

        for entry in entries:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(
                    bacon_with_eggs(entry), 
                    output,
                    msg=f"{entry} not returns {output}"
                )

unittest.main(verbosity=2)
