
import matplotlib.pyplot as plt
import numpy as np
class hyperon(object):
    def __init__(self,n, charge, radius=2*np.pi):
        self.n=n
        self.charge=charge
        self.radius=radius
        self.angles = [ i*2*np.pi/n for i in np.arange(n)]
        self.positions= [[radius*np.cos(x), radius*np.sin(x)] for x in self.angles]

    def plotMe(self):
        fig = plt.figure(figsize=plt.figaspect(1))
        # Square figure
        ax = fig.add_subplot(111, projection='3d')
        getattr(ax, 'set_{}lim'.format('x'))((-np.pi / 4, np.pi / 4))
        getattr(ax, 'set_{}lim'.format('y'))((-np.pi / 4, np.pi / 4))
        getattr(ax, 'set_{}lim'.format('z'))((-np.pi / 4, 2.25 * np.pi))