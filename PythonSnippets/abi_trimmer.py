# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:49:17 2015

@author: SpiffKringle
"""
import os
from Bio import SeqIO, Alphabet


targetDir = '/Users/owenje/Dropbox/PapersAndData/LiweiPKS/sequencing result-Liwei/20170903/170828FN-011/'
extensions = set(['.ab1'])
#can't handle Ns, is the alphabet set wrong?

generator =  os.walk(targetDir)#this will recursively yeild a tuple of (currentDir, subdirs in currentDir, files in CurrentDir)
items = next(generator)#look one level down only
fileList = items[2]#the file list is third in the tuple
dirName = items[0]
#os.mkdir(dirName + '/newdir')
records = []
for fname in fileList:
    print(fname)
    if fname[-4:] in extensions:
        to_open = os.path.join(dirName,fname)
        OutName = to_open[:-4] +'.fastq'
        #print to_open
        Handle = open(to_open,'rb')
        record = SeqIO.read(Handle,'abi')
        record.seq.alphabet = Alphabet.IUPAC.ambiguous_dna
        trimmed = SeqIO.AbiIO._abi_trim(record[20:])
        print(len(record), len(trimmed))
        records.append(trimmed)

for record in records:
    print(record.id, len(record))
#outHandle = os.path.join()        
with open(targetDir + '/Multifasta.fasta','w') as f:
    for record in records:
        f.write('> ' + str(record.id) +'\n')
        f.write(str(record.seq) + '\n')
        
        
        
        

    
    

                    
                    
