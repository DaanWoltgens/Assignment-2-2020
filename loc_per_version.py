import subprocess
import os

def version_to_int(version):
    subversions = version.split('.')
    if len(subversions) > 4:
        print("Cannot sort version number:", version)
        exit(0)
    versionsum = 0
    for i in range(len(subversions)):
        versionsum += int(subversions[i]) * 10 ** (6 - 2 * i)
    return versionsum
        

versions = [name for name in os.listdir(".") if os.path.isdir(name)]
versions.sort(key=version_to_int)

csv = ''
for version in versions:
    result = subprocess.run(['cloc', '--exclude-ext=json', '--csv', '--quiet', f'./{version}/src'], stdout=subprocess.PIPE) # cloc --exclude-ext=json ./src --csv --quiet
    result_str = result.stdout.decode('utf8')
    js_info = result_str.split('\n')[2].split(',')
    loc = int(js_info[4]) + int(js_info[3]) + int(js_info[2])
    print(f'{version},{loc}')