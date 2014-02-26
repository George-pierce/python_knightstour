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
            newPosition_Row = ((startingRow-1)+ indexRow )
            newPosition_Column = ((startingColumn-1) + indexColumn)
            print newPosition_Row, ' ' , newPosition_Column
            

        


Tour = KnightsTour(8)
Tour.printBoard()

startingRow = int(raw_input('Enter your starting position: (Row # 1-8) '))
startingColumn = int(raw_input('Enter your starting position: (Column # 1-8) '))

Tour.runSimulation(startingRow,startingColumn,1)
