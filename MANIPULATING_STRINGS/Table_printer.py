    
def printTable(tableData):
    col= [0] * len(tableData)
    for i in range(len(tableData)):
        col[i] = len(max(tableData[i], key=len))
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(col[y]), end=' ')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David',],
                ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)