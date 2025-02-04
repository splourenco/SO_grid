from SO_grid import l1listb, l2listb, nstructurelist
from SO_energies import energylist

import matplotlib.pyplot as plt
import numpy as np

#Calculate first minimum
grid1 = {}

for i in nstructurelist:
    index = i-1
    if -0.5 < l1listb[index] < 0.5 and -1.0 < l2listb[index] < 1.0:
        x = l1listb[index]
        y = l2listb[index]
        z = energylist[index]
        grid1[x,y] = z

firstminimum = min(grid1.values())
print("1minimum = ", firstminimum)

positionfirstminimum = [k for k, v in grid1.items() if v == min(grid1.values())]
print("position2minimum = ", positionfirstminimum)

#Calculate second minimum
grid2 = {}

for i in nstructurelist:
    index = i-1
    if -0.5 < l1listb[index] < 0.5 and 1.0 < l2listb[index] < 3.0:
        x = l1listb[index]
        y = l2listb[index]
        z = energylist[index]
        grid2[x,y] = z

secondminimum = min(grid2.values())
print("2minimum = ", secondminimum)

positionsecondminimum = [k for k, v in grid2.items() if v == min(grid2.values())]
print("position2minimum = ", positionsecondminimum)


#Calculate maximum
grid3 = {}

for i in nstructurelist:
    index = i-1
    if -0.2 < l1listb[index] < 0.1 and 0.0 < l2listb[index] < 1.5:
        x = l1listb[index]
        y = l2listb[index]
        z = energylist[index]
        grid3[x,y] = z

maximum = max(grid3.values())
print("maximum = ", maximum)

positionmaximum = [k for k, v in grid3.items() if v == maximum]
print("positionmaximum = ", positionmaximum)
