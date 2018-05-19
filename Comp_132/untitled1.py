#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:34:01 2018

@author: spiffkringle
"""

import random
from Bio import SeqIO
#standard genetic code, * indicates a stop codon
genetic_code = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
    "TCT":"S", "TCC":"s", "TCA":"S", "TCG":"S",
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
        


def decode_message(encoded_message, dictionary):
    """
    decodes (translates) a nucleotide sequence into a protein sequence
    """
    codons = [encoded_message[i:i+3] for i in range(0, len(encoded_message), 3)]
    decoded_list = [dictionary[codon] for codon in codons]
    
    return "".join(decoded_list)

#reverse_code = invert_dictionary(genetic_code)
#message = "THIS*IS*A*SECRET*MESSAGE*"
#encoded_message = encode_message(message, reverse_code)
#decoded_message = decode_message(encoded_message, genetic_code)
#print(decoded_message)

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
#below we pull out all of the protein sequences encoded ina a genome
#these are then put in a standard file format
#can then (for example) be searched against reference databases
#assign a putative biological function to each protein in the genome

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
    
    