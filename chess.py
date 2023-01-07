from copy import deepcopy
import re

def runRegex(pattern, context):
    txtRegex = re.compile(pattern)
    mO = txtRegex.search(context)
    try:
        match = mO.group()
        return True
    except (AttributeError, UnboundLocalError):
        print("", end = "")
        
board = {
   "a": ["Rw", "Nw", "Bw", "Qw","Kw", "Bw", "Nw", "Rw"],
   "b": ["Pw", "Pw", "Pw", "Pw","Pw", "Pw", "Pw", "Pw"],
   "c": ["  ", "  ", "  ", "  ","  ", "  ", "  ", "  "],
   "d": ["  ", "  ", "  ", "  ","  ", "  ", "  ", "  "],
   "e": ["  ", "  ", "  ", "  ","  ", "  ", "  ", "  "],
   "f": ["  ", "  ", "  ", "  ","  ", "  ", "  ", "  "],
   "g": ["Pb", "Pb", "Pb", "Pb","Pb", "Pb", "Pb", "Pb"],
   "h": ["Rb", "Nb", "Bb", "Qb","Kb", "Bb", "Nb", "Rb"] }
alc = "abcdefgh"    

def makeMove(moves, grid):
    positions = moves.split(" ")
    fro = positions[0]
    to = positions[1]
    new = grid[fro[0]][int(fro[1])-1]
    grid[fro[0]][int(fro[1])-1] = "  "
    grid[to[0]][int(to[1])-1] = new
     
def printBoard(grid):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    print("   1","2","3","4","5","6","7","8", sep= " "*4)
    for char in letters:
        print("-"*40, " |", sep="")
        print(f"{char}| {grid[char][0]} | {grid[char][1]} | {grid[char][2]} | {grid[char][3]} | {grid[char][4]} | {grid[char][5]} | {grid[char][6]} | {grid[char][7]} |")
    print("-"*40, " |", sep="")
    print()
    print()

def delFunc(list, movement):
    del list[-1]
    sct = list[-1].split()
    sct2 = " ".join([sct[1], sct[0]])
    del list[-1]
    list.append(sct2)
     
def pawn(moves):
    fro = moves.split()[0] 
    to = moves.split()[1]
    if fro[1] == to[1]: 
        if fro[0] =="b":
            if not runRegex(r"[c|d]", to[0]):
                print("INVALID MOVE")
            else:
                print("moved")
                try:
                    makeMove(moves, board)
                except IndexError:
                    print("INVALID MOVE!")
        else:
            if not runRegex(fr"{chr(ord(fro[0])+1)}", to[0]):
                print("INVALID MOVE")
            else:
                print("moved")
                try:
                    makeMove(moves, board)
                except IndexError:
                    print("INVALID MOVE!")
    else:
        print("INVALID MOVE")
    
def rook():
    print("rook")
        
def pieceChecker(moves, grid):
    fro = moves.split()[0]    
    piece = grid[fro[0]][int(fro[1])-1][0]
    if piece == "P":
        pawn(moves)
    elif piece == "R":
        rook()
    elif piece == "N":
        knight()       
    elif piece == "Q":
        queen()
    elif piece == "B":
        bishop()
    elif piece == "K":
        king()
        
                               
moveList = []            
while True:   
    printBoard(board)                      
    move = input("make a move>> ").lower()
    moveList.append(move)
    if move == "del":
        delFunc(moveList, move)
        move = moveList[-1]            
        makeMove(move, board) 
    try:
        pieceChecker(move, board)
    except KeyError:
        print("INVALID MOVE")