import re
sen =input('Enter Date in DD/MM/YYYY: ')
com = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
fin = com.findall(sen)
ans = True

for day,month,year in fin:
    day = int(day)
    month = int(month)
    year = int(year)

    if(month == 4 or month == 6 or month ==9 or month == 11):
        if day == 31:
            print("Invalid Date")
            ans = False
    elif month == 2:
        if year%4 == 0:
            if day > 30:
                print('Invalid Date')
                ans = False
        else:
            if day > 29:
                print('Invalid Date')
                ans = False
    if ans:
        print("Valid date")