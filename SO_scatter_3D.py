from SO_grid import l1listb, l2listb, nstructurelist
from SO_energies import energylist

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(projection='3d')


ax.scatter(l1listb[350:500], l2listb[350:500], energylist[350:500])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
