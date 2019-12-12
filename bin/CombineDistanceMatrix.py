#!/usr/bin/env python
import sys,os

def Readresults(pth,mydis):
	with open(pth,'r') as f:
		headers = f.readline().rstrip().split("\t")[1:]
		for j in f:
			tmp = j.rstrip().split("\t")
			line_name = tmp.pop(0)
			if not line_name in mydis:
				mydis[line_name] = {}
			for x,y in zip(tmp,headers):
				if y in mydis[line_name]:
					if mydis[line_name][y] != x:
						sys.exit("ERROR:1")
				else:
					mydis[line_name][y] = x
	return(mydis)

def ReadData(file_name):
    disT = {}
	for i in open(file_name,'r'):
    	line = i.rstrip()
	nm = line.split("/")[-1]
	disT = Readresults(line,disT)
    return distT

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
    dis_lst, out = sys.argv[1:]
    data = ReadData(dis_lst)
	Output(out,data)

if __name__ == '__main__':
    main()
	