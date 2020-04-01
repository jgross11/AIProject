### class for a classic implementation of a tic tac toe board using
### an nxn array
from AIProject.TicTacToe import constants


class ClassicBoard:
    # passed the number of tiles per row / column
    def __init__(self, n):
        self.dimensions = n
        self.movesLeft = n*n
        self.board = [[0]*n for i in range(n)]
        # must assign as board[y][x], not board[x][y]
        print("### INITIAL BOARD STATE ###")
        for x in range(self.dimensions):
            print(self.board[x])

    def placePiece(self, location, piece):
        if self.board[location[1]][location[0]] == 0 and -1 < location[1] < self.dimensions and -1 < location[0] < self.dimensions:
            self.board[location[1]][location[0]] = piece
            self.movesLeft -= 1
            return True
        else:
            print("invalid move")
            return False

    def printBoardRaw(self):
        print("### RAW BOARD ###")
        print(self.board)

    def printBoardGame(self):
        print("### GAME BOARD STATE ###")
        for x in range(self.dimensions):
            print("|", end="")
            for y in range(self.dimensions):
                print(constants.PIECES[self.board[x][y]] + "|", end="")
            print("")

    def printBoardValues(self):
        print("### GAME VALUES STATE ###")
        for x in range(self.dimensions):
            print("|", end="")
            for y in range(self.dimensions):
                print(str(self.board[x][y]) + "|", end="")
            print("")

    def checkForWin(self):
        # check horizontals
        for x in range(self.dimensions):
            sum = 1
            for y in range(self.dimensions):
                sum *= self.board[x][y]
            if sum == 1 or sum == pow(2, self.dimensions):
                print("horizontal win")
                return True

        # check verticals
        for y in range(self.dimensions):
            sum = 1
            for x in range(self.dimensions):
                sum *= self.board[x][y]
            if sum == 1 or sum == pow(2, self.dimensions):
                print("vertical win")
                return True

        # check left-right diagonal
        sum = 1
        for i in range(self.dimensions):
            sum *= self.board[i][i]
            if sum == 1 or sum == pow(2, self.dimensions):
                print("left-right diagonal win")
                return True

        # check right-left diagonal
        sum = 1
        for i in range(self.dimensions):
            sum *= self.board[i][self.dimensions - i - 1]
            if sum == 1 or sum == pow(2, self.dimensions):
                print("right-left diagonal win")
                return True
        return False

    def checkForDraw(self):
        return self.movesLeft == 0

testBoardSize = 5
board = ClassicBoard(testBoardSize)
# board.placePiece([0, 0], constants.X_VALUE)
# board.placePiece([0, 1], constants.X_VALUE)
# board.placePiece([0, 2], constants.O_VALUE)

# board.placePiece([1, 0], constants.X_VALUE)
# board.placePiece([1, 1], constants.O_VALUE)
# board.placePiece([1, 2], constants.X_VALUE)

# board.placePiece([2, 0], constants.O_VALUE)
# board.placePiece([2, 1], constants.X_VALUE)
# board.placePiece([2, 2], constants.X_VALUE)

# uncomment one of the following tests to run

# diagonal test
for i in range(testBoardSize):
    board.placePiece([testBoardSize-1-i, i], constants.O_VALUE)

# vertical test
#for i in range(testBoardSize):
#    board.placePiece([0, i], constants.O_VALUE)

# horizontal test
#for i in range(3):
#    board.placePiece([i, 0], constants.O_VALUE)

# draw test
#for x in range(testBoardSize):
#    for y in range(testBoardSize):
#        board.placePiece([x, y], constants.O_VALUE)
#print(board.checkForDraw())

board.printBoardRaw()
board.printBoardGame()
board.printBoardValues()