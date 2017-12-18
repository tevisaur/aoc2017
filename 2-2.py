import csv
import math

numbers

checksum=0

with open('2input.tsv') as numberfile:
	numberfilereader = csv.reader(numberfile,delimiter='\t',quoting=csv.QUOTE_NONNUMERIC)
	for row in numberfilereader:
		foundit=False
		while not foundit:
			for columnindex, columnvalue in enumerate(row):
				for jumper in range(len(row)):
					if jumper!=columnindex and row[jumper]>=columnvalue:
						if int(row[jumper]) % int(columnvalue) == 0:
							checksum+=( int(row[jumper]) / int(columnvalue) )
							foundit=True

