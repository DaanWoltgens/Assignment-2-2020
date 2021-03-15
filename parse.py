import json
from pathlib import Path
from collections import defaultdict

#Load Data
f=open("output_type1.json","r",encoding="utf8")
dups = json.loads(f.read())

d = defaultdict(lambda:0)


for dup in dups:
    inst_list  = dup['instances']
    #Go through all instances of the duplication
    for p in dup['instances']:
        version1 = Path(p['path']).parts[0]
        #For each instance go through the list of all other instances
        for i in inst_list:
            version2 = Path(i['path']).parts[0]
            #Iterate counter
            d[version1,version2] += 1

f = open("type1.txt", "w") 

for key in sorted(d):
    f.write(', '.join(key) + ", " + str(d[key]) + "\n")
        