"""
Functions for building and quering an FM-Index for a given input
"""
from xgenom.fm_index.burrows_wheeler_transform import bwt as get_bwt
from xgenom.fm_index.suffix_array import suffix_array
from xgenom.fm_index.tally import get_tally
from xgenom.fm_index.first import get_first_function as first
from xgenom.fm_index.search_tree import SearchTree, Node


def get_first_nodes(symbol, first_struct, parent):
    """
    Function that initializez the first nodes of a pattern matching workflow
    :param symbol: the first symbol searched of the pattern
    :param first_struct: the first functio struct
    :param parent: the root node of a search tree
    :return: a list of Nodes, and their rank
    """
    nodes = []
    first_tupel = first_struct[symbol]
    postion_diff = first_tupel[0]

    for i in range(first_tupel[0], first_tupel[1] + 1):
        nodes.append(Node(symbol, i - postion_diff, parent))

    return nodes



def exact_match_fm_index(reference, pattern):
    """
    Function that returns the positions where :param pattern matches the :param reference as a list
    The function will build the BW-transform and partial suffix array for :param reference,
    as well as the tally for the LAST column, and the first function for the FIRST column

    After the fm-index and its helper constructions have been build, a backward exact string match algorithm will find
    the positions where the pattern matches the reference

    :param reference: the reference where patterns will be searched
    :param pattern: the searched pattern, as a list of characters
    :return: a list containing the positions where :param pattern matches the :param reference
    """
    suffix_array_step = 5
    tally_step = 5
    alphabet = ["A", "B", "$"]

    bwt = get_bwt(reference)
    first_func = first(reference, alphabet)
    sa = suffix_array(reference, suffix_array_step)
    tally = get_tally(input, alphabet, tally_step)

    pattern = reversed(pattern)

    search_tree = SearchTree(Node("START", -1, None))

    search_tree.latest_nodes = get_first_nodes(pattern.pop(0), first_func, search_tree.root)

    while len(pattern) != 0:
        current_symbol = pattern.pop(0)
        next_nodes =

















