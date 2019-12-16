#!/usr/bin/env python3
import sys
import os
import gzip
from collections import defaultdict
import argparse

def ArgumentParser():
    parser = argparse.ArgumentParser(
        prog="CombineTables",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''
    Combine Tables
    from position arguments or a file list
    ''')
    parser.add_argument("Files",nargs="*",default=[],help="files to be combined")
    parser.add_argument("--input_file_list","-i",  help='input files list')
    parser.add_argument("--out","-o",help="out file name",required=True)
    args = parser.parse_args()
    return args

def ReadPositionFiles(files):
    out = defaultdict(dict)
    for file in files:
        with open(file,'r') as fh:
            SampleNames = fh.readline().rstrip().split("\t")
            for line in fh:
                line = line.rstrip().split("\t")
                rownames = line.pop(0)
                for x,y in zip(line,SampleNames):
                    out[rownames][y] = x
    return out

def ReadTables(file_name):
    out = {}
    with open(file_name,'r') as fh:
        fh.readline()
        for line in fh:
            line = line.rstrip().split("\t")
            rownames = line.pop(0)
            out[rownames] = line[1]
    return out

def ReadListFiles(file_name):
    out = defaultdict(dict)
    file_list = {}
    with open(file_name,'r') as fh:
        for line in fh:
            line = line.rstrip().split("\t")
            file_list[line[0]] = ReadTables(line[1])
    return out

def Output(data,file_name):
    with open(file_name,'w') as fh:
        SampleNames = list(fh.keys())
        header = "\t".join(SampleNames)
        fh.write(f"\t{header}\n")
        for sample in data:
            fh.write(f"{sample}")
            for k in sorted(data[sample]):
                fh.write(f"\t{data[sample][k]}")
            fh.write(f"\n")

def main():
    args = ArgumentParser()
    # check input file
    if len(args.Files)==0 and args.input_file_list is None:
        print("InputFileERROR:\n\tAt least one file should be provide")
        sys.exit()
    # read files from position arguments
    if len(args.Files)>0:
        data_position = ReadPositionFiles(args.Files)
    # read files from a file list
    if args.input_file_list is not None:
        data_list = ReadListFiles(args.input_file_list)
    # combine data
    if data_position is not None and data_list is not None:
        res = data_position.update(data_list)
    elif data_position is not None:
        res = data_position
    elif data_list is not None:
        res = data_list
    # output
    Output(res,args.out)

if __name__ == "__main__":
    main()