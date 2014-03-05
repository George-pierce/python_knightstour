import time
import sys

class Board():
    gameBoard = None
    currentPositionChar = 'K'
    visitedPositionChar = 'K'

    def __init__(self,boardSize):
        self.gameBoard = [[0 for x in xrange(boardSize)] for x in xrange(boardSize)]
     
    def resetPosition(self, rowIndex,columnIndex):
        if self.isPositionOnBoard(rowIndex,columnIndex):
            self.gameBoard[rowIndex][columnIndex] = 0       

    def setPosition(self, rowIndex, columnIndex,stepInterval):
        if self.isPositionOnBoard(rowIndex,columnIndex):
            self.gameBoard[rowIndex][columnIndex] = self.visitedPositionChar
            
    def printBoard(self):
        print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in self.gameBoard]))

    def isValidMove(self,row,column):
       # Is move on gameBoard?
       if not self.isPositionOnBoard(row,column):
           return False        
       #is move still valid, ie not traversed already
       if self.gameBoard[row][column] != 0:
           return False
       return True

    def isPositionOnBoard(self,row,column):
       if (row < 0) or (column < 0) or (row > len(self.gameBoard) - 1) or (column > len(self.gameBoard) - 1):
           return False 
       return True

    def successfulTraversal(self):
         for row in range(len(self.gameBoard)):
            for column in range(len(self.gameBoard[row])):
                if str(self.gameBoard[row][column]) == '0':
                    return False
         return True


class KnightsTour():
    boardSize = 8
    knightsMoves = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
    playersBoard = None

    def __init__(self,boardSize):
        self.initialize(boardSize)

    def initialize(self,boardSize):
        self.boardSize = boardSize     
        self.playersBoard = Board(boardSize)

    def printBoard(self):
        self.playersBoard.printBoard()

    def runSimulation(self,startingRow,startingColumn,stepInterval):
        
        validMove = self.playersBoard.isValidMove(startingRow,startingColumn)
        if validMove:
            #Update the board with new position                    
            self.playersBoard.setPosition(startingRow,startingColumn,1)
            #self.printBoard()
            #Check if we finished the Tour
            if self.playersBoard.successfulTraversal():
                print "We won!!" 
                self.printBoard()
                time.sleep(50)
        else:
            return              
            
        currentStep =stepInterval+1
        for indexRow,indexColumn in self.knightsMoves:
            newPosition_Row = startingRow + indexRow 
            newPosition_Column = startingColumn + indexColumn           
            if self.playersBoard.isValidMove(newPosition_Row,newPosition_Column):
                 self.runSimulation(newPosition_Row,newPosition_Column,currentStep)
                 self.playersBoard.resetPosition(newPosition_Row,newPosition_Column)
            
       # print "Backtracking from current Position", startingRow, startingColumn, "\n"
        self.playersBoard.resetPosition(startingRow,startingColumn)
               
        
boardSize = 8

Tour = KnightsTour(boardSize)
Tour.printBoard()
sys.setrecursionlimit(5000)
startingRow = -1
startingColumn = -1

while (startingRow < 0 or startingRow > boardSize) or (startingColumn < 0 or startingColumn > boardSize):
    startingRow = int(raw_input('Enter your starting position: (Row # 1-8) ')) - 1
    startingColumn = int(raw_input('Enter your starting position: (Column # 1-8) ')) - 1

Tour.runSimulation(startingRow,startingColumn,1)
