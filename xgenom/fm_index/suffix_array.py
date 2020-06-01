"""
Function that computates the suffix array of a string, with gaps in respect to input
"""
from numba import jit


def suffix_array(input, step):
    """
    Function that returns a suffix array data structure with gaps in respect to input, as a dictionary
    The key of the dictionary is the position of the suffix in the original suffix array, and the value is the suffix position
    in the original :param input
    index
    :param input: The string on which to construct the gapped suffix array
    :param step: The distance between the values of the suffix array stored
    :return: a dictionary holding some positions of the suffix array and their respective value
    """
    suffix_array_list =  sorted(range(len(input)), key=lambda i: input[i:])
    sa_dict = {}

    for i in range(len(suffix_array_list)):
        if (suffix_array_list[i] % step == 0):
            sa_dict[i] = suffix_array_list[i]

    return sa_dict






