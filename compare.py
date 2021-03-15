import os
from concurrent.futures import ThreadPoolExecutor

def version_to_int(version):
    subversions = version.split('.')
    if len(subversions) > 4:
        print('Cannot sort version number:', version)
        exit(0)
    versionsum = 0
    for i in range(len(subversions)):
        versionsum += int(subversions[i]) * 10 ** (6 - 2 * i)
    return versionsum
        

versions = [name for name in os.listdir('.') if os.path.isdir(name)]
versions.sort(key=version_to_int)
combinations = []
executor = ThreadPoolExecutor(max_workers=8)

for i in range(len(versions)):
    for j in range(len(versions)):
        if j > i:
            combinations.append([versions[i], versions[j]])
            executor.submit(os.system(f'jsinspect -t 50 -I -r json ./{versions[i]}/src ./{versions[j]}/src > ../../out/comparison{versions[i]},{versions[j]}.json'))