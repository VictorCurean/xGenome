from unittest import TestCase
from xgenom.fm_index.tally import get_tally


class TestGet_tally(TestCase):
    def test_get_tally(self):
        input = ["a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d"]
        alphabet = ["a", "b", "c", "d"]
        step = 4

        result = get_tally(input, alphabet, step)
        assert result == {0: {'a': 1, 'b': 0, 'c': 0, 'd': 0}, 4: {'a': 2, 'b': 1, 'c': 1, 'd': 1}, 8: {'a': 3, 'b': 2, 'c': 2, 'd': 2}}
