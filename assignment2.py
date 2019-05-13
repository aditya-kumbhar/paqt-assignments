# read input file
inFile = open("input.txt",'r')

# dictionary to store frequency count of words
freq = {}

for line in inFile:
	for word in line.split():
		if(word.lower() in freq):
			freq[word.lower()]+=1	#increment if word already exists in dictionary (convert to lower case first)
		else:
			freq[word.lower()]=1		#initialise with 1 if word does not exist

from collections import OrderedDict

#Sort the dictionary of freq counts by key
od = OrderedDict(sorted(freq.items()))

#Open output file to store result
outFile = open("output.txt",'w')

#Write to output file
for key in od:
	outFile.write(key+','+str(od[key])+'\n')

