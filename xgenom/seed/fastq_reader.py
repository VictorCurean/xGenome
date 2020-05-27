"""
Methods for reading and storing a fastq file, and transforming it into Read objects
"""
from xgenom.seed.Read import FASTQRead

def read_from_file(file):
    f = open(file, "r")
    reads = []
    counter = 0;

    while(True):
        #reading the lines
        read_id = f.readline()
        sequence = f.readline()
        f.readline()
        phredscore = f.readline()

        #logging the process
        counter += 1
        if counter % 1000 == 0:
            print(str(counter) + " reads processed")
            print("current read ....... " + read_id)

        #ensuring the while loop is not infinite
        if read_id == "":
            print(str(counter) + " total reads processed.")
            break

        #validating reads
        try:
            read = FASTQRead(read_id, sequence, phredscore)
            reads.append(read)
        except(ValueError):
            print("Read " + read_id + " has an invalid format")

    f.close()

    return reads


# examplefile = "D:\Licenta\Data\\example.fastq"
#
# test = read_from_file(examplefile)



