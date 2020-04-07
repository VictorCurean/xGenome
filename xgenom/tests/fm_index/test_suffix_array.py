from unittest import TestCase
from xgenom.fm_index.suffix_array import suffix_array


class TestSuffix_array(TestCase):
    def test_suffix_array(self):
        input = "Mississippi$"

        assert suffix_array(input, 1) == {0: 11, 1: 0, 2: 10, 3: 7, 4: 4, 5: 1, 6: 9, 7: 8, 8: 6, 9: 3, 10: 5, 11: 2}
        assert suffix_array(input, 2) == {1: 0, 2: 10, 4: 4, 7: 8, 8: 6, 11: 2}
