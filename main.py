import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

def AmpFromTimeAndPosOffsets(t, x):
    return np.cos(k0*x - omega0*t)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

dt = 0.03
omega0 = .1*np.pi

dx = 0.05
k0 = .3*np.pi

T = np.arange(0, 20, dt)
X = np.arange(0, 100, dx)

Ta, Xa = np.meshgrid(T, X) # 'a' for 'axis'

ax.set_zlim(-1.01, 1.01)

# Fixing random state for reproducibility
rng = np.random.default_rng(19680801)

Tnoise = (-1.0+2*rng.standard_normal(T.size))
Xnoise = (-1.0+2*rng.standard_normal(X.size))

#Perfectly coherent
#T1, X1 = np.meshgrid(T, X)
#Y1 = AmpFromTimeAndPosOffsets(T1, X1)
#surf1 = ax.plot_surface(Ta, Xa, Y1, cmap=cm.coolwarm,
#                       linewidth=0, antialiased=True)
#fig.colorbar(surf1, shrink=0.5, aspect=5)

#Temporally-coherent but spatially-incoherent
#T2, X2 = np.meshgrid(T, X+Xnoise)
#Y2 = AmpFromTimeAndPosOffsets(T2, X2)
#surf2 = ax.plot_surface(Ta, Xa, Y2, cmap=cm.coolwarm,
#                       linewidth=0, antialiased=True)
#fig.colorbar(surf2, shrink=0.5, aspect=5)

#Temporally-incoherent but spatially-coherent
T3, X3 = np.meshgrid(T+Tnoise, X)
Y3 = AmpFromTimeAndPosOffsets(T3, X3)
surf3 = ax.plot_surface(Ta, Xa, Y3, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
fig.colorbar(surf3, shrink=0.5, aspect=5)

ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_zlabel('y');
plt.show()
