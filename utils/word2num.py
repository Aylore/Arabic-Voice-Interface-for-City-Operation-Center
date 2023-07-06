"""
This module provides a function for converting number words in a string to their numerical representation.
"""

import re
from string import punctuation

def words_to_numbers(text: str) -> str:
    """
    Converts number words in a given string to their numerical representation.

    This function takes a string as input and replaces any number words (e.g., "one", "two", "three") with their numerical
    representation (e.g., "1", "2", "3").

    Args:
        text: The string to convert.

    Returns:
        A new string with the number words replaced by their numerical representation.
    """

    number_words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
        "billion": 1000000000,
        "trillion": 1000000000000,
    }

    words = re.sub(rf"[{punctuation}]", "", text).split()

    return " ".join(
        str(number_words[word]) if word in number_words else word for word in words
    )


if __name__ == "__main__":
    print(words_to_numbers("I want alert id one."))