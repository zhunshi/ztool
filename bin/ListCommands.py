#!/usr/bin/env python

def ListCommands():
    commands = r'''
Current available commands:

Checkmd5 :              correctness checking between two md5 files
CombineDistanceMatrix : Combine distance tables (Big data distance)
CombineTables :         Combine any two or more files by rows
TaxaRichness :          Calculate taxa richness (eg. gene richness)
RerunGeneral :          Re-submit scripts undone
RerunPipeline :         Re-submit scripts undone (in cOMG pipeline)
SpliceCombine :         Splice big data to specific number and combinie between any two

type 'ztool {command} -h' for detail information
'''
    print(commands)

def main():
    ListCommands()
if __name__ == "__main__":
    main()
    