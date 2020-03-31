#!/usr/bin/env python

def ListCommands():
    commands = r'''
Current available commands:

Checkmd5 :              correctness checking between two md5 files
CombineDistanceMatrix : Combine distance tables (Big data distance)
CombineTables :         Combine any two or more files by rows
FileNumberStat:         Statistic file number in a given directory and its subdirectories
init:                   init a script frame
kraken2profile:         Transfer kraken2 output to a tidy profile
Kraken2ReadsPicker:     Pick given list of reads from kraken2 output
TaxaRichness :          Calculate taxa richness (eg. gene richness)
RerunGeneral :          Re-submit scripts undone
RerunPipeline :         Re-submit scripts undone (in cOMG pipeline)
SpliceCombine :         Splice big data to specific number and combinie between any two
SplitMetaphlanProfile:  Splice metaphlan profile into seperate files with only one rank
SplitTable:             Split Tables to given number of files by rows

type 'ztool {command} -h' for detail information
'''
    print(commands)

def main():
    ListCommands()
if __name__ == "__main__":
    main()
    
