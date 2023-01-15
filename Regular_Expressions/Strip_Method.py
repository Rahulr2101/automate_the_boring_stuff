import re
sen =input()
arg1 = input()
com = re.compile(r'\w*\w')
ans = com.findall(sen)
x = ans.count(arg1)
if arg1 != '' and x != 0:
    ans.remove(arg1)

print(' '.join(ans))