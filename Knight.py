from Element import *


class Knight(Element):

    def __init__(self, name_element, couleur, pos_i, pos_j):
        Element.__init__(self, name_element, couleur, pos_i, pos_j)

    def validate_movement(self, echequier, i, j, i_next, j_next):
        if abs(i - i_next) == 1 and abs(j - j_next) == 2:
            if echequier[i_next][j_next].ID == "N":
                return True
            else:
                if echequier[i][j].couleur != echequier[i_next][j_next].couleur:
                    return True
                else:
                    return False
        elif abs(i - i_next) == 2 and abs(j - j_next) == 1:
            if echequier[i_next][j_next].ID == "N":
                return True
            else:
                if echequier[i][j].couleur != echequier[i_next][j_next].couleur:
                    return True
                else:
                    return False
        else:
            return False
