#!/usr/bin/env python
import sys
import os

def PickingDone(myfile):
    out = []
    with open(myfile,'r') as fh:
        for line in fh:
            line = line.rstrip()
            if line.endswith("is finished!"):
                tmp = line.split()
                if tmp[0] not in out:
                    out.append(tmp[0])
    return out

def PickingMatrix(mydir,mydone,out_name):
    out = {}
    myfiles = os.listdir(mydir)
    myfiles = [x for x in myfiles if x.endswith("sh")]
    myfiles = [x for x in myfiles if x not in mydone]
    with open(out_name,'w') as fh_out:
        for myfile in myfiles:
            with open(os.path.join(mydir,myfile),'r') as fh_in:
                for line in fh_in:
                    if not line.rstrip().endswith("this-work-is-complete"):
                        fh_out.write(line)

def main():
    if len(sys.argv)!=4:
        print("Usage:")
        print(f"python {sys.argv[0]} [log file] [qsub_dir] [out]")
        sys.exit()
    logFile = sys.argv[1]
    doneSam = PickingDone(logFile)
    print(f"{len(doneSam)}")
    PickingMatrix(sys.argv[2],doneSam,sys.argv[3])

if __name__ == "__main__":
    main()