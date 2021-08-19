from project0_funs import *

myBoard = loadBoard("test.txt")
printBoard(myBoard) 
print(possibleMoves((0,0), myBoard))
print(possibleMoves((2,2), myBoard))
legalMoves(possibleMoves((2,2),myBoard), ((0,0),(1,1),(2,2),(3,3)))

myDict = open('myDict.txt', "r")
examineState(myBoard,(0,0),((1,1),(1,0)), myDict)
examineState(myBoard, (1,0), ((2,2),(2,1),(1,1)), myDict)
examineState(myBoard,(3,1),((0,1),(1,0),(1,1),(2,1)), myDict)
myDict.close()