#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:22:18 2017

@author: owenje
"""
import os
from Bio import SeqIO
import time

#note that this was designed to work with antismash outputs. need to mod to make general

def FileGen(TargetDir, extension = ".gbk",subset_tag = "final"):
    """
    Looks one level down in a folder and iteratively yeilds all file names that 
    have the specified extension
    """
    
    for F in next(os.walk(TargetDir))[2]:
        print(F)
        if F[-1*len(extension):] == extension:
            if F.split(".")[-2][:len(subset_tag)] == subset_tag:
                yield(TargetDir + '/' + F)
    


def Parse_folder_to_multi_faa(target_dir,faa_filename):
    """
    Iterates a folder of gbk files and outputs a multi fasta file of
    """
    os.chdir(target_dir)
    output_handle = open(faa_filename, "w")
    for gbk_filename in FileGen(target_dir):
        with open(gbk_filename, "r") as input_handle:
            for seq_record in SeqIO.parse(input_handle, "genbank") :
                print("Dealing with GenBank record %s" % seq_record.id)
                for seq_feature in seq_record.features :
                    i = 0
                    if seq_feature.type=="CDS" :
                        assert len(seq_feature.qualifiers['translation'])==1
                        try:
                            name = seq_feature.qualifiers['locus_tag'][0]
                        except KeyError:
                             #name = seq_feature.qualifiers['product'][0]
                             name = str(i)
                        output_handle.write(">%s from %s\n%s\n" % (
                               name,
                               gbk_filename.split("/")[-1],
                               seq_feature.qualifiers['translation'][0])) 
                        i += 1
    output_handle.close()

before = time.time()
Parse_folder_to_multi_faa('/Users/spiffkringle/Desktop/polyaa/','All_all_multi.faa')
after = time.time()

