from xgenom.fm_index.fm_index_search import exact_match_fm_index
from xgenom.seed import fastq_reader
from xgenom.fm_index.burrows_wheeler_transform import bwt as get_bwt
from xgenom.fm_index.suffix_array import suffix_array
from xgenom.fm_index.tally import get_tally
from xgenom.fm_index.first import get_first_function as first

# def bwt2(s):
#     """Apply Burrows-Wheeler transform to input string."""
#     assert "\002" not in s and "\003" not in s, "Input string cannot contain STX and ETX characters"
#     s = "\002" + s + "\003"  # Add start and end of text marker
#     table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
#     last_column = [row[-1:] for row in table]  # Last characters of each row
#     return "".join(last_column)  # Convert list of characters into string

# fasta = "D:\Licenta\Data\CGA009.fasta"

fasta = "D:\\Licenta\\Git Repository\\xGenome\\xgenom\\data\\file_27-05-2020_21-12-14.fasta"

f = open(fasta, "r")
descrpt = f.readline()
ref = f.read()
ref += "$"
alphabet = ["A", "C", "G", "T", "$"]

print(".....building the data structures.....")
print("______________________________________")
print(".....building the BWT.................")
bwt = get_bwt(ref)
# bwt = bwt2(ref)
print(".....building the Suffix Array........")
sa = suffix_array(ref, 10)
print(".....building the Tally...............")
tally = get_tally(bwt, ["A", "C", "G", "T", "$"], 10)
print(".....building the First Function......")
first_func = first(ref, ["A", "C", "G", "T", "$"])

reads = fastq_reader.read_from_file("D:\Licenta\Data\\example.fastq")

print("........initiating matching routine for reads.........")
counter = 0
exact_matches = []

for r in reads:
    counter += 1
    positions_found = exact_match_fm_index(ref, r.sequence, alphabet, bwt, first_func, sa, tally, 10, 10)
    if positions_found != []:
        res_tuple = (r.read_id, positions_found)
        exact_matches.append(res_tuple)

    print(counter)
    if counter % 100 == 0:
        print(str(counter) + " reads processed with " + str(len(exact_matches)) + "exact matches found")


print("........showing results........")
for t in exact_matches:
    print(str(t[0]) + "........." + str(t[1]))






