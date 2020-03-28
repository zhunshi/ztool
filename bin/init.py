#!/usr/bin/env python3
import sys
import os
import argparse

def ArgumentParser():
    parser = argparse.ArgumentParser(
        prog="init a null scripts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''
    init a null scripts
    ''')
    parser.add_argument(
        "--output","-o",  
        help='output scripts')
    args = parser.parse_args()
    return args

temp = r'''
#!/usr/bin/env python
import os
import sys
import argparse

def ArgumentParser():
    parser = argparse.ArgumentParser(
        prog="temp",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="xxx")
    parser.add_argument(
        "--input_file","-i",  
        help='input files')
    parser.add_argument(
        "--output_file","-o",  
        help='output files')
    parser.add_argument("--xx","-n",type=int,help="xxx")
    parser.add_argument("--xx","-l",type=int,help="xxx")
    #parser.add_argument("--xx",action="store_true",default=False,help="xx")
    args = parser.parse_args()
    return args

def main():
    args = ArgumentParser()

    #xxx

if __name__ == "__main__":
    main()

'''

def main():
    args = ArgumentParser()

    out = args.output
    with open(out,'w') as f:
        f.write(temp)

if __name__ == "__main__":
    main()