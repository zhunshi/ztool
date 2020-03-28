#!/usr/bin/env python
import sys
import os
import gzip

def FastqSpliter(filename,filenumber,nLine):
    with gzip.open(fq,'rt') as f:
        n_reads = nLine
        out = gzip.open(f"{out_dir}/split.{filenumber}.gz",'wt')
        for line in f:
            if n_reads == 0:
                out.close()
                n_reads = n
                filenumber += 1
                out = gzip.open(f"{out_dir}/split.{filenumber}.gz",'wt')
            if not line.startswith("@"):
                print("ERROR")
                sys.exit()
            seq = f.readline()
            p = f.readline()
            q = f.readline()
            out.write(f"{line}{seq}{p}{q}")
            n_reads = n_reads - 1
        out.close()
    return filenumber

def Process(filename,n,out_dir):
    lst = default
    with open(filename,'r'):
        a

def main():
    fqlst, n, out_dir = sys.argv[1:]

    out_dir = os.path.abspath(out_dir)
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    Process(fqlst,n,out_dir)