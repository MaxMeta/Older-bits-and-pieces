#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 13:04:21 2018

@author: spiffkringle
"""

import random
from Bio import SeqIO
import pylab
import matplotlib.pyplot as plt
import os

#standard genetic code, * indicates a stop codon

genetic_code = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
    "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
    "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
    "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W",
    "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def invert_dictionary(dictionary):
    """
    inverts a dictionary where multiple keys might have the same value
    values of inverted dicctionary are lists of keys from orginal dictionary
    """
    inverted = {}
    for key in dictionary.keys():
        if not dictionary[key] in inverted:
            inverted[dictionary[key]] = [key]
        else:
            inverted[dictionary[key]].append(key)
    return inverted

reverse_code = invert_dictionary(genetic_code)



#give each student own random seed, should get unique answers
def encode_message(message,dictionary):
    """
    Takes a protein string and reverse translages in to a nucleotide
    where mutliple codon choices exist, these are selected randomly
    """
    encoded_message = ""
    for letter in message:
        encoded_message += random.choice(dictionary[letter])
        
    return encoded_message
        
def Make_Codons(DNA):
    """
    splits a DNA sequence into 3mers
    """
    return  [DNA[i:i+3] for i in range(0, len(DNA), 3)]

def decode_message(encoded_message, dictionary):
    """
    decodes (translates) a nucleotide sequence into a protein sequence
    """
    codons = Make_Codons(encoded_message)
    decoded_list = [dictionary[codon] for codon in codons]
    
    return "".join(decoded_list)


message = "THIS*IS*A*SECRET*MESSAGE*"
encoded_message = encode_message(message, reverse_code)
decoded_message = decode_message(encoded_message, genetic_code)
print(encoded_message)
print(decoded_message)

def parse_file(sequence_file):
    """
    parses an example file containing a nucleotide sequence
    part of this sequence encodes the hidden message
    one of the lines indicates the indices of the hidden message
    designed to give an idea of how real sequence files are structured and parsed
        -pulls out the start and end location of the hidden message
        -returns a list containing the start, stop, nucleotide sequnce
        """
    with open(sequence_file,"r") as F:
        append = False
        seq = ""
        
        for line in F:
            
            if append:
                seq += line.strip()
                
            if line[:3] == "loc":
                data = line.strip().split()[1].split("-")
                start = int(data[0])
                end = int(data[1])
                
            if line[0] == ">":
                append = True                
    return [start,end,seq]
#replace with your path to example_data.txt             
example_data = '/Users/spiffkringle/Dropbox/Code/Comp_132/example_data.txt'

def get_message(file,dictionary):
    """
    takes an example_file containing a nucleotide seq encoding a hidden message
    and the indices of the hidden message
    prints the hidden message
    """
    data = parse_file(file)
    start = data[0]
    end = data[1]
    sequence = data[2]
    message_sequence = sequence[start:end]
    
    print((decode_message(message_sequence, genetic_code)))

get_message(example_data, genetic_code)

#real gbk files are complex, but Biopython takes care of this complexity for us
#really it is just doing what we have outlined above
#but structure of input file is more complex
#below we use SeqIO to pull out all of the protein sequences encoded in a genome
#these are then put in a standard file format
#can then (for example) be searched against reference databases


def Parse_gbk_to_multi_faa(gbk_filename,faa_filename):
    
    """
    parses a genbank file  and outputs a multi fasta file of proteins 
    """
    output_handle = open(faa_filename, "w")
    
    with open(gbk_filename, "r") as input_handle:
        
        for seq_record in SeqIO.parse(input_handle, "genbank") :
            print("Dealing with GenBank record %s" % seq_record.id)
            
            for seq_feature in seq_record.features:
                
                if seq_feature.type=="CDS" and 'translation' in seq_feature.qualifiers:
                    name = seq_feature.qualifiers['locus_tag'][0]
                    output_handle.write(">%s from %s\n%s\n" % (
                       name,
                       gbk_filename.split("/")[-1],
                       seq_feature.qualifiers['translation'][0]))
                    
    output_handle.close()

#Update paths    
genome_file = '/Users/spiffkringle/Dropbox/Code/Comp_132/E_coli.gbk'
output_name = '/Users/spiffkringle/Dropbox/Code/Comp_132/E_coli_proteins.faa'
Parse_gbk_to_multi_faa(genome_file, output_name) 

proteins = SeqIO.parse(output_name, "fasta")
lengths = [len(record.seq) for record in proteins]
pylab.hist(lengths, bins=30)
#could fit various distributions to these data and see which one best describes

#do some other task according to biopython documentation
#blast against NCBI server 
#parse xml output to a table
#plot a histogram of protein lengths (matplotlib)
#look at GC content and codon bias for multiple genomes
#codon usage bias
 
def FileGen(TargetDir, extension = ".gb",subset_tag = ""):
    """
    Looks one level down in a folder and iteratively yeilds all file names that 
    have the specified extension. If you can also choose only a subset using subset tag
    """
    
    for F in next(os.walk(TargetDir))[2]:
        print(F)
        if F[-1*len(extension):] == extension:
            if F.split(".")[-2][:len(subset_tag)] == subset_tag:
                yield(TargetDir + '/' + F)

#could make them use biopython to download a list of gbk files

def Get_Gene_Sequences(target_dir):
    """
    here we pull out the nucleotide sequences that encode proteins in
    from a folder of gbk files. return a dictionary where keys are the 
    file names, and vaues are a list of gene sequences
    """
    os.chdir(target_dir)
    genomes = {}
    for gbk_filename in FileGen(target_dir):
        name = gbk_filename.split("/")[-1]
        genomes[name] = []
        with open(gbk_filename, "r") as input_handle:
            for seq_record in SeqIO.parse(input_handle, "genbank"):
                print("Dealing with GenBank record %s" % seq_record.id)
                for seq_feature in seq_record.features :
                    if seq_feature.type=="CDS" and 'translation' in seq_feature.qualifiers:
                        genomes[name].append(str(seq_feature.extract(seq_record).seq))
    return genomes
#seems unreasonably slow. Don't use seq_feature.extract?
#use smaller example data? 


target_dir = '/Users/spiffkringle/Dropbox/Code/Comp_132/Genome_to_parse/'

genome_dict = Get_Gene_Sequences(target_dir)

#make a counts dictionary


def Count_Codons(genome_dict):
    """
    Takes dictionary of gene sequences for multiple organisms
    Returns a dictionary of codon usage counts for each
    """
    codon_data = {}
    for genome in genome_dict:
        codon_data[genome] = {key:0 for key in genetic_code.keys()}
        for gene in genome_dict[genome]:
            codons = Make_Codons(gene)
            for codon in codons:
                if len(codon) == 3:
                    codon_data[genome][codon] += 1
    return codon_data
    
codon_counts = Count_Codons(genome_dict)

def Plot_Dictionary(dictionary, title="title", ylabel="ylabel"):
    ax = plt.subplots()[1]
    plt.bar(range(len(dictionary)), list(dictionary.values()), align='center')
    plt.xticks(range(len(dictionary)), list(dictionary.keys()))
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show() 

def Plot_Codons(codon_counts, amino_acid, dictionary=reverse_code):
    codons = dictionary[amino_acid]
    for genome in codon_counts:
        total = sum([codon_counts[genome][codon] for codon in codons])
        to_plot = {codon:codon_counts[genome][codon]/total for codon in codons}
        Plot_Dictionary(to_plot,title=genome + " codon usage for " + amino_acid,ylabel="frequencey")
        
Plot_Codons(codon_counts,"R")            
        



 

                      