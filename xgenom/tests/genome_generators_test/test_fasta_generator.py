from unittest import TestCase
from xgenom.genome_generators.fasta_generator import generate_string

class TestGenerate_string(TestCase):
    def test_generate_string(self):
        """
        Unit test for fasta_generator.py/generate_string() function
        """

        test_string = generate_string(["A", "C", "G", "T"], 100)
        assert len(test_string) == 100
        assert len(test_string) != 999

        test_string2 = generate_string(["A", "C", "G", "T"], 1000)
        assert test_string2.find("A") != -1
        assert test_string2.find("C") != -1
        assert test_string2.find("G") != -1
        assert test_string2.find("T") != -1

        assert test_string2.find("X") == -1
        assert test_string2.find("Y") == -1
