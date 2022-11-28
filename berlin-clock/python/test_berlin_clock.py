import unittest
from berlin_clock import BerlinClock


class TestConvertingDigitalTimeToBerlinTime(unittest.TestCase):

    def test_should_return_correct_single_minutes_row_for_midnight(self):
        input_time = "00:00:00"
        clock = BerlinClock()
        actual_minutes = clock.convert(input_time)
        single_minutes = "OOOO"

        self.assertEqual(actual_minutes, single_minutes)

    def test_should_return_correct_single_minutes_row_before_midnight(self):
        input_time = "23:59:59"
        clock = BerlinClock()
        actual_minutes = clock.convert(input_time)
        single_minutes = "YYYY"

        self.assertEqual(actual_minutes, single_minutes)

    def test_should_return_correct_single_minutes_row_after_midnight(self):
        input_time = "12:32:00"
        clock = BerlinClock()
        actual_minutes = clock.convert(input_time)
        single_minutes = "YYOO"

        self.assertEqual(actual_minutes, single_minutes)
