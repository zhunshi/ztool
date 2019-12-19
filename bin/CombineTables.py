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
    Combine Tables from position arguments or a file list
    Position files:
    python src [file1] [file2] -o out.txt
    File list:
    python src -i list.txt -o out.txt
    where list.txt:
    Samples\tfile_path
    or
    file_path
    ''')
    parser.add_argument("Files",nargs="*",default=[],help="files to be combined")
    parser.add_argument(
        "--input_file_list","-i",  
        help='input files list ')
    parser.add_argument("--NumCol","-n",help="which column will be combined")
    parser.add_argument("--out","-o",help="out file name",required=True)
    args = parser.parse_args()
    return args

def ReadFiles(file_name,data,samples,SampleName=None,NumCol=None):
    with open(file_name,'r') as fh:
        headers = fh.readline().strip().split("\t")
        if SampleName is None:
            if NumCol is not None:
                SampleName = headers[NumCol - 1]
                samples.append(SampleName)
            else:
                SampleName = headers
                samples += SampleName
        else:
            samples.append(SampleName)
        for line in fh:
            line = line.strip().split("\t")
            rownames = line.pop(0)
            if NumCol is not None:
                line = line[NumCol - 1]
            for x,y in zip(SampleName,line):
                data[rownames][x] = y

def ReadPositionFiles(files,data,samples,NumCol=None):
    for file in files:
        ReadFiles(file,data,samples,SampleName=None,NumCol=NumCol)

def ReadFileList(file_name,data,samples,NumCol=None):
    with open(file_name,'r') as fh:
        for line in fh:
            line = line.strip().split("\t")
            SampleName = None if len(line)==1 else line.pop(0)
            ReadFiles(line[0],data,samples,SampleName,NumCol)

def Output(data,samples,file_name):
    with open(file_name,'w') as fh:
        rownames = sorted(data)
        header = "\t".join(samples)
        fh.write(f"\t{header}\n")
        for rowname in rownames:
            fh.write(f"{rowname}")
            for sample in samples:
                if sample in data[rowname]:
                    fh.write(f"\t{data[rowname][sample]}")
                else:
                    fh.write(f"\t0")
            fh.write(f"\n")

def main():
    args = ArgumentParser()
    # check input file
    if len(args.Files)==0 and args.input_file_list is None:
        print("InputFileERROR:\n\tAt least one file should be provide")
        sys.exit()
    if args.NumCol is not None:
        args.NumCol = int(args.NumCol)
    # read files from position arguments
    data = defaultdict(dict)
    samples = []
    if len(args.Files)>0:
        ReadPositionFiles(args.Files,data,samples,args.NumCol)
    print(data)
    # read files from a file list
    if args.input_file_list is not None:
        ReadFileList(args.input_file_list,data,samples,args.NumCol)

    # output 
    Output(data,samples,args.out)

if __name__ == "__main__":
    main()