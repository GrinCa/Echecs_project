import time

from Echequier import *

debut = time.time()

echequier = Echequier()
echequier.create_movement(1, 4, 2, 4)
echequier.create_movement(0, 5, 3, 2)
echequier.create_movement(0, 6, 2, 7)
echequier.create_movement(1, 3, 2, 3)
echequier.create_movement(6, 4, 5, 4)
echequier.create_movement(7, 5, 3, 1)
echequier.create_movement(0, 4, 1, 4)
echequier.create_movement(0, 3, 0, 5)

fin = time.time()

print(debut, fin, fin - debut)

print(disp_game(echequier.echequier))

