from unittest import TestCase
from xgenom.fm_index.first import get_first_function
from xgenom.fm_index.search_tree import Node
from xgenom.fm_index.fm_index_search import get_first_nodes


class TestGet_first_nodes(TestCase):
    def test_get_first_nodes(self):
        dict_function = get_first_function("AAAAGTTCTCGGTA", ["G", "A", "C", "T"])
        start_node = Node(None, None, None)
        start_symbol = "A"

        assert len(get_first_nodes("A", dict_function, start_node)) == 5
        assert len(get_first_nodes("G", dict_function, start_node)) == 3
        assert len(get_first_nodes("T", dict_function, start_node)) == 4
        assert len(get_first_nodes("C", dict_function, start_node)) == 2

        print(get_first_nodes("G", dict_function, start_node))





