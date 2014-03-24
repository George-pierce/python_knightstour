import time
import sys
from heapq import heappush, heappop

#NOTES: COULD NOT GET THIS CLASS TO WORK AS AN ABSTRACT CLASS
# THOUGHT PROCESS WAS TO STORE COMMON VARIABLES FOR ALL ALGORITHMS HERE, AND LET CHILD ALGOS USE IT>
#class AbstractAlgorithm():
#    gameBoard = None
#    currentRow = None
#    currentColumn = None
#    knightsMoves = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
#    priorityQueue = None
#    def getNextMove(self,row,column,gameBoard):
#        raise NotImplementedError("Should be Implemented In subclass")
        

class WarnsDorffAlgorithm():    
    gameBoard = None
    currentRow = None
    currentColumn = None
    knightsMoves = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
    priorityQueue = None

    def __init__(self):
             init =2
    
    def computeMoves(self,row,column,gameBoard):
        self.gameBoard = gameBoard
        self.currentRow = row
        self.currentColumn = column
        self.priorityQueue = []  
        self.setupMovesQueue()

    def getNextMove(self): 
        #Now, pull an unused move from the queue
        if len(self.priorityQueue)> 0:
            return heappop(self.priorityQueue)
        else:
            return -1, (-1,-1)        

    def setupMovesQueue(self):
        
        for indexRow,indexColumn in self.knightsMoves:
            availableMoves  = 0
            nextRow = self.currentRow + indexRow 
            nextColumn = self.currentColumn + indexColumn
            if self.gameBoard.isPositionOnBoard(nextRow,nextColumn) and self.gameBoard.isValidMove(nextRow,nextColumn):
                #Need 1 additional check that sees if this move will win the game.
                availableMoves +=1 #This move we are attempting is viable, so include it
                for indexRow,indexColumn in self.knightsMoves:
                    rowAttempt = nextRow + indexRow 
                    columnAttempt = nextColumn + indexColumn
                    if self.gameBoard.isPositionOnBoard(rowAttempt,columnAttempt) and self.gameBoard.isValidMove(rowAttempt,columnAttempt):
                        availableMoves+=1
            if availableMoves > 0:
                heappush(self.priorityQueue,(availableMoves,(nextRow,nextColumn)))

#Standard brute force backtracking implementation
class BruteForce():
    gameBoard = None
    currentRow = None
    currentColumn = None
    knightsMoves = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
    priorityQueue = None

    def __init__(self):
             init =2
    
    def computeMoves(self,row,column,gameBoard):
        self.gameBoard = gameBoard
        self.currentRow = row
        self.currentColumn = column
        self.priorityQueue = []  
        self.setupMovesQueue()

    def getNextMove(self): 
        #Now, pull an unused move from the queue
        if len(self.priorityQueue)> 0:
            return heappop(self.priorityQueue)
        else:
            return -1, (-1,-1)        

    def setupMovesQueue(self):
        index  = 1
        
        for indexRow,indexColumn in self.knightsMoves:
            nextRow = self.currentRow + indexRow 
            nextColumn = self.currentColumn + indexColumn
            if self.gameBoard.isPositionOnBoard(nextRow,nextColumn) and self.gameBoard.isValidMove(nextRow,nextColumn):
                heappush(self.priorityQueue,(index,(nextRow,nextColumn)))
            index+=1
#Board Class
class Board():
    gameBoard = None
    currentPositionChar = 'K'
    visitedPositionChar = 'K'

    def __init__(self,boardSize):
        self.gameBoard = [[0 for x in xrange(boardSize)] for x in xrange(boardSize)]
     
    def resetPosition(self, rowIndex,columnIndex):        
            self.gameBoard[rowIndex][columnIndex] = 0 

    def setPosition(self, rowIndex, columnIndex,stepInterval):        
            self.gameBoard[rowIndex][columnIndex] = stepInterval  

    def printBoard(self):
         s = [[str(e).zfill(1) for e in row] for row in self.gameBoard]
         lengths = [max(map(len,col)) for col in zip(*s)]
         fmt = " | ".join("{{:{}}}".format(x) for x in lengths)
         table = [fmt.format(*row) for row in s]
         print "\n".join(table)         
         
    def isValidMove(self,row,column):
       # Is move on gameBoard?
       if not self.isPositionOnBoard(row,column):
           return False        
       #is move still valid, ie not traversed already
       if self.gameBoard[row][column] == 0:#self.visitedPositionChar:
           return True
       return False

    def isPositionOnBoard(self,row,column):
       if (row < 0) or (column < 0) or (row > len(self.gameBoard) - 1) or (column > len(self.gameBoard) - 1):
           return False 
       return True

    def successfulTraversal(self):
         for row in range(len(self.gameBoard)):
            for column in range(len(self.gameBoard[row])):
                if self.gameBoard[row][column] == 0:
                    return False
         return True   


# Tour Class
class KnightsTour():
    boardSize = 8    
    playersBoard = None
    algorithmType = None
    def __init__(self,boardSize,algorithm):
        self.boardSize = boardSize     
        self.playersBoard = Board(boardSize)   
        self.algorithmType = algorithm       

    def printBoard(self):
        self.playersBoard.printBoard()

    def runSimulation(self,startingRow,startingColumn,stepInterval): 
        algorithm = None       
        if self.algorithmType == 0:
            algorithm = BruteForce()
        elif self.algorithmType ==1:
            algorithm = WarnsDorffAlgorithm()
        #Update the board with new position                    
        self.playersBoard.setPosition(startingRow,startingColumn,stepInterval)          
        #Check if we finished the Tour
        if self.playersBoard.successfulTraversal():
            print "\n We won!!" 
            #self.printBoard()
            return 'Success', [[startingRow,startingColumn]]                   
           
        currentStep =stepInterval+1
        algorithm.computeMoves(startingRow,startingColumn,self.playersBoard) 
        nextMove = algorithm.getNextMove()
        while nextMove[0] <> -1:
            nextRow = nextMove[1][0]
            nextColumn = nextMove[1][1]
            traversalStatus, movesList =  self.runSimulation(nextRow,nextColumn,currentStep)
            if traversalStatus =='Success':
                movesList.insert(0,[startingRow,startingColumn])
                return 'Success', movesList
            nextMove = algorithm.getNextMove()        
        
        self.playersBoard.resetPosition(startingRow,startingColumn)    
        return "Failure"


 #Main program execution
quit = "N" 
sys.setrecursionlimit(1500)
while quit != "Y":
    boardSize = 0
    while boardSize < 3:
        boardSize = int(raw_input("Enter your board size, this will be a square board: "))

    algorithmType  = -1  #Default to Warnsdorff

    while algorithmType < 0:
        algorithmType = int(raw_input("Enter an algorithm to solve the Knights Tour, (1 for Brute Force, 2 for WarnsDorff's Algorithm) : ")) -1
    Tour = KnightsTour(boardSize,algorithmType)
    startingRow = -1
    startingColumn = -1
    
    while (startingRow < 0 or startingRow > boardSize) or (startingColumn < 0 or startingColumn > boardSize):
        startingRow = int(raw_input('Enter your starting position: (Row # 1-8) ')) - 1
        startingColumn = int(raw_input('Enter your starting position: (Column # 1-8) ')) - 1

    tourResult, movesList = Tour.runSimulation(startingRow,startingColumn,1)
    if tourResult == "Failure":
        print "Sorry, no tour possible for your starting positions"
    else:
        #Print out the moves listing that was successful
        summaryBoard = Board(boardSize)
        index =1
        for row, column in movesList:
            summaryBoard.setPosition(row,column, 'K')
            print " \n Step ", index , " moving to ", row+1 , ",", column+1, " \n"
            summaryBoard.printBoard() , "\n"
            time.sleep(2)
            index +=1
    quit = str(raw_input(" \n Would you like to play again? ( Y or N) :"))

