import numpy as np

import Echequier
from Element import *


class King(Element):

    def __init__(self, name_element, couleur, pos_i, pos_j):
        Element.__init__(self, name_element, couleur, pos_i, pos_j)
        self.nb_play = 0

    def validate_movement(self, echequier, i, j, i_next, j_next):
        if abs(i - i_next) <= 1 and abs(j - j_next) <= 1:
            if echequier[i_next][j_next].ID == "N":
                self.nb_play += 1
                return True
            else:
                if echequier[i][j].couleur != echequier[i_next][j_next].couleur:
                    self.nb_play += 1
                    return True
                else:
                    return False
        elif i == i_next and abs(j - j_next) == 2 and self.nb_play == 0:  # if rook movement
            increment = self.rook(echequier, i, j, i_next, j_next)  # test rook conditions
            # increment == 0, no rook
            # increment == 2, small rook
            # increment == 3, great rook
            if increment != 0:  # if increment == 0, rook condition are not satisfied
                s_j = np.sign(j_next - j)  # give the direction of movement
                copy_echequier = Echequier.copy_echequier(echequier)  # copy of echequier to run test
                # without changing the real echequier
                for k in range(1, increment - 1):  # check if the king is checked during the movement
                    # until increment-1 instead of increment given the fact that the last position will be checked in
                    # all cases
                    echequier[i][int(j + s_j * k)] = echequier[i][int(j + s_j * (k - 1))]
                    echequier[i][int(j + s_j * k)].change_position(i, int(j + s_j * k))
                    echequier[i][int(j + s_j * (k - 1))] = \
                        Element("none", "none", i, int(j + s_j * (k - 1)))
                    if self.is_check(copy_echequier):  # if king is checked, rook isn't possible
                        echequier[i][j] = echequier[i][int(j + s_j * k)]
                        echequier[i][j].change_position(i, j)
                        echequier[i][int(j + s_j * k)] = Element("none", "none", i, int(j + s_j * k))
                        return False
                echequier[i][j_next - s_j] = echequier[i][j_next + increment % 2 + 1]
                echequier[i][j_next - s_j].change_position(i, j_next - s_j)
                echequier[i][j_next + increment % 2 + 1] = Element("none", "none", i, j_next + increment % 2 + 1)
                return True
            else:
                return False

    def is_check(self, echequier):
        return self.check_lines(echequier) or self.check_knight_position(echequier) or self.check_diags(echequier)

    def check_diags(self, echequier):
        signs = [1, -1]  # enable to browse all diags
        increment = 0  # increment for moving forward into diags
        position = self.get_position()  # position of the king
        something = False  # boolean to check if there is something on a box
        for s_i in signs:
            for s_j in signs:
                while 0 <= int(position[0] + s_i * (increment + 1)) <= 7 \
                        and 0 <= int(position[1] + s_j * (increment + 1)) <= 7:
                    increment += 1
                    if echequier[int(position[0] + s_i * increment)][int(position[1] + s_j * increment)].ID != "N":
                        something = True
                        break
                if something:  # if there is something, we check the kind of piece
                    current_element = echequier[int(position[0] + s_i * increment)][
                        int(position[1] + s_j * increment)]  # element on the box
                    if current_element.couleur != self.couleur:  # check the color, only a difference count
                        if increment == 1 and current_element.ID != "P":
                            if self.couleur == "white" and s_i > 0:
                                return True
                            if self.couleur == "black" and s_i < 0:
                                return True
                        if current_element.ID == "D":
                            return True
                        if current_element.ID == "F":
                            return True
                increment = 0
                something = False
        return False

    def check_lines(self, echequier):
        signs = [1, -1]  # enable to browse all lines
        increment = 0  # increment for moving forward into lines
        position = self.get_position()  # position of the king
        something = False  # boolean to check if there is something on a box
        for s_i in signs:
            while 0 <= int(position[0] + s_i * (increment + 1)) <= 7:
                increment += 1
                if echequier[int(position[0] + s_i * increment)][position[1]].ID != "N":
                    something = True
                    break
            if something:
                current_element = echequier[int(position[0] + s_i * increment)][position[1]]  # element on the box
                if current_element.couleur != self.couleur:
                    if current_element.ID == "T":
                        return True
                    if current_element.ID == "D":
                        return True
            increment = 0
            something = False
        for s_j in signs:
            while 0 <= int(position[1] + s_j * (increment + 1)) <= 7:
                increment += 1
                if echequier[position[0]][int(position[1] + s_j * increment)].ID != "N":
                    something = True
                    break
            if something:
                current_element = echequier[position[0]][int(position[1] + s_j * increment)]  # element on the box
                if current_element.couleur != self.couleur:
                    if current_element.ID == "T":
                        return True
                    if current_element.ID == "D":
                        return True
            increment = 0
            something = False
        return False

    def check_knight_position(self, echequier):
        position = self.get_position()
        box_coord = [-2, -1, 1, 2]
        for i in box_coord:
            for j in box_coord:
                if (abs(i) == 1 and abs(j) == 2) or (abs(i) == 2 and abs(j) == 1):
                    if 0 <= (position[0] + i) <= 7 and 0 <= (position[1] + j) <= 7:
                        current_element = echequier[position[0] + i][position[1] + j]
                        if current_element.ID == "C":
                            if current_element.couleur != self.couleur:
                                return True
        return False

    def rook(self, echequier, i, j, i_next, j_next):
        s_j = np.sign(j_next - j)
        increment = 0
        while 0 <= int(j + s_j * (increment + 1)) <= 7:
            if echequier[i][int(j + s_j * (increment + 1))].ID == "N":
                increment += 1
            else:
                break
        if (increment == 2 or increment == 3) and echequier[i][int(j + s_j * (increment + 1))].ID == "T":
            return increment
        else:
            return 0
