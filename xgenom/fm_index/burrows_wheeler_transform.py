"""
Functions to generate the Burrows-Wheeler Transform of a string
"""

def bwt(input):
    """
    Function that returns the Burrows Wheeler Transform of an input string
    :param input: The input tring
    :return: The BW-Transform of the input string, as a list
    """
    bw_matrix = []
    characters = list(input)
    for i in range(len(characters)):
        word = input[-1] + input[:-1]
        new = ''.join(word)
        input = new
        bw_matrix.append(new)
        i += 1

    bw_matrix = sorted(bw_matrix)

    bw_transform = []

    for i in range(len(bw_matrix)):
        element = bw_matrix[i]
        last = element[- 1]
        bw_transform.append(last)
        i = i + 1

    return bw_transform
