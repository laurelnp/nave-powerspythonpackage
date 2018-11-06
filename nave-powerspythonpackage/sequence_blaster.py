from Bio.Blast import NCBIWWW
from Bio import SeqIO 
#pre condition- check if file is there and is in fasta format-- check file format
#dont need an assertion here for pre condit because the first line in the code below already checks for that
def sequence_blaster(fasta_path, results_path):
    record = SeqIO.read(fasta_path, format="fasta")
    result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))
    
    save_file = open(results_path, 'w')
    save_file.write(result_handle.read())
    save_file.close()
    assert os.stat(results_file).st_size != 0 
    #post condition- check results file is not size zero
    