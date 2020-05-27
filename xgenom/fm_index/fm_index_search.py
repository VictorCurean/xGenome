"""
Functions for building and quering an FM-Index for a given input
"""
from xgenom.fm_index.burrows_wheeler_transform import bwt as get_bwt
from xgenom.fm_index.suffix_array import suffix_array
from xgenom.fm_index.tally import get_tally
from xgenom.fm_index.first import get_first_function as first
from xgenom.fm_index.search_tree import SearchTree, Node
from skbio import local_pairwise_align_ssw



def get_FIRST_nodes(symbol, first_struct, parent, ranks = []):
    """
    Function that initializez the first nodes of a pattern matching workflow
    :param symbol: the first symbol searched of the pattern
    :param first_struct: the first functio struct
    :param parent: the root node of a search tree
    :param ranks: the ranks boundry that should be kept
    :return: a list of Nodes, and their rank
    """
    nodes = []
    first_tupel = first_struct[symbol]
    postion_diff = first_tupel[0]

    for i in range(first_tupel[0], first_tupel[1] + 1):
        nodes.append(Node(symbol, i - postion_diff, i, parent))

    #returning all nodes
    if ranks == []:
        return nodes
    #returning only nodes with rank in the :param ranks
    else:
        for node in nodes:
            if node.rank not in ranks:
                nodes.remove(node)
        return nodes


def get_LAST_rank(character, absolute_position, tally, bwt):
    """
    Returns the character and its rank from the BW-Transform corresponding to an :param absolute_position  in the FIRST
    column of the BW-Matrix. The algorithm uses a partial tally matrix in order to computate the rank without storing
    all ranks for each individual character in the bw-transform
    :param character: the character that should be matched in the LAST column
    :param absolute_position: the absolute position of the previous matched character in the FIRST column
    :param tally: the partial tally matrix that keeps count on the number of appearances of each character
    :param bwt: the Burrows-Wheeler Transform/ The LAST column
    :return: the character and its rank, as a tuple
    """

    if absolute_position in tally.keys():
        closest_record = absolute_position
    else:
        closest_record = min(tally.keys(), key=lambda k: abs(k - absolute_position))

    char_rank = -1
    counter = 0
    if absolute_position == closest_record:
        char_rank = tally[closest_record][character] - 1

    elif closest_record < absolute_position:
        for k in range(absolute_position, closest_record, -1):
            if bwt[k] == character:
                counter += 1
        char_rank = tally[closest_record][character] + counter - 1

    elif closest_record > absolute_position:
        for k in range(absolute_position, closest_record + 1, 1):
            if bwt[k] == character:
                counter += 1
        char_rank = tally[closest_record][character] - counter

    if char_rank < 0:
        char_rank = 0

    return (character, char_rank)


def get_last_values(searched_character, prev_nodes, bwt, tally):
    """
    Function that returns the next matching values
    :param searched_character:
    :param prev_nodes:
    :param bwt:
    :param tally:
    :return:
    """
    bwt_values = []
    for node in prev_nodes:
        if bwt[node.first_position] == searched_character:
            bwt_values.append(get_LAST_rank(searched_character, node.first_position, tally, bwt))

    return bwt_values

def get_FIRST_pos_from_rank(character, rank, first_func):
    """
    Function that returns the absolute position of a chaaracter in a BW-Transform based on their relative rank
    :param character: character the needs its absolute position found
    :param rank: the relative rank of the character
    :param first_func: the first function of the FM-index
    :return: the absolute position of the character in the BW-transform
    """
    return first_func[character][0] + rank

def resolve_offset(char_first_pos, first_func, bwt, tally, sa):
    """
    Function that returns the offset of a character in the original pattern
    More precisley, this function is used to determine the exact position of a match found using the FM-Index, in the
    original pattern
    :param first_char_abs_pos: the absolute position of a character in the BW-Transform
    :param sa:the partial suffix array from the pattern
    :return: the offset of the character in the original pattern
    """
    current_pos = char_first_pos
    moves_made = 0
    while current_pos not in sa.keys():
        next_char = bwt[current_pos]
        last_rank_tuple = get_LAST_rank(next_char, current_pos, tally, bwt)
        current_pos = get_FIRST_pos_from_rank(last_rank_tuple[0], last_rank_tuple[1], first_func)
        moves_made += 1


    return  sa[current_pos] + moves_made


def exact_match_fm_index(reference, pattern, alphabet, suffix_array_step, tally_step):
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

    bwt = get_bwt(reference)
    first_func = first(reference, alphabet)
    sa = suffix_array(reference, suffix_array_step)
    tally = get_tally(bwt, alphabet, tally_step)

    pattern = ''.join(reversed(pattern))

    matches_found = []
    start_character, pattern = pattern[0], pattern[1 : len(pattern)]

    #depth first search in the fm index:
    for pos in range(first_func[start_character][0], first_func[start_character][1] + 1):

        pattern_copy = pattern
        current_pos = pos
        continue_matching = True

        while continue_matching:
            if bwt[current_pos] == pattern_copy[0]:
                next_char, pattern_copy = pattern_copy[0], pattern_copy[1 : len(pattern_copy)]
                last_rank_tuple = get_LAST_rank(next_char, current_pos, tally, bwt)
                current_pos = get_FIRST_pos_from_rank(next_char, last_rank_tuple[1], first_func)

                #An exact match for the whole pattern has been found
                if len(pattern_copy) == 0:
                    matches_found.append(resolve_offset(current_pos, first_func, bwt, tally, sa))
                    continue_matching = False

            else:
                continue_matching = False


    return matches_found


