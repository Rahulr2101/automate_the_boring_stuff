import re
import os
from pathlib import Path
search  = input("Enter the string: ")
for filename in os.listdir(os.getcwd()):
    f = open(f"{Path.home()}/git/automate_the_boring_stuff/Reading_and_writing_files/files/{filename}","r")
    sent = f.readline()

    match = re.compile(search)
    match_obj = match.findall(sent)
    if len(match_obj) != 0:
        print(f"Find sentense in {os.listdir(os.getcwd())[0]} =",match_obj)

