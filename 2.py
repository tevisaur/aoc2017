import csv
import math

numbers

checksum=0

with open('2input.tsv') as numberfile:
	numberfilereader = csv.reader(numberfile,delimiter='\t',quoting=csv.QUOTE_NONNUMERIC)
	for row in numberfilereader:
		highest=-math.inf
		lowest=math.inf
		for column in row:
			if column>highest:
				highest=column
			if column<lowest:
				lowest=column
		checksum+=(highest-lowest)