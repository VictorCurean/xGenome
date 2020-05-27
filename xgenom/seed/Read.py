"""
File that contains the class that stores info for one FASTQ Read
"""

class FASTQRead:
    read_id = ""
    sequence = ""
    phredscore = ""

    def __init__(self, read_id, sequence, phredscore):
        if len(sequence) != len(phredscore):
            raise ValueError("FASTQ Read Error - The PHRED Quality Score and the BP Sequence must be the same length for a Read")
        read_id = read_id.replace('\n', "")
        sequence = sequence.replace('\n', "").replace('N', "")
        sequence = sequence[0:10]
        phredscore = phredscore.replace('\n', "")
        self.read_id = read_id
        self.sequence = sequence
        self.phredscore = phredscore



