import json
import csv
import os
from pathlib import Path
from collections import defaultdict



def getLinesofDups(dups):
    linecount = 0
    for dup in dups:
        inst_list  = dup['instances']
        #Go through all instances of the duplication
        current_range = inst_list[0]['lines']
        for p in inst_list:
            range = p['lines']
            #If lower bound of new range is higher than stored upperbound add to sum and set stored value
            if range[0] > current_range[1]:
                linecount += current_range[1] - current_range[0]
                current_range = range
            else:
                #If new upperbound higher than old upperbound update value
                if range[1] > current_range[1]:
                    current_range[1] = range[1]
    return linecount

data = defaultdict(lambda:0)

for filename in os.listdir(r'out'):
    #Load Data
    if filename.endswith(".json"):
        print(filename)
        f=open("out/"+filename,"r",encoding="utf8")
        dups = json.loads(f.read())

        name = os.path.splitext(filename)[0]
        name = name[len("comparison"):]
        versions = name.split(",")
        
        data[versions[0],versions[1]] = getLinesofDups(dups)