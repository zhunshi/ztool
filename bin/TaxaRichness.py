#!/usr/bin/env python3
import sys
import os
import gzip
from collections import defaultdict
import argparse

def ArgumentParser():
    parser = argparse.ArgumentParser(
        description='Calculate taxa richness')
    parser.add_argument("--input_data","-i",  help='input data', required=True)
    parser.add_argument("--out","-o",help="out file name",required=True)
    args = parser.parse_args()
    return args

def TaxaRichess(file_name):
    res = defaultdict(lambda :0)
    if file_name.endswith(".gz"):
        fh = gzip.open(file_name,'rt')
    else:
        fh = open(file_name,'r')
    
    header = fh.readline().strip().split("\t")
    for line in fh:
        line = line.rstrip().split("\t")
        line.pop(0)
        line = [1 if float(x)>0 else 0 for x in line]
        for i,j in zip(header,line):
            res[i] += j
    fh.close()
    return res

def output(data,file_name):
    with open(file_name,'w') as fh:
        fh.write(f"SampleID\tRichness\n")
        for i in data:
            fh.write(f"{i}\t{data[i]}\n")

def main():
    args = ArgumentParser()
    file_in = args.input_data
    file_out = args.out

    res = TaxaRichess(file_in)
    output(res,file_out)

if __name__ == "__main__":
    main()