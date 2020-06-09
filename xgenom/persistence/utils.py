from xgenom.persistence.reference_persistence import *
from xgenom.fm_index.burrows_wheeler_transform import bwt as getbwt
from xgenom.fm_index.first import get_first_function
from xgenom.fm_index.suffix_array import suffix_array
from xgenom.fm_index.tally import get_tally

alphabet = ["A", "C", "G", "T", "$"]
rootdir = "D:\Licenta\Git Repository\\xGenome\\xgenom\\temp_data\\"

def store_fasta(filename, name, date, specimen):

    id = persist_reference_meta(name, date, specimen)

    f = open(rootdir+filename, "r")
    descrpt = f.readline()
    ref = f.read()
    ref += "$"

    #persisting reference
    persist_reference(id, ref)

    #building and persisting bwt
    bwt = getbwt(ref)
    persist_bwt(id, bwt)

    # #building and persisting first function
    # firsfunc = get_first_function(ref, alphabet)

    #building and persisting suffix array
    sa = suffix_array(ref, 5)
    persist_sa(id, sa)

    # #building and persisting tally
    # tally = get_tally(bwt, alphabet, 5)





