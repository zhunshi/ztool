#!/usr/bin/env python3
import sys
import os
import gzip
import math
import argparse
from itertools import combinations

def ArgumentParser():
    parser = argparse.ArgumentParser(
        description='Splice big data to specific number and combinie between any two')
    parser.add_argument("--input_data",  help='input big data table', required=True)
    parser.add_argument("--out_tmp",default=os.getcwd(),help="Tempory profiles output directory")
    parser.add_argument("--n_split_samples",type=int,default=100,help="number of samples to be a files. ")
    args = parser.parse_args()
    return args

def openFile(file_name):
    if file_name.endswith("gz"):
        fh = gzip.open(file_name,'rt')
    else:
        fh = open(file_name,'r')
    return fh

def Splice_list(l,n):
    l2 = [l[i:(i+n)] for i in range(0,len(l),n)]
    l2 = ["\t".join(x) for x in l2]
    return l2

def output(l,fh,g_id):
    for i,j in zip(l,fh):
        j.write(g_id+"\t"+i+"\n")

def DataProcess(IN_fh,Num_split,OUT_p):
    # read header
    header = IN_fh.readline().strip().split()
    n_sample = len(header)

    sample_names = Splice_list(header,Num_split)
    a = list(combinations(sample_names,2))
    a = [x+y for x,y in a]
    out_fh = [open(OUT_p+str(x),'w') for x in range(len(a))]
    output(a,out_fh,"")

    for line in IN_fh:
        line = line.rstrip().split()
        gene_id = line.pop(0)
        if len(line)!=n_sample:
            print(f"Samples number Error in gene ID: {gene_id}")
        tmp = Splice_list(line,Num_split)
        tmp = list(combinations(tmp,2))
        tmp = [x+y for x,y in tmp]
        output(tmp,out_fh,gene_id)
    
    [x.close() for x in out_fh]

def main():
    # args parser
    args = ArgumentParser()
    
    # tempory output
    tmpdir = args.out_tmp
    if not os.path.exists(tmpdir):
        os.mkdir(tmpdir)
    tmp_prefix = os.path.join(tmpdir,"tmp.")
    
    in_fh = openFile(args.input_data)
    len_split = math.ceil(args.n_split_samples/2)

    DataProcess(in_fh,len_split,tmp_prefix)


if __name__ == "__main__":
    main()
