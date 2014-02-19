class Board():
    gameBoard = [[]]
    
    def __init__(self,boardSize):
        self.gameBoard = [[0 for x in xrange(boardSize)] for x in xrange(boardSize)]
           

class KnightsTour():
    boardSize = 6
    knightsMoves = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
    playersBoard = Board(1)

    def __init__(self,boardSize):
        self.initialize(boardSize)

    def initialize(self,boardSize):
        self.boardSize=boardSize     
        self.playersBoard = Board(boardSize)

Tour = KnightsTour(8)
print Tour.knightsMoves
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in Tour.playersBoard.gameBoard]))
