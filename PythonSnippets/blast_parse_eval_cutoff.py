#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:25:50 2017

@author: spiffkringle
"""
from Bio import SeqIO
#pull out frmt 6 matches that meet cutoff
cutoff = 0.001
match_set = set({})
fasta = '/Users/spiffkringle/Desktop/pat_frags/idba_ud_k20_240_contig.fa'
blastout = '/Users/spiffkringle/Desktop/pat_frags/ks_blastout.txt'
outdir = '/Users/spiffkringle/Desktop/pat_frags/'
outname = 'MH_KS_hits.fasta'

with open(blastout, 'r') as F:
    for line in F:
        if float(line.split()[-2]) < cutoff:
            #print(line.split()[-2], line.split()[1])
            match_set.add(line.split()[1])
            
            
print(list(sorted(match_set)))

with open(fasta, 'r') as F:
    seqs = SeqIO.parse(fasta,"fasta")
    #print(type(seqs))

with open(outdir + outname,'w') as F:
    for record in seqs:
        if record.id in match_set:
            #print(record.id)
            SeqIO.write(record,F,"fasta")