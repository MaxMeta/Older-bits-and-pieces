#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:19:43 2018

@author: spiffkringle
"""
gbk1 = '/Users/spiffkringle/Desktop/genome.ctg.10k.smp/ctg7180000024262.cluster024.gbk'
OutName = '/Users/spiffkringle/Desktop/ctg21.fasta'

from Bio import SeqIO

def GbkToFasta(InputFile,OutputFile):
    """
    Converts a (possibly multi) GBK file into a (possibly multi) FASTA file
    """

    
    input_handle  = open(InputFile, "r")
    output_handle = open(OutputFile, "w")
    
    for seq_record in SeqIO.parse(input_handle, "genbank") :
        print("Dealing with GenBank record %s" % seq_record.id)
        output_handle.write(">%s %s\n%s\n" % (
               seq_record.id,
               seq_record.description,
               seq_record.seq))
    
    output_handle.close()
    input_handle.close()
    
GbkToFasta(gbk1,OutName)

def GbkToString(Gbk):
    """
    Takes a path to GBK file and returns a string of the sequence
    """
    with open(Gbk, "r") as F:
        seq = SeqIO.read(F, "genbank")
        
        return str(seq.seq)
        
NRPS_cluster = GbkToString(gbk1)
