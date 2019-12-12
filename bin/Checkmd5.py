#!/usr/bin/env python
import sys,os
import argparse

def ArgumentParser():
    parser = argparse.ArgumentParser(
        description='correctness checking between two md5 files')
    parser.add_argument("--source","-s",required=True,help="md5 file for source data")
    parser.add_argument("--target","-t",required=True,
        help="md5 file for target data.\nFiles not in the file will be ignored")
    parser.add_argument("--out","-o",required=True,help="output file")
    args = parser.parse_args()
    return args

def Readfiles(file_name):
    out = {}
    with open(file_name,'r') as fh:
        for line in fh:
            tmp = line.rstrip().split()
            tmp2 = tmp[-1].split("/")
            if tmp2[-1] not in out:
                out[tmp2[-1]] = tmp[0]
            else:
                print("Error1")
                sys.exit()
    return out

def comparison(dat1,dat2,out_name):
    n_all, n_done, n_fail, n_nofound = 0, 0, 0, 0
    with open(out_name,'w') as fh:
        for i in dat2:
            n_all += 1
            if i in dat1:
                if dat1[i]==dat2[i]:
                    n_done += 1
                    fh.write(f"{i}\t{dat1[i]}\t{dat2[i]}\tOK\n")
                else:
                    n_fail += 1
                    fh.write(f"{i}\t{dat1[i]}\t{dat2[i]}\tNO\n")
            else:
                n_nofound += 1
    if n_all == n_done:
        print("All files are OK\n\nDetail information:")
    print(f"\tAll md5 files: {n_all}")
    print(f"\tDone: {n_done}")
    print(f"\tFail: {n_fail}")
    print(f"\tNot found: {n_nofound}")

def main():
    args = ArgumentParser()
    file_name1,file_name2,out = sys.argv[1:]
    dat1 = Readfiles(file_name1)
    dat2 = Readfiles(file_name2)

    comparison(dat1,dat2,out) 
if __name__ == "__main__":
    main()
