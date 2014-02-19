
class KnightsTour():
    boardSize = 6
    knightsMoves = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))

    def __init__(self,boardSize):
        self.initialize(boardSize)

    def initialize(self,boardSize):
        self.boardSize=boardSize       


Tour = KnightsTour(8)
print Tour.knightsMoves