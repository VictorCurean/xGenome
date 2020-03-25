"""
Functions for generating mock FASTA files, used for testing purposes.

"""
from random import randrange
from datetime import datetime

def generate_string(alphabet, size):
    """
    Function that generates a random string
    :param alphabet: A list of characters used to build the random string
    :param size: The size of the randomly generated string
    :return: A random string
    """
    if alphabet == []:
        raise ValueError("The alphabet must contain at least one character")
    if size < 0:
        raise ValueError("The length of the string cannot be negative")

    alph_len = len(alphabet)

    return ''.join([alphabet[randrange(alph_len)] for i in range(size)])


def generate_fasta_file(path):
    now = datetime.now()
    filename = now.strftime("file_%d/%m/%Y_%H:%M:%S.fasta")
    




