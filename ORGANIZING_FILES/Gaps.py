import os
from pathlib import Path
import re
al = 0
l = []
s=[]
files = []
for folderName, subfolders, filenames in os.walk(f"{Path.home()}/Testing/test"):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print(folderName + ': ' + subfolder)

    for filename in filenames:
        print(folderName + ': '+ filename)
        p=Path(folderName+'/'+filename)
        x = re.compile(r'\d*\d')
        y = x.search(p.stem)
        l.append(y.group())
   
        s.append(p.stem)
        files.append(p.stem)
    print(l)
    l.sort()
    s.sort()
    files.sort()

    for x in range(len(l)):
        b = '{:03}'.format(al+1)
        c = f"{b}"
        if c != l[x]:
            l[x] = c
        s[x] = f"spam{l[x]}"
        os.rename(f"{Path.home()}/Testing/test/{files[al]}.txt",f"{Path.home()}/Testing/test/{s[al]}.txt")
        al += 1
    break
