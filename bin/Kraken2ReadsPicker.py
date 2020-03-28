#!/usr/bin/env python
import sys
import os
import re
from collections import defaultdict

def ReadReport(filename):
    res = {}
    bacteria = False
    with open(filename,'r') as f:
        for line in f:
            line = line.rstrip().split("\t")
            taxID = line[4]
            taxName = line[5].strip()
            if bacteria and line[3] == "D": break
            if taxName == "Bacteria": 
                bacteria = True
            if not bacteria: continue
            if taxID not in res:
                res[taxID] = taxName
            else:
                print("ERROR1")
                sys.exit()
    return res

def Kraken2ReadsPicker(db,infile,outfile):
    with open(infile,'r') as f1, open(outfile,'w') as f2:
        for line in f1:
            if line.startswith("U"): continue
            line = line.rstrip().split("\t")
            tt = re.search("\(taxid (\d+)\)",line[2])
            if tt:
                if tt.group(1) in db:
                    f2.write(f"{line[1]}\n")
            else:
                print(f"ERROR in search:\t{line[2]}")
                sys.exit()

def main():
    if len(sys.argv) != 4:
        print("ERROR in arg number")
        sys.exit()
    f_report, f_kraken2, f_out = sys.argv[1:]

    db = ReadReport(f_report)
    Kraken2ReadsPicker(db,f_kraken2,f_out)


if __name__ == "__main__":
    main() 
