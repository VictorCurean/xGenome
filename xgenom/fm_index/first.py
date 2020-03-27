"""
Function that computates the FIRST column function of the FM-Index
"""

import collections

def get_char_count(input, alphabet):
    """
    Functions that returns an ordered dictionary, that holds the count for each character in an input string
    The function also artificially inserts the "$" symbol in the dictionary
    :param input: The input string
    :param alphabet: The characters that will be counted in the input string
    :return: An ordered (by key) dictionary with the character as key, and count as value
    """
    chars = {}
    for c in alphabet:
        chars[c] = input.count(c)

    chars["$"] = 1

    return collections.OrderedDict(sorted(chars.items()))

def get_first_function(dict):
    """
    Function that returns a dictionary corresponding to the FM-Index first column mapping of a character
    The Function has the characters as keys, and the value is a tuple holding the first occurrence the last occurrence
    :param dict: the dictionary holding the character count of a string
    :return: the dictionary holding the intervals at which a character is located in the FIRST column of the FM-index
    """

    function_dict = {}
    prev_first_value = 0
    prev_last_value = 0

    for k, value in dict.items():

        function_dict[k] = (prev_first_value, prev_last_value + value - 1)
        prev_first_value += value
        prev_last_value += value

    return function_dict








