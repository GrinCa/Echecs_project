class Element():
    name_element = ""
    ID = ""
    list_elements = ["pion", "tour", "fou", "cavalier", "roi", "dame", "none"]
    list_ID_letter = ["P", "T", "F", "C", "R", "D", "N"]
    color = ""
    pos_i = 0
    pos_j = 0

    def __init__(self, name_element, couleur, pos_i, pos_j):
        self.name_element = name_element
        self.pos_i = pos_i
        self.pos_j = pos_j
        if couleur == "black" or couleur == "white" or "none":
            self.couleur = couleur
        else:
            print("probleme de definition de couleur")

        if self.name_element in self.list_elements:
            self.ID = self.list_ID_letter[self.list_elements.index(self.name_element)]
        else:
            print("probleme de definition d'ID")

    def __str__(self):
        return "Name :  " + self.name_element + "\nID :  " + str(self.ID) + "\nCoordonnées : (" + str(
            self.pos_i) + "," + str(self.pos_j) + ")"

    def change_position(self, i, j):
        self.pos_i = i
        self.pos_j = j

    def get_position(self):
        return [self.pos_i, self.pos_j]

    def copy(self):
        return Element(self.name_element, self.couleur, self.pos_i, self.pos_j)
