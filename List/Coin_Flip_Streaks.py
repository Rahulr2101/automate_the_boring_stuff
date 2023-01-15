import random
numberOfStreaks = 0
count = 0
for experimentNumber in range(1000):
    com = [ random.randint(0,1) for x in range(100)]
    # Code that creates a list of 100 'heads' or 'tails' values.
    for x in range(100):
        if x  == 0:
            continue
        elif com[x] == com[x-1]:
            count += 1
        else:
            count  = 0
        if count == 6:
            count = 0
            numberOfStreaks += 1
            
       
   # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))