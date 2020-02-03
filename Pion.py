from Element import *


class Pion(Element):

    def __init__(self, name_element, couleur, pos_i, pos_j):
        Element.__init__(self, name_element, couleur, pos_i, pos_j)
        self.nb_play = 0

    def validate_movement(self, echequier, i, j, i_next, j_next):
        if self.couleur == "white":
            if echequier[i_next][j_next].ID == "N" and (i_next - i) == 1 and j == j_next:
                self.played()
                return True
            elif echequier[i_next][j_next].ID == "N" and (
                    i_next - i) == 2 and j == j_next and self.nb_play == 0:
                self.played()
                return True
            elif echequier[i_next][j_next].ID != "N" and (i_next - i) == 1 and (j_next - j) == 1 and \
                    echequier[i_next][j_next].couleur == "black":
                self.played()
                return True
            elif echequier[i_next][j_next].ID != "N" and (i_next - i) == 1 and (j_next - j) == -1 and \
                    echequier[i_next][j_next].couleur == "black":
                self.played()
                return True
            else:
                return False
        elif self.couleur == "black":
            if echequier[i_next][j_next].ID == "N" and (i - i_next) == 1 and j == j_next:
                self.played()
                return True
            elif echequier[i_next][j_next].ID == "N" and (
                    i - i_next) == 2 and j == j_next and self.nb_play == 0:
                self.played()
                return True
            elif echequier[i_next][j_next].ID != "N" and (i - i_next) == 1 and (j_next - j) == 1 and \
                    echequier[i_next][j_next].couleur == "white":
                self.played()
                return True
            elif echequier[i_next][j_next].ID != "N" and (i - i_next) == 1 and (j_next - j) == -1 and \
                    echequier[i_next][j_next].couleur == "white":
                self.played()
                return True
            else:
                return False

    def copy(self):
        copy_of_pion = Pion(self.name_element, self.couleur, self.pos_i, self.pos_i)
        copy_of_pion.nb_play = self.nb_play
        return copy_of_pion

    def played(self):
        self.nb_play += 1
