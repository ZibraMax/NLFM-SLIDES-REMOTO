import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import mpl_toolkits.mplot3d.art3d as art3d
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap

nx = 9
ny = 9

hx = 0.5
hy = 0.5

x0 = 4*hx
x1 = (5)*hx

y0 = 4*hy
y1 = (5)*hy
center = np.array([x0 + (x1-x0)/2, y0 + (y1-y0)/2, 0.0])
l = 0.25
lr = 6*l

circle = mpatches.Circle(center, lr, fc="none", ec='#dc2c41', linewidth=3)

fig = plt.figure()
ax = Axes3D(fig, computed_zorder=False)
for i in range(nx):
    for j in range(ny):
        x0 = i*hx
        x1 = (i+1)*hx

        y0 = j*hy
        y1 = (j+1)*hy

        rectx = [x0, x1, x1, x0, x0]
        recty = [y0, y0, y1, y1, y0]
        rectz = [0.0, 0.0, 0.0, 0.0, 0.0]
        verts = [list(zip(rectx, recty, rectz))]
        centeri = np.array([x0 + (x1-x0)/2, y0 + (y1-y0)/2, 0.0])
        if np.linalg.norm(centeri-center) < lr:
            poly = Poly3DCollection(verts)
            poly.set_facecolor('#dcdcdc')
            ax.add_collection3d(poly)
            if i == 4 and j == 4:
                poly = Poly3DCollection(verts)
                poly.set_facecolor('#dc2c41')
                ax.add_collection3d(poly)
                # plt.fill(rectx, recty, c='#dc2c41')

        ax.plot(rectx, recty, rectz, c='k')
        ax.plot(x0 + (x1-x0)/2, y0 + (y1-y0)/2, 0.0, 'o', c='#5c5c5c')

ax.add_patch(circle)
art3d.patch_2d_to_3d(circle, 0.0, 'z')


def ate(p):
    return np.exp(-p)


x = np.linspace(0.0, 4.5, 51)

xx, yy = np.meshgrid(x, x)
x = xx.flatten()
y = yy.flatten()
p = ((x-center[0])**2+(y-center[1])**2)**0.5
pp = ((xx-center[0])**2+(yy-center[1])**2)**0.5
z = ate(p/l)
zz = ate(pp/l)

ncolors = 256
color_array = plt.get_cmap('Reds')(range(ncolors))

# change alpha values
color_array[:, -1] = 1.0-np.logspace(np.log10(0.000001),
                                     np.log10(1), ncolors, base=10)[::-1]

# create a colormap object
map_object = LinearSegmentedColormap.from_list(
    name='RedsAlpha', colors=color_array)

# register this new colormap with matplotlib
plt.register_cmap(cmap=map_object)


ax.plot_trisurf(x, y, z, cmap='RedsAlpha', zorder=100)

# plt.gca().set_aspect('equal')
# plt.gca().add_artist(circle)
plt.axis('off')
# plt.tight_layout()
plt.savefig("./resources/deteccion_no_local_3D.svg", bbox_inches='tight')
plt.show()
