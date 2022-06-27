import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

h = 9
l = 0.5
for aaa in [1, 3, 5, 9/5]:
    nx = int(5*(aaa))
    ny = int(5*(aaa))

    hx = h/nx
    hy = h/ny

    centerid = int(nx/2)

    x0 = centerid*hx
    x1 = (centerid+1)*hx

    y0 = centerid*hy
    y1 = (centerid+1)*hy
    center = np.array([x0 + (x1-x0)/2, y0 + (y1-y0)/2])

    lr = 6*l

    circle = mpatches.Circle(center, lr, fc="none", ec='#dc2c41', linewidth=3)

    for i in range(nx):
        for j in range(ny):
            x0 = i*hx
            x1 = (i+1)*hx

            y0 = j*hy
            y1 = (j+1)*hy

            rectx = [x0, x1, x1, x0, x0]
            recty = [y0, y0, y1, y1, y0]
            centeri = np.array([x0 + (x1-x0)/2, y0 + (y1-y0)/2])
            if np.linalg.norm(centeri-center) < lr:
                plt.fill(rectx, recty, c='#dcdcdc')
                if i == centerid and j == centerid:
                    plt.fill(rectx, recty, c='#dc2c41')

            plt.plot(rectx, recty, c='k')
            plt.plot(x0 + (x1-x0)/2, y0 + (y1-y0)/2, '.', c='#5c5c5c')
    t = 0.5
    plt.annotate('',
                 [center[0] + lr*np.cos(t), center[1] + lr*np.sin(t)],
                 xycoords="data",
                 textcoords="data",
                 xytext=(center[0], center[1]),
                 va="center",
                 ha="left",
                 c='#8f1625',
                 size=20,
                 arrowprops=dict(arrowstyle="simple",
                                 connectionstyle="arc3",
                                 ec='#8f1625',
                                 fc='#dc2c41'),
                 )
    plt.annotate('Lr',
                 [center[0] + 0.5*lr*np.cos(t), center[1] + 0.5*lr*np.sin(t)],
                 textcoords="offset points",
                 xytext=(-20, 20),
                 va="center",
                 ha="left",
                 c='#dc2c41',
                 fontsize=20)
    plt.gca().set_aspect('equal')
    plt.gca().add_artist(circle)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(
        f"./resources/deteccion_no_local{aaa}.svg", bbox_inches='tight')
    plt.show()
