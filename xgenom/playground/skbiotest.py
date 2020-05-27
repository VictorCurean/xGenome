from skbio import local_pairwise_align_ssw,DNA
from skbio.alignment import global_pairwise_align_nucleotide

alignment, score, start_end_positions = global_pairwise_align_nucleotide(DNA("ACTAAGGCTCTCTACCCCTTCTCAGAGATTT"), DNA("ACTAAGGCTCCTAACCCCCTTTTCTCAGATTAAAA"))
print(alignment)