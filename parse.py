import json
import csv
from pathlib import Path
from collections import defaultdict

#Load Data
f=open("output_type1.json","r",encoding="utf8")
dups = json.loads(f.read())

count = defaultdict(lambda:[])


for dup in dups:
    inst_list  = dup['instances']
    #Go through all instances of the duplication
    for p in dup['instances']:
        version1 = Path(p['path']).parts[0]
        #For each instance go through the list of all other instances
        for i in inst_list:
            version2 = Path(i['path']).parts[0]
            #Add code range to list
            line = p['lines']
            count[version1,version2].append(line)

#Can be overlapping ranges
linecount = defaultdict(lambda:0)
for key in sorted(count):
    #Keep track of current range
    current_range = sorted(count[key])[0]
    for range in sorted(count[key]):
        #If lower bound of new range is higher than stored upperbound add to sum and set stored value
        if range[0] > current_range[1]:
            linecount[key] += current_range[1] - current_range[0]
            current_range = range
        else:
            #If new upperbound higher than old upperbound update value
            if range[1] > current_range[1]:
                current_range[1] = range[1]

f = open("type1.csv", "w") 

f.write(', '.join(("v1", "v2", "dup lines", "v1_lines", "v2_lines", "measure")) + "\n")

with open('loc.csv', mode='r') as infile:
    reader = csv.reader(infile)
    loc = {rows[0]:rows[1] for rows in reader}

for key in sorted(linecount):
    f.write(', '.join(key) + ", " + str(linecount[key]) +  ", " + loc[key[0]] + ", "+ loc[key[1]] + ", " + str(linecount[key] / (int(loc[key[0]]) + int(loc[key[1]]))) + "\n")
        