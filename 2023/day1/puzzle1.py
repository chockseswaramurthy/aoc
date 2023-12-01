# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
#
# For example:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
#
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
#
# Consider your entire calibration document. What is the sum of all of the calibration values?
from typing import Optional, List, Dict, Tuple

NUMBER_MAP = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def concat_two_strings(string1: str, string2: str) -> str:
    return string1 + string2


def find_number_and_position(input_str: str) -> Dict[str, str]:
    return_dict = {}
    for index, character in enumerate(input_str):
        if character.isdigit():
            return_dict[index] = character

    return return_dict


def find_number_and_position_by_word(input_str: str) -> Dict[str, str]:
    return_dict = {}
    for key, value in NUMBER_MAP.items():
        if key in input_str:
            indexes = [i for i, _ in enumerate(input_str) if input_str.startswith(key, i)]
            for index in indexes:
                return_dict[index] = value

    return return_dict


def get_max_min_dict_values(input_dict: Dict[str, str]) -> Tuple[str, str]:
    max_key = max(input_dict)
    min_key = min(input_dict)
    return input_dict[max_key], input_dict[min_key]


def get_calibrated_string(input_str: str) -> Optional[str]:
    dict1 = find_number_and_position(input_str)
    dict2 = find_number_and_position_by_word(input_str)
    dict3 = dict1.copy()
    dict3.update(dict2)

    if not dict3:
        return

    max_value, min_value = get_max_min_dict_values(dict3)
    return concat_two_strings(min_value, max_value)


def get_total_calibrated_number(op_values: List[str]) -> int:
    return sum([int(output_value) for output_value in op_values if output_value])


if __name__ == '__main__':
    output_values = []
    with open('input1.txt', 'r') as input_file:
        input_strings = input_file.readlines()
        for input_string in input_strings:
            output_value = get_calibrated_string(input_string)
            output_values.append(output_value)
            #print(input_string.strip() + ' = ' + output_value)

    print(get_total_calibrated_number(output_values))

