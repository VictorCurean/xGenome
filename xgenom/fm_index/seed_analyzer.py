"""
Functions for analyzing reads (and their respective PHRED quality scores) for determining the best seed candidates

READ EXAMPLE:
@HWUSI-EAS300R_0005_FC62TL2AAXX:8:30:18447:12115#0/1
CGTAGCTGTGTGTACAAGGCCCGGGAACGTATTCACCGTG
+HWUSI-EAS300R_0005_FC62TL2AAXX:8:30:18447:12115#0/1
acdd^aa_Z^d^ddc`^_Q_aaa`_ddc\dfdffff\fff

"""

def get_best_seed(read, quality_scores):
