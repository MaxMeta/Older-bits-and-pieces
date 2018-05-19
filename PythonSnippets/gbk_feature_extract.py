#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 14:14:08 2018

@author: spiffkringle
"""
from Bio import SeqIO

def read_gbk(gbk):
    """
    Parses an antismash gbk file and returns a dictionary of relevant features
    that are subsequently used in vector generation. For modular genes, the
    label sec_met is used, and and ordered list of the modules present is 
    given with the key "sec_met"
    """
    #count = 0
    handle = open(gbk,'r')
    parsed = SeqIO.read(handle,"genbank")
    handle.close()
    return parsed


MH_phosphonate = read_gbk('/Users/spiffkringle/Desktop/genome.ctg.10k.smp/ctg7180000024262.cluster028.gbk')
str(MH_phosphonate.seq[40000:41000])


MH_lasso = read_gbk('/Users/spiffkringle/Dropbox/PapersAndData/SpongeData/R_bins_AS/P11b/57.cluster003.gbk')
str(MH_lasso.seq[20000:21000])

CS_lanti_93 = read_gbk( '/Users/spiffkringle/Dropbox/PapersAndData/SpongeData/CS_zamp/Zamp_hybSPA.antismash/c00001_NODE_1_...cluster093.gbk')
str(CS_lanti_93.seq[3000:4000])

CS_lanti_65 = read_gbk( '/Users/spiffkringle/Dropbox/PapersAndData/SpongeData/CS_zamp/Zamp_hybSPA.antismash/c00001_NODE_1_...cluster065.gbk')
str(CS_lanti_65.seq[22800:23800])

CS_lasso = read_gbk( '/Users/spiffkringle/Dropbox/PapersAndData/SpongeData/CS_zamp/Zamp_hybSPA.antismash/c00001_NODE_1_...cluster100.gbk')
str(CS_lasso.seq[14600:15600])

pat_target = '/Users/spiffkringle/Desktop/genome.ctg.10k.smp/ctg7180000024262.cluster001.gbk'

def Get_nuc_from_CDS_aa(gbk_file, CDS_name, aa_start, aa_stop):
    parsed = read_gbk(gbk_file)
    for feature in parsed.features:
        if feature.type == "CDS"  and feature.qualifiers["locus_tag"][0] == CDS_name:
            print("found it!")
            target = feature.extract(parsed)[3*aa_start:3*aa_stop]
            print(target.seq.translate())
        
Get_nuc_from_CDS_aa(pat_target,'ctg1_165',0,10)    
    
pat = read_gbk(pat_target)
