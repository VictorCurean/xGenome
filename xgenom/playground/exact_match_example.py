from xgenom.fm_index.fm_index_search import exact_match_fm_index
from xgenom.seed import fastq_reader
from xgenom.fm_index.burrows_wheeler_transform import bwt as get_bwt
from xgenom.fm_index.suffix_array import suffix_array
from xgenom.fm_index.tally import get_tally
from xgenom.fm_index.first import get_first_function as first
from timeit import default_timer as timer


#____________files________________
# fasta = "D:\Licenta\Data\CGA009.fasta"
fasta = "D:\\Licenta\\Git Repository\\xGenome\\xgenom\\data\\file_27-05-2020_21-12-14.fasta"


#____________reading files_________
start = timer()

print(".....reading files....................")
f = open(fasta, "r")
descrpt = f.readline()
ref = f.read()
ref += "$"
alphabet = ["A", "C", "G", "T", "$"]

#########TIMER###########
duration = timer() - start
duration_str = "{:.2f}".format(duration)
print("Finished in " + duration_str + " seconds...")
#########################


print(".....building the data structures.....")
print("______________________________________")
print(".....building the BWT.................")
bwt = get_bwt(ref)

#########TIMER###########
duration = timer() - start
duration_str = "{:.2f}".format(duration)
print("Finished in " + duration_str + " seconds...")
#########################

print(".....building the Suffix Array........")
sa = suffix_array(ref, 10)

#########TIMER###########
duration = timer() - start
duration_str = "{:.2f}".format(duration)
print("Finished in " + duration_str + " seconds...")
#########################

print(".....building the Tally...............")
tally = get_tally(bwt, ["A", "C", "G", "T", "$"], 10)

#########TIMER###########
duration = timer() - start
duration_str = "{:.2f}".format(duration)
print("Finished in " + duration_str + " seconds...")
#########################

print(".....building the First Function......")
first_func = first(ref, ["A", "C", "G", "T", "$"])

#########TIMER###########
duration = timer() - start
duration_str = "{:.2f}".format(duration)
print("Finished in " + duration_str + " seconds...")
#########################

print(".....reading fastq reads..............")
reads = fastq_reader.read_from_file("D:\Licenta\Data\\example.fastq")

#########TIMER###########
duration = timer() - start
duration_str = "{:.2f}".format(duration)
print("Finished in " + duration_str + " seconds...")
#########################

print("........initiating matching routine for reads.........")
counter = 0
exact_matches = []

for r in reads:
    counter += 1
    positions_found = exact_match_fm_index(ref, r.sequence, alphabet, bwt, first_func, sa, tally, 10, 10)
    if positions_found != []:
        res_tuple = (r.read_id, positions_found)
        exact_matches.append(res_tuple)

    if counter % 100 == 0:
        print(str(counter) + " reads processed with " + str(len(exact_matches)) + "exact matches found")

        #########TIMER###########
        duration = timer() - start
        duration_str = "{:.2f}".format(duration)
        print("Finished in " + duration_str + " seconds...")
        #########################


print("........showing results........")
for t in exact_matches:
    print(str(t[0]) + "........." + str(t[1]))






