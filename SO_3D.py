from SO_grid import l1listb, l2listb, nstructurelist
from SO_energies import energylist

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = l1listb
Y = l2listb
Z = energylist

# Plot the surface.

surf = ax.plot_trisurf(X, Y, Z, cmap="gray", linewidth=0, antialiased=False)

# Customize the z axis.
#
ax.set_zlim(-0.1*10**(-6.0), 10.0*10**(-6.0))
#ax.zaxis.set_major_locator(LinearLocator(10))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.xlabel("l1")
plt.ylabel("l2")

plt.show()




