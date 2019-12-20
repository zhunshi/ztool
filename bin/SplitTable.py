#!/usr/bin/env python3
import sys
import os
import gzip
import argparse

def ArgumentParser():
    parser = argparse.ArgumentParser(
        prog="SplitTable",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''
    Split Tables to given number of files by rows
    ''')
    parser.add_argument(
        "--input_file","-i",  
        help='input files')
    parser.add_argument("--num_file","-n",type=int,help="number of files to be generated")
    parser.add_argument("--num_line","-l",type=int,help="number of line of files to be generated")
    parser.add_argument("--out_prefix","-o",help="out file prefix",required=True)
    parser.add_argument("--with_header",action="store_true",default=False,help="if with a header")
    args = parser.parse_args()
    return args

def openFile(file_name):
    if file_name.endswith("gz"):
        fh = gzip.open(file_name,'rt')
    else:
        fh = open(file_name,'r')
    return fh

def SplitTable1(file_name,num_line,prefix,withHeader):
    fh_in = openFile(file_name)
    n_file = 0
    if withHeader:
        header = fh_in.readline()
    for line in fh_in:
        n = num_line
        with open(f"{prefix}_{str(n_file)}",'w') as out:
            if withHeader: out.write(header)
            out.write(line)
            while n > 1:
                line = fh_in.readline()
                if len(line)==0: break
                out.write(line)
                n -= 1
        n_file += 1
    fh_in.close()

def SplitTable2(file_name,num_file,prefix,withHeader):
    fh_in = openFile(file_name)
    for i,l in enumerate(fh_in):
        pass
    total_lines = i+1
    if withHeader:
        num_line = (total_lines-1) // num_file + 1
    else:
        num_line = total_lines // num_file + 1
    SplitTable1(file_name,num_line,prefix,withHeader)

def main():
    args = ArgumentParser()
    if args.num_file is not None and args.num_line is not None:
        print("Error: only need one parameter between --num_file and --num_line ")
        sys.exit()
    if args.num_line is not None:
        SplitTable1(args.input_file,args.num_line,args.out_prefix,args.with_header)
    if args.num_file is not None:
        SplitTable2(args.input_file,args.num_file,args.out_prefix,args.with_header)

if __name__ == "__main__":
    main()