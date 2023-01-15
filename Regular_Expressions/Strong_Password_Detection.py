import re


password = '@1njneiefAiefni'
com = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[#?!@$%^&*-]).{8,}$')
ans = com.findall(password)
print(ans)