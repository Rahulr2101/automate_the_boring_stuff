import os
from pathlib import Path

for folderName, subfolders, filenames in os.walk(f'{Path.home()}/Testing'):

    for filename in filenames:
        if os.path.getsize(f'{folderName}/{filename}')> 100000000:
            print('Exceptionally Large File:' + folderName + ': '+ filename)
            print("Size:",int(os.path.getsize(f'{folderName}/{filename}')/1000000),'MB')

    print()