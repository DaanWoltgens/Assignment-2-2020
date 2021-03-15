import json
import csv
import os
from pathlib import Path
from collections import defaultdict



def getLinesofDups(dups):
    ranges = []
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
                ranges.append(line)

    #Can be overlapping ranges
    linecount = 0
    current_range = [0,0]
    for range in sorted(ranges):
        #If lower bound of new range is higher than stored upperbound add to sum and set stored value
        if range[0] > current_range[1]:
            linecount += current_range[1] - current_range[0]
            current_range = range
        else:
            #If new upperbound higher than old upperbound update value
            if range[1] > current_range[1]:
                current_range[1] = range[1]
    linecount += current_range[1] - current_range[0]
    return linecount

data = defaultdict(lambda:0)

for filename in os.listdir(r'out'):
    #Load Data
    if filename.endswith(".json"):
        f=open("out/"+filename,"r",encoding="utf8")
        dups = json.loads(f.read())

        name = os.path.splitext(filename)[0]
        name = name[len("comparison"):]
        versions = name.split(",")
        
        data[versions[0],versions[1]] = getLinesofDups(dups)

f = open("duplications.csv", "w") 

f.write(', '.join(("v1", "v2", "dup lines", "len_v1", "len_v2", "measure")) + "\n")

with open('loc.csv', mode='r') as infile:
    reader = csv.reader(infile)
    loc = {rows[0]:rows[1] for rows in reader}

for key in sorted(data):
    f.write(', '.join(key) + ", " + str(data[key]) +  ", " + str(loc[key[0]]) + ", "+ str(loc[key[1]]) + ", " + str(data[key] / max(int(loc[key[0]]), int(loc[key[1]]))) + "\n")