import unittest
from berlin_clock import BerlinClock


class TestConvertingDigitalTimeToBerlinTime(unittest.TestCase):

    def test_should_return_correct_single_minutes_row_for_midnight(self):
        input_time = "00:00:00"
        clock = BerlinClock()
        actual_minutes = clock.convert(input_time)[-4:]
        minutes_format = "OOOO"

        self.assertEqual(actual_minutes, minutes_format)

    def test_should_return_correct_single_minutes_row_before_midnight(self):
        input_time = "23:59:59"
        clock = BerlinClock()
        actual_minutes = clock.convert(input_time)[-4:]
        minutes_format = "YYYY"

        self.assertEqual(actual_minutes, minutes_format)

    def test_should_return_correct_single_minutes_row_after_midnight(self):
        input_time = "12:32:00"
        clock = BerlinClock()
        actual_minutes = clock.convert(input_time)[-4:]
        minutes_format = "YYOO"

        self.assertEqual(actual_minutes, minutes_format)

    def test_should_return_correct_five_minutes_row_for_midnight(self):
        input_time = "00:00:00"
        clock = BerlinClock()
        actual_minutes = clock.convert(input_time)[8:19]
        minutes_format = "OOOOOOOOOOO"

        self.assertEqual(minutes_format, actual_minutes)

    def test_should_return_correct_five_minutes_row_before_midnight(self):
        input_time = "23:59:59"
        clock = BerlinClock()
        actual_minutes = clock.convert(input_time)[8:19]
        minutes_format = "YYRYYRYYRYY"

        self.assertEqual(minutes_format, actual_minutes)

    def test_should_return_correct_five_minutes_row_after_midnight(self):
        input_time = "12:35:00"
        clock = BerlinClock()
        actual_minutes = clock.convert(input_time)[8:19]
        minutes_format = "YYRYYRYOOOO"

        self.assertEqual(minutes_format, actual_minutes)

    def test_should_return_correct_single_hours_row_for_midnight(self):
        input_time = "00:00:00"
        clock = BerlinClock()
        actual_hours = clock.convert(input_time)[4:8]
        hours_format = "OOOO"

        self.assertEqual(hours_format, actual_hours)

    def test_should_return_correct_single_hours_before_midnight(self):
        input_time = "23:59:59"
        clock = BerlinClock()
        actual_hours = clock.convert(input_time)[4:8]
        hours_format = "RRRO"

        self.assertEqual(hours_format, actual_hours)

    def test_should_return_correct_single_hours_after_midnight(self):
        input_time = "14:35:00"
        clock = BerlinClock()
        actual_hours = clock.convert(input_time)[4:8]
        hours_format = "RRRR"

        self.assertEqual(hours_format, actual_hours)

    def test_should_return_correct_five_hours_for_midnight(self):
        input_time = "00:00:00"
        clock = BerlinClock()
        actual_hours = clock.convert(input_time)[:4]
        hours_format = "OOOO"

        self.assertEqual(hours_format, actual_hours)

    def test_should_return_correct_five_hours_before_midnight(self):
        input_time = "23:59:59"
        clock = BerlinClock()
        actual_hours = clock.convert(input_time)[:4]
        hours_format = "RRRR"

        self.assertEqual(hours_format, actual_hours)

    def test_should_return_correct_five_hours_after_midnight(self):
        input_time = "08:23:00"
        clock = BerlinClock()
        actual_hours = clock.convert(input_time)[:4]
        hours_format = "ROOO"

        self.assertEqual(hours_format, actual_hours)
