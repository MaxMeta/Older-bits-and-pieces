#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:54:04 2017

@author: owenje
"""
import xml.etree.ElementTree as ET
import os
import json
import numpy as np

target_xml = '/Users/spiffkringle/Dropbox/PapersAndData/MoreB4/blast_out.xml'

def ParseXML(infile):
    """
    Parses XML file and returns an ET object
    """
    with open(infile,'r') as F:
        ParsedXML = ET.fromstring(F.read())
    return ParsedXML

parsed = ParseXML(target_xml)

iterations = parsed.findall(".BlastOutput_iterations/Iteration")

for iteration in iterations:
    gene_number = iteration.find("Iteration_iter-num").text
    query_length = iteration.find("Iteration_query-len").text
    db_match = iteration.find("Iteration_hits/Hit/Hit_def").text
    db_accession = iteration.find("Iteration_hits/Hit/Hit_id").text
    identities = iteration.find("Iteration_hits/Hit/Hit_hsps/Hsp/Hsp_identity").text
    align_len = iteration.find("Iteration_hits/Hit/Hit_hsps/Hsp/Hsp_align-len").text
    PID = str(float(identities)/float(align_len)*100).split(".")[0]
    print(gene_number,db_match,db_accession,PID )
    
