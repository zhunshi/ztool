#!/usr/bin/env python
import sys,os
import argparse
from collections import defaultdict

def ArgumentParser():
    parser = argparse.ArgumentParser(
    prog="CombineDistanceTables",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
    Combine distance from distinct files,
    always follow the scripts SpliceCombine.py
    steps:
        1. python SpliceCombine.py -i Profile -n 100
        2. run every scripts
        3. python CombineDistanceTables.py -i ListFile -o out.txt
    ''')
    parser.add_argument(
        "--input_file_list","-i",  
        help='input files list ')
    parser.add_argument("--out","-o",help="out file name",required=True)
    args = parser.parse_args()
    return args

def Readresults(pth,mydis):
    with open(pth,'r') as f:
        headers = f.readline().strip().split("\t")
        for j in f:
            tmp = j.rstrip().split("\t")
            line_name = tmp.pop(0)
            for x,y in zip(tmp,headers):
                if y in mydis[line_name]:
                    if mydis[line_name][y] != x:
                        sys.exit("ERROR:1")
                else:
                    mydis[line_name][y] = x
    return(mydis)

def ReadData(file_name):
    disT = defaultdict(dict)
    with open(file_name,'r') as fh:
        for i in fh:
            line = i.rstrip()
            nm = line.split("/")[-1]
            Readresults(line,disT)
    return disT

def Output(file_name,data):
    with open(file_name,'w') as f:
        keys1 = list(data.keys())
        f.write("\t"+"\t".join(keys1)+"\n")
        for x in data:
            f.write(x)
            for y in keys1:
                try:
                    f.write("\t"+data[x][y])
                except:
                    f.write("\tNA")
                    print("There are some miss value")
            f.write("\n")

def main():
    args = ArgumentParser()
    dis_lst = args.input_file_list
    out = args.out
    data = ReadData(dis_lst)
    Output(out,data)

if __name__ == '__main__':
    main()
	