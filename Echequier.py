from Bishop import *
from King import *
from Knight import *
from Pion import *
from Queen import *
from Rook import *


def copy_echequier(echequier):
    return [[echequier[i][j].copy() for j in range(8)] for i in range(8)]


def disp_game(echequier):
    line = ""
    for i in range(len(echequier[:][0])):
        for j in range(len(echequier[0][:])):
            line += echequier[i][j].ID + " "
        line += "\n"
    return line


class Echequier():
    echequier_historical = []
    echequier = np.zeros((8, 8)).tolist()

    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.create_pion()
        self.create_bishop()
        self.create_king()
        self.create_knight()
        self.create_rook()
        self.create_queen()
        self.create_none()

    def create_pion(self):
        white_pions = [Pion("pion", "white", 1, j) for j in range(8)]
        black_pions = [Pion("pion", "black", 6, j) for j in range(8)]
        for j in range(8):
            self.echequier[1][j] = white_pions[j]
            self.echequier[6][j] = black_pions[j]

    def create_knight(self):
        white_knights = [Knight("cavalier", "white", 0, int(5 * i + 1)) for i in range(2)]
        black_knights = [Knight("cavalier", "black", 7, int(5 * i + 1)) for i in range(2)]
        self.echequier[0][1] = white_knights[0]
        self.echequier[0][6] = white_knights[1]
        self.echequier[7][1] = black_knights[0]
        self.echequier[7][6] = black_knights[1]

    def create_bishop(self):
        white_bishops = [Bishop("fou", "white", 0, int(3 * i + 2)) for i in range(2)]
        black_bishops = [Bishop("fou", "black", 7, int(3 * i + 2)) for i in range(2)]
        self.echequier[0][2] = white_bishops[0]
        self.echequier[0][5] = white_bishops[1]
        self.echequier[7][2] = black_bishops[0]
        self.echequier[7][5] = black_bishops[1]

    def create_rook(self):
        white_rooks = [Rook("tour", "white", 0, int(7 * i)) for i in range(2)]
        black_rooks = [Rook("tour", "black", 7, int(7 * i)) for i in range(2)]
        self.echequier[0][0] = white_rooks[0]
        self.echequier[0][7] = white_rooks[1]
        self.echequier[7][0] = black_rooks[0]
        self.echequier[7][7] = black_rooks[1]

    def create_king(self):
        white_king = King("roi", "white", 0, 3)
        black_king = King("roi", "black", 7, 3)
        self.echequier[0][3] = white_king
        self.echequier[7][3] = black_king

    def create_queen(self):
        white_queen = Queen("dame", "white", 0, 4)
        black_queen = Queen("dame", "black", 7, 4)
        self.echequier[0][4] = white_queen
        self.echequier[7][4] = black_queen

    def create_none(self):
        for i in range(2, 6):
            for j in range(8):
                self.echequier[i][j] = Element("none", "none", i, j)

    def create_movement(self, i, j, i_next, j_next):
        if not (0 <= i_next <= 7) or not (0 <= j_next <= 7):  # check if i and j are in the frame
            return False
        current_element = self.echequier[i][j]
        if current_element.ID != "N":
            if current_element.validate_movement(self.echequier, i, j, i_next, j_next):
                self.echequier_historical.append(copy_echequier(self.echequier))
                self.echequier[i_next][j_next] = self.echequier[i][j]
                self.echequier[i_next][j_next].change_position(i_next, j_next)
                self.echequier[i][j] = Element("none", "none", i, j)
                king_checked_color = self.is_check()
                if king_checked_color != "":
                    if self.echequier[i_next][j_next].couleur == king_checked_color:
                        self.echequier = self.echequier_historical[-1].copy()
                        return False
                    else:
                        return True
                return True
            else:
                return False
        else:
            return False

    def get_king_position(self):
        kings_positions = []
        for i in range(8):
            for j in range(8):
                if self.echequier[i][j].ID == "R":
                    pos = self.echequier[i][j].get_position()
                    kings_positions.append([self.echequier[i][j].couleur, pos[0], pos[1]])
        return kings_positions

    def is_check(self):
        kings_positions = self.get_king_position()
        for i in range(len(kings_positions)):
            if self.echequier[kings_positions[i][1]][kings_positions[i][2]].is_check(self.echequier):
                return kings_positions[i][0]  # color of the king checked
        return ""
