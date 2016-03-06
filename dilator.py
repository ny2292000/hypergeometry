from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np




# ATOM
#
# Smallest particle of an element which shows all properties of element is called atom.
# Some characteristics of "atoms" are as follows:
# Atom takes part in chemical reactions independently.
# Atom can be divided into a number of sub-atomic particles.
# Fundamental particles of atom are electron, proton and neutron.
# CHARACTERISTICS OF ELECTRON
#
# Charge: It is a negatively charged particle.
# Magnitutide of charge: Charge of electron is 1.6022 x 10-19 Coulomb.
# Mass of electron: Mass of electron is 0.000548597 a.m.u. or 9.1 x 10-31 kg.
# Symbol of electron: Electron is represented by "e".
# Location in the atom: Electrons revolve around the nucleus of atom in different circular orbits.
# CHARACTERISTICS OF PROTON
#
# Charge: Proton is a positively charged particle.
# Magnitude of charge: Charge of proton is 1.6022 x 10-19 coulomb.
# Mass of proton: Mass of proton is 1.0072766 a.m.u. or 1.6726 x 10-27 kg.
# Comparative mass: Proton is 1837 times heavier than an electron.
# Position in atom: Protons are present in the nucleus of atom.
# For latest information , free computer courses and high impact notes visit : www.citycollegiate.com
# CHARACTERISTICS OF NEUTRON
#
# charge: It is a neutral particle because it has no charge.
# Mass of neutron: . Mass of neutron is 1.0086654 a.m.u. or 1.6749 x 10-27 kg.
# Compartive mass: Neutron is 1842 times heavier than an electron.
# Location in the atom: Neutrons are present in the nucleus of an atom.

# Proton Charge=-Electron Charge = 1.6022 x 10-19 Coulomb
# Proton Mass = 1837 Electron Mass

# These are the thicknesses along the radial direction (Fourth Dimensional direction perpendicular to our
# 3D Universe (LightSpeed Expanding Hypersperical Universe).
# The total 4D volume should be identical.
hp=1e-6
he=hp*1837

protonCoeff = (2 / 3, 2 / 3, -1 / 3,hp)
electronCoeff = (0,-2/3,-1/3,he)
positronCoeff = (0,2/3,1/3,-he)
antiprotonCoeff = (-2 / 3, -2 / 3, 1 / 3,-hp)

# The actual amplitude of the metric distorsion is not know. Considering that it is very, very small
# the metric displacement will be approximated by the sum of the 3D coefficients times the radial thickness
# hp is unknown

# Radii corresponding to the coefficients:
class unit(object):
    def __init__(self,coeffs,center=(0,0,0)):
        self.coeffs=coeffs
        self.center=center
        a=1
        print(a)
        self.rx, self.ry, self.rz = [(e+1.0)/a for e in coeffs]
        print(self.rx,self.ry,self.rz)
        print(coeffs)

        # Set of all spherical angles:
        self.u = np.linspace(0, 2 * np.pi, 100)
        self.v = np.linspace(0, np.pi, 100)
    def surface(self,center=(0,0,0)):
        # Cartesian coordinates that correspond to the spherical angles:
        # (this is the equation of an ellipsoid):
        u=self.u
        v=self.v
        x = self.rx * np.outer(np.cos(u), np.sin(v))+self.center[0]
        y = self.ry * np.outer(np.sin(u), np.sin(v))+self.center[1]
        z = self.rz * np.outer(np.ones_like(u), np.cos(v))+self.center[2]
        return x,y,z
    def plotMe(self):
        fig = plt.figure(figsize=plt.figaspect(1))
        # Square figure
        ax = fig.add_subplot(111, projection='3d')
        # Plot:
        x,y,z = self.surface()
        ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
        # Adjustment of the axes, so that they all have the same span:
        max_radius = max(self.rx, self.ry, self.rz)
        max_radius = max(max_radius,self.center[0], self.center[1], self.center[2])
        for axis in 'xyz':
            getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))
        plt.show()

if(__name__=='__main__'):
    vaccumCoeff = (0, 0, 0)
    vaccum = dilator(vaccumCoeff)
    vaccum.plotMe()
    a=1
    protonCoeff = (2 / 3, 2 / 3, -1 / 3)
    proton1 = dilator(protonCoeff)
    proton1.plotMe()
    proton2 = dilator(protonCoeff,(0,0,2*np.pi))
    proton2.plotMe()
    electronCoeff = (0, -2 / 3, -1 / 3)
    electron = dilator(electronCoeff)
    electron.plotMe()
    a=1
    electron.plotMe(np.pi/4.0)
    a=1