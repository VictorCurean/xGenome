"""
Functions for the tally construct of the FM-index
"""
from numba import jit


def get_tally(bwt, alphabet, step):
    """
    Function that generates a dictionary with the position as a key, and another dictionary with tally counters as value
    The second dictionary that stores the values wil have the following form (example) : {a: 1, b: 0, c: 5, ...}
    The function will store the tally counter for size(:param input) / :param step positions.
    The values considered will be given as a list in :param alphabet

    The function holds exception handling for the special character "$" marking the end of the line - it will not count
    this character for it is assumed that it will appear only once in the input
    :param bwt: A BW-Transform as a list
    :param alphabet: The alphabet containing the values that should be counted
    :param step: The distance between positions where a tally will be counted
    :return: A disctionary of the form: {0: {a: 1, b: 0, c: 5, ...}, 0 + :param step : {a: 10, b: 0, c: 5, ...}, ... }
    """

    tally = {}
    step_tally = {}

    #initialize step_tally
    for val in alphabet:
        step_tally[val] = 0

    for i in range(len(bwt)):
        try:
            step_tally[bwt[i]] += 1
            if (i % step == 0):
                tally[i] = step_tally
                step_tally = step_tally.copy()
        except KeyError:
            continue

    return tally


