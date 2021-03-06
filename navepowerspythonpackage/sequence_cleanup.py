import os
import dendropy

def sequence_cleanup(sequence_set, out_file, taxon, gene_start, gene_end):

   # pre condition check if its a string, if the files include taxon and gene, make sure theres an outfile
    assert sequence_set[taxon]
    my_taxon_sequence = sequence_set[taxon].symbols_as_string()
    my_taxon_sequence = my_taxon_sequence[gene_start : gene_end] 
    ofile = open(out_file, "w")
    ofile.write(">" + taxon + "\n" + my_taxon_sequence + "\n")
    ofile.close()
    assert os.stat(out_file).st_size != 0 
   # post condition check if theres a file, that it wrote out correctly (isnt empty) and is in correct spot  
