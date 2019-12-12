#!/usr/bin/env python
import sys
import os
import re

def PickingDone(myfile):
    out = {}
    with open(myfile,'r') as fh:
        for line in fh:
            line = line.rstrip()
            if line.endswith("is finished!"):
                tmp = line.split()
                #tmp2 = tmp[0].split("_")
                res = re.search(r"(.*?)_([1234])_\d+\.sh",tmp[0])
                if not res:
                    print ("ERROR")
                    sys.exit(1)
                samID = res.group(1)
                step = res.group(2)
                if samID not in out:
                    out[samID] = [step]
                elif step not in out[samID]:
                    out[samID].append(step)
    return out

def PickingMatrix(myfile):
    out = {}
    with open(myfile,'r') as fh:
        for line in fh:
            line = line.rstrip()
            tmp = line.split()
            samName = tmp[0].split("=")[1]
            ids = tmp[1].split("=")[1]
            if samName not in out:
                out[samName] = {}
            out[samName][ids] = line
    return out

def undoneGenerate(mydone,mymatrx):
    out_fh = open("ReRUN.matrix",'w')
    for key1 in mymatrx:
        if key1 in mydone:
            for key2 in mymatrx[key1]:
                if key2 not in mydone[key1]:
                    out_fh.write(f"{mymatrx[key1][key2]}\n")
        else:
            for key2 in mymatrx[key1]:
                out_fh.write(f"{mymatrx[key1][key2]}\n")
    out_fh.close()

def main():
    if len(sys.argv)!=3:
        print("Usage:")
        print(f"python {sys.argv[0]} [log file] [matrix]")
        sys.exit()
    logFile = sys.argv[1]
    doneSam = PickingDone(logFile)
    print(f"{len(doneSam.keys())}")
    matrx = PickingMatrix(sys.argv[2])
    print(f"{len(matrx.keys())}")
    undoneGenerate(doneSam,matrx)

if __name__ == "__main__":
    main()
