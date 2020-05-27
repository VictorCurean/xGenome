from unittest import TestCase
from xgenom.fm_index.first import get_first_function
from xgenom.fm_index.search_tree import Node
from xgenom.fm_index.fm_index_search import get_FIRST_nodes, get_LAST_rank
from xgenom.fm_index.tally import get_tally
from xgenom.fm_index.burrows_wheeler_transform import bwt as get_bwt
from xgenom.fm_index.fm_index_search import exact_match_fm_index


class TestGet_first_nodes(TestCase):
    def test_get_first_nodes(self):
        dict_function = get_first_function("AAAAGTTCTCGGTA", ["G", "A", "C", "T"])
        start_node = Node(None, None, None, None)
        start_symbol = "A"

        assert len(get_FIRST_nodes("A", dict_function, start_node)) == 5
        assert len(get_FIRST_nodes("G", dict_function, start_node)) == 3
        assert len(get_FIRST_nodes("T", dict_function, start_node)) == 4
        assert len(get_FIRST_nodes("C", dict_function, start_node)) == 2

        print(get_FIRST_nodes("A", dict_function, start_node))


    def test_get_LAST_rank(self):
        reference = "AAAAGTTCTCGGTAAAAAGTTCTCGGTA$"
        bwt = get_bwt(reference)
        tally = get_tally(bwt, ["G", "A", "C", "T"], 4)

        assert get_LAST_rank("A", 0, tally, bwt) == ("A", 0)
        assert get_LAST_rank("A", 10, tally, bwt) == ("A", 7)
        assert get_LAST_rank("T", 11, tally, bwt) == ("T", 2)


        reference = "BANANA$"
        bwt = get_bwt(reference)
        tally = get_tally(bwt, ["A", "B", "N"], 5)

        assert get_LAST_rank("A", 0, tally, bwt) == ("A", 0)
        assert get_LAST_rank("N", 1, tally, bwt) == ("N", 0)
        assert get_LAST_rank("N", 2, tally, bwt) == ("N", 1)
        assert get_LAST_rank("B", 3, tally, bwt) == ("B", 0)
        assert get_LAST_rank("A", 5, tally, bwt) == ("A", 1)
        assert get_LAST_rank("A", 6, tally, bwt) == ("A", 2)




    def test_exact_match_fm_index(self):
        print(sorted(["M", "I", "S", "P", "$"]))

        assert sorted(exact_match_fm_index("BANANA$", "NA", ["A", "B", "N", "$"], 2, 5)) == [2, 4]
        assert sorted(exact_match_fm_index("BANANA$", "ANA", ["A", "B", "N", "$"], 5, 5)) == [1, 3]
        assert sorted(exact_match_fm_index("BANANA$", "BANA", ["A", "B", "N", "$"], 2, 2)) == [0]

        assert sorted(exact_match_fm_index("MISSISSIPPI$", "SSI", ['S', 'I', 'M', 'P', '$'], 3, 4)) == [2, 5]
        assert sorted(exact_match_fm_index("AAAAAAAAAAABBBAAAAAAA$", "BBB", ["A", "B", "$"], 2, 4) ) == [11]








