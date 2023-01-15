import os
from pathlib import Path
import shutil

print(Path.home())
for folderName, subfolders, filenames in os.walk(Path.home()/'Testing'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        p =Path(folderName +':'+filename)
        print(p.suffix)
        if not os.path.exists(f'{folderName}/New_Folder'):
            os.makedirs(f'{folderName}/New_Folder')
        print(f'{filename}')
        if p.suffix == '.png'or p.suffix == '.pdf':
            print(f'{Path.home()}/Testing/New_Folder') 
            shutil.copyfile(f'{folderName}/{filename}',f'{Path.home()}/Testing/New_Folder/{filename}')
    break