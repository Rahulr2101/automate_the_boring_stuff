import time
import random


def cal(sttime,a,b,count):
    sttime = time.strftime("%s")
    ans=int(input(f'{a} x {b} = '))
    if ans == a*b and int(int(time.strftime("%s"))- int(sttime) ) <= 8:
        print('Correct!')
        time.sleep(1)
        return
    if int(int(time.strftime("%s"))- int(sttime) ) >8:
        print("incorrect")
        return

    elif count  == 2:
        print("incorrect")
        return
    else:
        count += 1
        cal(sttime,a,b,count)
        


count = 0
sttime = time.time()
for null in range(11):
    sttime = 0
    a = random.randint(0,9)
    b = random.randint(0,9)
    cal(sttime,a,b,count)

