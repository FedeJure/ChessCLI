import os
import re

inputTranslator = {
    "" : 0,
    "2" : 1,
    "3" : 2,
    "4" : 3,
    "5" : 4,
    "6" : 5,
    "7" : 6,
    "8" : 7,
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7,
}

class Chess:
    def __init__(self, whiteName, blackName, turnRepository) :
        self.sideSize = 8
        self.table = Table()
        print(self.table)
        self.blackPlayer = Player(blackName, turnRepository)
        self.whitePlayer = Player(whiteName, turnRepository)

    def playTurn(self, userInput):
        regex = re.compile("[12345678][abcdefgh] [12345678][abcdefgh]")
        if regex.match(userInput) is not None:
            fromPos = Position(inputTranslator[userInput[0]], inputTranslator[userInput[1]])
            toPos = Position(inputTranslator[userInput[3]], inputTranslator[userInput[4]])
            return self.table.movePiece(fromPos, toPos)
        return False

    def __repr__(self):
        return self.table.__repr__()



class Player:
    def __init__(self, name, turnRepository):
        self.name = name
        self.turnRepository = turnRepository

    def play(self, chess, fromPosition, toPosition) :
        if (_canPlay() == False) : return
        print("playing")

    def _canPlay():
        return turnRepository.getCurrent() == self.name



class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TurnRepository:
    def __init__(self, whiteName, blackName):
        self.turns = [whiteName, blackName]
        self.winner = None

    def getCurrent(self):
        current = self.turns[0]
        return current
    
    def nextTurn(self):
        self.turns.reverse()

    def finished(self):
        return self.winner != None


class Table:
    def __init__(self):
        self.size = 8
        self.table = [" "] * self.size   # [2,3] => [3,d]
        for i in range(self.size):
            self.table[i] = [" "] * self.size

        self._initPieces()

    def __repr__(self):
        repr = ""
        repr += "     A     B     C     D     E    F     G     H\n"
        repr += "    _____________________________________________\n"
        aux = ["1","2","3","4","5","6","7","8"]
        for i in range(self.size):
            repr += aux[i] + " | "+self.table[i][0].__repr__()+" | "+self.table[i][1].__repr__()+" | "+self.table[i][2].__repr__()+" | "+self.table[i][3].__repr__()+" | "+self.table[i][4].__repr__()+" | "+self.table[i][5].__repr__()+" | "+self.table[i][6].__repr__()+" | "+self.table[i][7].__repr__()+" |\n"
            repr += "    _____________________________________________\n"

        return repr
        
    def _initPieces(self):
        for i in range(self.size):
            self.table[1][i] = Peon("B")
            self.table[6][i] = Peon("N")

        self.table[0][0] = Torre("B")
        self.table[7][0] = Torre("N")

        self.table[0][1] = Alfil("B")
        self.table[7][1] = Alfil("N")

        self.table[0][2] = Caballo("B")
        self.table[7][2] = Caballo("N")

        self.table[0][3] = Reina("B")
        self.table[7][3] = Rey("N")

        self.table[0][4] = Rey("B")
        self.table[7][4] = Reina("N")

        self.table[0][5] = Caballo("B")
        self.table[7][5] = Caballo("N")

        self.table[0][6] = Alfil("B")
        self.table[7][6] = Alfil("N")
        
        self.table[0][7] = Torre("B")
        self.table[7][7] = Torre("N")

    def movePiece(self, fromPos, toPos):
        piece = self.table[fromPos.x][fromPos.y]
        if (piece is " "):
            return False
        intermediatePieces = self.getIntermediatepiecesFromTo(fromPos, toPos)
        if not piece.canMoveTo(fromPos, toPos, intermediatePieces):
            return False
        secondPiece = self.table[toPos.x][toPos.y]
        if (secondPiece is not " "):
            piece = piece #delete this  
            # Kill second piece, do related stuffs
        self.table[fromPos.x][fromPos.y] = " "
        self.table[toPos.x][toPos.y] = piece
        return True

    def getIntermediatepiecesFromTo(self, fromPos, toPos):
        return []

class Peon:
    def __init__(self, colorId):
        self.colorId = colorId
    def __repr__(self):
        return "P-" + self.colorId
    def canMoveTo(self, fromPos, toPos, intermediatePieces):
        return True

class Alfil:
    def __init__(self, colorId):
        self.colorId = colorId
    def __repr__(self):
        return "A-" + self.colorId
    def canMoveTo(self, fromPos, toPos, intermediatePieces):
        return True

class Caballo:
    def __init__(self, colorId):
        self.colorId = colorId
    def __repr__(self):
        return "C-" + self.colorId
    def canMoveTo(self, fromPos, toPos, intermediatePieces):
        return True

class Torre:
    def __init__(self, colorId):
        self.colorId = colorId
    def __repr__(self):
        return "T-" + self.colorId
    def canMoveTo(self, fromPos, toPos, intermediatePieces):
        return True

class Reina:
    def __init__(self, colorId):
        self.colorId = colorId
    def __repr__(self):
        return "Q-" + self.colorId
    def canMoveTo(self, fromPos, toPos, intermediatePieces):
        return True

class Rey:
    def __init__(self, colorId):
        self.colorId = colorId
    def __repr__(self):
        return "K-" + self.colorId
    def canMoveTo(self, fromPos, toPos, intermediatePieces):
        return True

#________________
#8               |
#7               |
#6               |
#5               |
#4               |
#3               |
#2               |
#1               |
# a b c d e f g h

def clearScreen():
    if (os.name == "posix"):
        system("clear")
    else :
        system("cls")
        

def initGame():
    print("### Ajedrez ###")
    print("Ingrese nombre del jugador BLANCAS:")
    whiteName = raw_input()
    print("Ingrese nombre del jugador NEGRAS:")
    blackName = raw_input()

    turnRepository = TurnRepository(whiteName, blackName)
    chess = Chess(whiteName, blackName, turnRepository)

    while not turnRepository.finished():
        played = False
        while not played:
            userInput = raw_input("Juega "+turnRepository.getCurrent()+" > ")
            played = chess.playTurn(userInput)

        print(chess)
        turnRepository.nextTurn()


initGame()