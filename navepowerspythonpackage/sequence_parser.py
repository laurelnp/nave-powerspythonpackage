"""Function that parses the BLAST output and lists the results"""

from Bio.Blast import NCBIXML
import os 

def sequence_parser(filepath):

 
    assert os.path.exists(filepath)
    result_handle = open(filepath, 'r')

    blast_records = NCBIXML.parse(result_handle)

    blast_records = list(blast_records)

    blast_records 

