def isvalidChessBoard(chess_board):
    l =  list(chess_board.keys())
    lp =  list(chess_board.values())
    lw =[]
    lb =[]
    position = []
    a = 97
    for y in range(8):
        for x in range(1,9):
            position.append(str(x)+chr(a))
        a += 1
    for x in l:
        for y in position:
            if x == y:
                valid = True
                break
        else:
            break       
    if valid:
        for x in lp:
            if x[0] == 'w':
                lw.append(x)
            else:
                lb.append(x)
        if len(lw) == 16 and len(lb) == 16:
                if lw.count("wking") == 1:
                    valid = True
                else:
                    return False
                if lw.count("wpawn") == 8:
                    valid = True
                else:
                    return False
                if lb.count("bking") == 1:
                    valid = True
                else:
                    return False
                if lb.count("bpawn") == 8:
                    valid = True
                else:
                    return False
                return True
        else:
            return False
              

    
            





chess_board = {
    "1a": "wrook", "1b": "wknight", "1c": "wbishop", "1d": "wqueen",
    "1e": "wking", "1f": "wbishop", "1g": "wknight", "1h": "wrook",
    "2a": "wpawn", "2b": "wpawn", "2c": "wpawn", "2d": "wpawn",
    "2e": "wpawn", "2f": "wpawn", "2g": "wpawn", "2h": "wpawn",
    "8a": "brook", "8b": "bknight", "8c": "bbishop", "8d": "bqueen",
    "8e": "bking", "8f": "bbishop", "8g": "bknight", "8h": "brook",
    "7a": "bpawn", "7b": "bpawn", "7c": "bpawn", "7d": "bpawn",
    "7e": "bpawn", "7f": "bpawn", "7g": "bpawn", "7h": "bpawn",    
}
print(isvalidChessBoard(chess_board))