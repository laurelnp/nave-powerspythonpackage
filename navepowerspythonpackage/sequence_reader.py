import dendropy
import os.path
def sequence_reader(filepath):
    #pre condition check if the file path is there and correct 
    assert os.path.exists(filepath)
    sequence_set = dendropy.DnaCharacterMatrix.get(
        path=filepath,
        schema="phylip") 
        
   #post condition check the returned type is correct - should be dna char matrix 
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set) 
