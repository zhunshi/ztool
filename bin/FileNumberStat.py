#!/usr/bin/env python3
import sys
import os
import argparse
from collections import defaultdict

def ArgumentParser():
    parser = argparse.ArgumentParser(
        description='Statistic file number in a given directory and its subdirectories')
    parser.add_argument("--dir","-d",  help='give a directory', required=True)
    parser.add_argument("--out","-o",help="output name")
    parser.add_argument("--maxdepth","-m",help="max depth directory query")
    args = parser.parse_args()
    return args

def DirectoryParser(path,maxdepth):
    out = defaultdict(lambda : 0)
    for root, dirs, files in os.walk(path):
        nFiles = len(files)
        out[root] += nFiles
        out[path] += nFiles
    return out

def output(dat, file_name):
    with open(file_name,'w') as fh:
        for key in sorted(dat.keys()):
            fh.write(f"{key}\t{dat[key]}\n")

def main():
    args = ArgumentParser()
    
    data = DirectoryParser(args.dir,args.maxdepth)
    output(data,args.output)

if __name__ == '__main__':
    main()
    