#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:22:18 2017

@author: owenje
"""
from Bio import SeqIO
#import time
import os

def FileGen(TargetDir, extension = ".gbk",subset_tag = ""):
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
                    if seq_feature.type=="CDS" :
                        assert len(seq_feature.qualifiers['translation'])==1
                        try:
                            name = seq_feature.qualifiers['locus_tag'][0]
                        except KeyError:
                             name = seq_feature.qualifiers['product'][0]
                        output_handle.write(">%s from %s\n%s\n" % (
                               name,
                               gbk_filename.split("/")[-1],
                               seq_feature.qualifiers['translation'][0]))   
    output_handle.close()

#before = time.time()
#Parse_folder_to_multi_faa('/Users/spiffkringle/Desktop/polyaa/','All_clusters_multi.faa')
#after = time.time()

def Parse_single_to_multi_faa(gbk_filename,faa_filename):
    
    """
    parses a genbank file  and outputs a multi fasta file of proteins 
    """
    orf_num = 1
    output_handle = open(faa_filename, "w")
    with open(gbk_filename, "r") as input_handle:
        for seq_record in SeqIO.parse(input_handle, "genbank") :
            print("Dealing with GenBank record %s" % seq_record.id)
            for seq_feature in seq_record.features:
                if seq_feature.type=="CDS" :
                    assert len(seq_feature.qualifiers['translation'])==1
                    try:
                        name = seq_feature.qualifiers['locus_tag'][0]
                    except KeyError:
                         name = seq_feature.qualifiers['product'][0]
                    output_handle.write(">%s: %s from %s\n%s\n" % (
                           orf_num,
                           name,
                           gbk_filename.split("/")[-1],
                           seq_feature.qualifiers['translation'][0])) 
                    orf_num +=1
    output_handle.close()
    
#pat = '/Users/owenje/Dropbox/PapersAndData/Pateamine_paper/COG_analysis/pat_genome.gbk'
#out = '/Users/owenje/Dropbox/PapersAndData/Pateamine_paper/COG_analysis/pat_aa.fna'

#Parse_single_to_multi_faa(pat,out)
    

def ParseFolderToMultiOutput(target_dir):
    out_dir = target_dir + "aa_out"
    os.mkdir(out_dir)
    os.chdir(target_dir)
    for gbk_filename in FileGen(target_dir):
        faa_filename = out_dir +"/"+ "".join(gbk_filename.split("/")[-1].split(".")[:-1]) + ".faa"
        Parse_single_to_multi_faa(gbk_filename,faa_filename)
        
target_dir = '/Users/spiffkringle/Dropbox/PapersAndData/Pateamine_paper/COG_analysis/Single_bin_genomes_gbk/'

ParseFolderToMultiOutput(target_dir)

        
