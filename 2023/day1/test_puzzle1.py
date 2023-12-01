from unittest import TestCase

from parameterized import parameterized

from puzzle1 import get_calibrated_string, get_total_calibrated_number


class Puzzle1TestCase(TestCase):
    @parameterized.expand([
        ('1abc2', '12'),
        ('pqr3stu8vwx', '38'),
        ('a1b2c3d4e5f', '15'),
        ('treb7uchet', '77'),
        ('', None),
        ('two1nine', '29'),
        ('eightwothree', '83'),
        ('abcone2threexyz', '13'),
        ('xtwone3four', '24'),
        ('4nineeightseven2', '42'),
        ('zoneight234', '14'),
        ('7pqrstsixteen', '76'),
        ('eighthree', '83'),
        ('sevenine', '79'),
        ('eightone16nine', '89'),
        ('936', '96'),
        ('8vfvbrnclnmthree8onetwoeightthree', '83'),
    ])
    def test_get_calibrated_string(self, input_string, expected_output):
        self.assertEqual(get_calibrated_string(input_string), expected_output)

    def test_get_total_calibrated_number(self):
        self.assertEqual(get_total_calibrated_number(['12', '38', '15', '77']), 142)
        self.assertEqual(get_total_calibrated_number(['29', '83', '13', '24', '42', '14', '76']), 281)
