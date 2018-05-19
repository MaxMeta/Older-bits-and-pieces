#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 23:26:00 2017

@author: spiffkringle
"""

from Bio import SeqIO
gbk_filename = '/Users/spiffkringle/Dropbox/blast/DB/1.final.gbk'
faa_filename = '/Users/spiffkringle/Dropbox/blast/DB/converted_PKS2.fna'
input_handle  = open(gbk_filename, "r")
output_handle = open(faa_filename, "w")

for seq_record in SeqIO.parse(input_handle, "genbank") :
    print("Dealing with GenBank record %s" % seq_record.id)
    output_handle.write(">%s %s\n%s\n" % (
           seq_record.id,
           seq_record.description,
           seq_record.seq))

output_handle.close()
input_handle.close()