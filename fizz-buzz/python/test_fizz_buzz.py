import unittest
from fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_should_return_fizz_when_the_number_is_dividable_by_three(self):
        number = 3
        actual_result = fizz_buzz(number)
        expected_result = ["1", "2", "Fizz"]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_buzz_when_the_number_is_dividable_by_five(self):
        number = 5
        actual_result = fizz_buzz(number)
        expected_result = ["1", "2", "Fizz", "4", "Buzz"]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_fizzbuzz_when_the_number_is_dividable_by_three_and_five(self):
        number = 15
        actual_result = fizz_buzz(number)
        expected_result = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"
        ]

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
