
class Pawn:

    def __init__(self,col,color):
        self.col = col
        self.row = 1 if color else 6#color of True is white, False is black
        self.color = color

    def possibleMoves(self, board):
        moves = []

        nextRow = (self.row + 1) if self.color else (self.row - 1)

        #get basic moves (i.e. moving forward one or two)
        try:
            if board.grid[nextRow][self.col] == None:
                moves.append([self.row,self.col,self.row+1,self.col])
                try:
                    twoRowsNext = (self.row + 2) if self.color else (self.row -2)
                    if (board.grid[twoRowsNext][self.col] == None) and (self.row == 1 if self.color else 6):
                        moves.append([self.row,self.col,twoRowsNext,self.col])
                except:
                    pass
        except:
            pass

        #get the possible taking moves

        if self.col!=0:
            if board.grid[nextRow][self.col-1] != None:
                moves.append([self.row,self.col,nextRow,self.col-1])
        if self.col!=7:
            if board.grid[nextRow][self.col+1] != None:
                moves.append([self.row,self.col,nextRow,self.col+1])

        print("possible moves are:")
        print(moves)
        print("because I am at:")
        print(self.row,self.col)
        return moves

    def isLegalMove(self,move,board):
        #TODO: make more efficient
        moves = self.possibleMoves(board)
        return (move in moves)

    def __str__(self):
        return ("w" if self.color else "b") + "P"

class Board:

    def __init__(self):
        self.initiateGrid()

    def initiateGrid(self):
        self.grid = [[None for i in range(8)] for i in range(8)]
        for col in range(8):
            self.grid[1][col] = Pawn(col,True)
            self.grid[6][col] = Pawn(col,False)

    def takeUserMove(self):
        raw = input("\nPlease enter your move:\n\n>>>")#TODO: make sure move is entered correctly
        chars = raw.split()
        move = [int(i) for i in chars]
        if(self.grid[move[0]][move[1]].isLegalMove(move,self)):
            print("doing move...")
            self.movePiece(move)
        else:
            print("illegal move")

    def movePiece(self,move):#make sure to check if it's a legal move first, if it is coming from the user
        self.grid[move[2]][move[3]]=self.grid[move[0]][move[1]]
        self.grid[move[0]][move[1]]=None

    def __str__(self):
        thing = ""
        for row in range(8):
            for col in range(8):
                if self.grid[row][col]!=None:
                    thing += str(self.grid[row][col]) + " "
                else:
                    thing += "   "
            thing += "\n"
        return thing

if __name__ == "__main__":
    board = Board()
    print(board)
    while 1:
        board.takeUserMove()
        print(board)
