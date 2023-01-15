import pyinputplus as pl
totalCost = 0

cost = {'wheat':2,'white':1,'sourdough':3,'chicken':4,'turkey':6,'ham':5,'tofu':5,'Cheddar':2,'Swiss':3,'mozzarella':5,'mayo':1,
            'mustard': 2,'lettuce': 3,'tomato':2}


breadtype = pl.inputMenu(['wheat','white','sourdough'],prompt='Select the type of bread you want for Sandwich \n')
totalCost += cost[breadtype]

protein = pl.inputMenu(["chicken",'turkey','ham','tofu'],prompt='Select the type of protein\n')
totalCost += cost[protein]

cheese = pl.inputYesNo('Do you want cheese in your sandwich?(Yes/No)?\n')
if cheese == 'Yes':
    cheeseType = pl.inputMenu(['Cheddar','Swiss','mozzarella'],prompt='Which type of cheese do you want? \n')
mayo = pl.inputYesNo('Do you want mayo?(Yes/No) \n')
if mayo == 'yes':
    totalCost += cost['mayo']
mustard = pl.inputYesNo('Do you want mustard?(Yes/No) \n')
if mayo == 'yes':
    totalCost += cost['mustard']
lettuce = pl.inputYesNo('Do you want lettuce?(Yes/No) \n')
if mayo == 'yes':
    totalCost += cost['lettuce']
if lettuce == 'no':
    tomato = pl.inputYesNo('Do you want tomato?(Yes/No) \n')
    totalCost += cost['tomato']
numberSandwiches = pl.inputInt('How many sandwiches do you want?\n', min = 1)
print('Total cost =',totalCost*numberSandwiches)