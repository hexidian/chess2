class Piece:

    def __init__(self,color):
        self.color = color

    def isLegalMove(self,move, board):
        return False

    def possibleMoves(self, board):
        return []

    def __str__(self):
        return "na"

class Pawn(Piece):

    def __init__(self,col,color):
        self.color = color

        self.col = col
        self.row = 1 if color else 6#color of True is white, False is black

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

class Rook(Piece):

    def __init__(self,col,color):
        self.color = color

        self.col = col
        self.row = 0 if color else 7#color of True is white, False is black

    def isLegalMove(self,move,board):

        #depending on where the target tile is, check all the tiles in between this piece and that tile
        if move[2] > move[0]:
            for row in range(move[0]+1,move[2]):
                if (board.grid[row][move[1]]) != None:
                    return False
        elif move[2] < move[0]:
            for row in range(move[2] + 1, move[0]):
                if (board.grid[row][move[1]]) != None:
                    return False
        elif move[3] > move[1]:
            for col in range(move[1] + 1, move[3]):
                if (board.grid[move[0]][col]) != None:
                    return False
        elif move[3] < move[1]:
            for col in range(move[3] + 1, move[1]):
                if (board.grid[move[0]][col]) != None:
                    return False
        else:#if the target is just the same as this tile
            return False

        targetPiece = board.grid[move[2]][move[3]]

        #check if the player is trying to take their own piece
        if targetPiece == None:
            return True
        if targetPiece.color == this.color:
            return False
        return True

    def possibleMoves(self,board):#NOTE: this function will not take into account if you are moving yourself into check
        moves = []

        #check moving left
        for col in range(self.col-1,-1,-1):#looks left and does 0
            target = board.grid[self.row][col]
            if target == None:#if there is nothing there
                moves.append([self.row,self.col,self.row,col])
            elif target.color != self.color:#if there is a piece of the opposite color
                moves.append([self.row,self.col,self.row,col])
                break
            else:#if there is a piece of the same color
                break

        #check moving right
        for col in range(self.col,8):
            target = board.grid[self.row][col]
            if target == None:#if there is nothing there
                moves.append([self.row,self.col,self.row,col])
            elif target.color != self.color:#if there is a piece of the opposite color
                moves.append([self.row,self.col,self.row,col])
                break
            else:#if there is a piece of the same color
                break

        #check moving up
        for row in range(self.row,-1,-1):
            target = board.grid[row][self.col]
            if target == None:#if there is nothing there
                moves.append([self.row,self.col,row,self.col])
            elif target.color != self.color:#if there is a piece of the opposite color
                moves.append([self.row,self.col,row,self.col])
                break
            else:#if there is a piece of the same color
                break

        #check moving down
        for row in range(self.row,8):
            target = board.grid[row][self.col]
            if target == None:#if there is nothing there
                moves.append([self.row,self.col,row,self.col])
            elif target.color != self.color:#if there is a piece of the opposite color
                moves.append([self.row,self.col,row,self.col])
                break
            else:#if there is a piece of the same color
                break

        return moves

    def __str__(self):
        return ("w" if self.color else "b") + "R"

class Board:

    def __init__(self):
        self.initiateGrid()

    def initiateGrid(self):
        self.grid = [[None for i in range(8)] for i in range(8)]
        for col in range(8):
            self.grid[1][col] = Pawn(col,True)
            self.grid[6][col] = Pawn(col,False)


        self.grid[0][0] = Rook(0,True)
        self.grid[0][7] = Rook(7,True)

        self.grid[7][0] = Rook(0,False)
        self.grid[7][7] = Rook(7,False)

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
