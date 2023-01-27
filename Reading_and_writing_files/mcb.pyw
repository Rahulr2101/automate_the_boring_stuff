import shelve
import sys
import pyperclip

mcb_sh = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_sh[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcb_sh.keys())))
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'deleteall':
    for words in list(mcb_sh.keys()):
        del mcb_sh[words]
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_sh[sys.argv[2]]
mcb_sh.close()
