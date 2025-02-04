import matplotlib.pyplot as plt
import numpy as np
from SO_grid import l1listb, l2listb, nstructurelist
from SO_energies import energylist
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, ListedColormap



plt.scatter(l1listb, l2listb, c=energylist, cmap='gray')
plt.xlabel("l1")
plt.ylabel("l2")
plt.colorbar()
plt.savefig('SO_chart_gray_2.png')




