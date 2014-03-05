import time

class Board():
    gameBoard = None
    currentPositionChar = 'K'
    visitedPositionChar = 'X'

    def __init__(self,boardSize):
        self.gameBoard = [[0 for x in xrange(boardSize)] for x in xrange(boardSize)]
     
    def resetPosition(self, rowIndex,columnIndex):
        if self.isPositionOnBoard(rowIndex,columnIndex):
            self.gameBoard[rowIndex][columnIndex] = 0       

    def setPosition(self, rowIndex, columnIndex,stepInterval):
        if self.isPositionOnBoard(rowIndex,columnIndex):
            self.gameBoard[rowIndex][columnIndex] = self.visitedPositionChar
        else:
            io = 2
    
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
        
        if startingRow == 6 and startingColumn ==6:
            gotcha =2
        validMove = self.playersBoard.isValidMove(startingRow,startingColumn)
        if validMove:
            #Update the board with new position
            print 'You are starting at row ',startingRow, ' and column ', startingColumn
            self.playersBoard.setPosition(startingRow,startingColumn,1)
            #Check if we finished the Tour
            if self.playersBoard.successfulTraversal():
                print "We won!!" 
                self.printBoard()
                time.sleep(50)
        else:
            return      
            #Print the current Location on the board
            #self.printBoard()
            #Try each available move, and run the simulation on the new
            #starting position
        for indexRow,indexColumn in self.knightsMoves:
            newPosition_Row = startingRow + indexRow 
            newPosition_Column = startingColumn + indexColumn           
            self.runSimulation(newPosition_Row,newPosition_Column,stepInterval + 1)
            self.playersBoard.resetPosition(newPosition_Row,newPosition_Column)
        
        #print "Backtracking from current Position", startingRow,
        #startingColumn
       
        
boardSize = 8
Tour = KnightsTour(boardSize)
Tour.printBoard()

startingRow = 0
startingColumn = 0

while (startingRow < 1 or startingRow > boardSize) or (startingColumn < 1 or startingColumn > boardSize):
    startingRow = int(raw_input('Enter your starting position: (Row # 1-8) ')) - 1
    startingColumn = int(raw_input('Enter your starting position: (Column # 1-8) ')) - 1

Tour.runSimulation(startingRow,startingColumn,1)
