
#!/usr/bin/env python
import os
import sys
import argparse

def ArgumentParser():
    parser = argparse.ArgumentParser(
        prog="Split.metaphlan2.profile",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Split metaphlan2 profile into every clssification")
    parser.add_argument("--profile","-p",type=int,help="combined metaphlan2 profile")
    parser.add_argument("--rank","-r",choices=list("akpcofgs"),default="a",help="select a rank, default all rank")
    parser.add_argument("--out_prefix","-o",help="prefix of out file name")
    parser.add_argument("--ignore_eukaryon",action='store_true',help="ignore eukaryon,default=False")
    parser.add_argument("--ignore_virus",action='store_true',help="ignore virus,default=False")
    args = parser.parse_args()
    return args

def Split(filename,rank,out,if_virus=False,if_euk=False):
    outname = f"{out}.{rank}.profile.txt"
    with open(filename,'r') as f1,open(outname,'w') as f2:
        header = f1.readline()
        f2.write(header)
        for line in f1:
            if line.startswith("#"): continue
            tmp = line.rstrip().split("\t")[0]
            tmp = tmp.split("|")[-1]
            if not tmp.startswith(f"{rank}__"): continue
            if if_viurs and line.startswith("k__virus"): continue
            if if_euk and line.startswith("k__eukary"): continue
            f2.write(line)

def main():
    args = ArgumentParser()

    ranks = args.rank if "a" not in args.rank else "kpcofgs"
    for r in ranks:
        Split(args.profile,r,args.out_prefix,args.ignore_eukaryon,args.virus)

if __name__ == "__main__":
    main()

