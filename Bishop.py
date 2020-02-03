from math import *

from Element import *


class Bishop(Element):

    def __init__(self, name_element, couleur, pos_i, pos_j):
        Element.__init__(self, name_element, couleur, pos_i, pos_j)

    def validate_movement(self, echequier, i, j, i_next, j_next):
        if abs(i - i_next) == abs(j - j_next):
            for k in range(1, abs(i - i_next)):
                ind_i = int(
                    (1 + copysign(1, i_next - i)) / 2 * (min(i, i_next) + k) + (1 - copysign(1, i_next - i)) / 2 * (
                            max(i, i_next) - k))
                ind_j = int(
                    (1 + copysign(1, j_next - j)) / 2 * (min(j, j_next) + k) + (1 - copysign(1, j_next - j)) / 2 * (
                            max(j, j_next) - k))
                if echequier[ind_i][ind_j].ID != "N":
                    return False
            if echequier[i_next][j_next] == "N":
                return True
            else:
                if echequier[i][j].couleur != echequier[i_next][j_next].couleur:
                    return True
                else:
                    return False
        else:
            return False
