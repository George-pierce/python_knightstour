import time

class Board():
    gameBoard = None
    currentPositionChar = 'K'
    visitedPositionChar = 'X'

    def __init__(self,boardSize):
        self.gameBoard = [[0 for x in xrange(boardSize)] for x in xrange(boardSize)]
     
    def resetPosition(self, rowIndex,columnIndex):
        gameBoard[rowIndex][columnIndex] = '0'

    def setPosition(self, rowIndex, columnIndex,stepInterval):
        self.gameBoard[rowIndex][columnIndex] = stepInterval
    
    def printBoard(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.gameBoard]))

    def isValidMove(row,column):
       


class KnightsTour():
    boardSize = 8
    knightsMoves = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
    playersBoard = None

    def __init__(self,boardSize):
        self.initialize(boardSize)

    def initialize(self,boardSize):
        self.boardSize=boardSize     
        self.playersBoard = Board(boardSize)

    def printBoard(self):
        self.playersBoard.printBoard()

    def runSimulation(self,startingRow,startingColumn,stepInterval):
        print 'You are starting at row ',startingRow, ' and column ', startingColumn

        #Update the board with new position
        self.playersBoard.setPosition(startingRow,startingColumn,1)

        #Print the current Location on the board
        self.printBoard()
        #Try each available move, and run the simulation on the new starting position
        for indexRow,indexColumn in self.knightsMoves:
            newPosition_Row = ((startingRow)+ indexRow )
            newPosition_Column = ((startingColumn) + indexColumn)
            print  "starting at position ",startingRow, startingColumn, " and moving to these coords: ",  indexRow , indexColumn, " and moving to ", newPosition_Row, ' ' , newPosition_Column
            time.sleep(10)

        

boardSize = 8
Tour = KnightsTour(boardSize)
Tour.printBoard()

startingRow = 0
startingColumn = 0

while (startingRow < 1 or startingRow > boardSize) or (startingColumn < 1 or startingColumn > boardSize):
    startingRow = int(raw_input('Enter your starting position: (Row # 1-8) ')) -1
    startingColumn = int(raw_input('Enter your starting position: (Column # 1-8) ')) -1

Tour.runSimulation(startingRow,startingColumn,1)
