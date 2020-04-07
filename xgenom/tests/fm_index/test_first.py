from unittest import TestCase
from xgenom.fm_index.first import get_char_count
from xgenom.fm_index.first import get_first_function

class TestGet_char_count(TestCase):
    def test_get_char_count(self):
        """
        Unit Test for the char count first.py/get_char_count() function
        """
        #testing character count
        dict1 = get_char_count("AAAAGTTCTCGGTA", ["G", "A", "C", "T"])
        assert dict1["$"] == 1
        assert dict1["A"] == 5
        assert dict1["T"] == 4
        assert dict1["G"] == 3
        assert dict1["C"] == 2

        #testing that the dictionary is ordered by keys
        keys_list = []

        for k,v in dict1.items():
            keys_list.append(k)

        assert keys_list == sorted(["G", "A", "C", "T", "$"])

    def test_get_first_function(self):
        """
        Unit Test for the char count first.py/get_first_function() function
        """
        disct_fucntion = get_first_function("AAAAGTTCTCGGTA", ["G", "A", "C", "T"])

        assert disct_fucntion["$"] == (0, 0)
        assert disct_fucntion["A"] == (1, 5)
        assert disct_fucntion["C"] == (6, 7)
        assert disct_fucntion["G"] == (8, 10)
        assert disct_fucntion["T"] == (11, 14)





