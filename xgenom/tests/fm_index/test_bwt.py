from unittest import TestCase
from xgenom.fm_index.burrows_wheeler_transform import bwt

class TestBwt(TestCase):
    def test_bwt(self):
        """
        Unit Test for the Burrows Wheeler Transform burrows_wheeler_transform.py/bwt() function
        """
        assert bwt("banana$") == list("annb$aa")
        assert bwt("Hello_my_name_is_Victor$") == list("r$_seoynimHV_ela__ltoicm")
        assert bwt("GGGACCCTTAGCGAATCTCT$") == list("TGGTAACGTTCCGAG$CTCAC")