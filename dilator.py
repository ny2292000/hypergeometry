from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from itertools import cycle



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

def swap_cols(arr, frm, to):
    arr[:,[frm, to]] = arr[:,[to, frm]]
    return arr

def swap_rows(arr, frm, to):
    arr[[frm, to], :] = arr[[to, frm], :]
    return arr

def getSpin(axis=None):
    spin = np.identity(4)
    if axis is None:
        return spin
    spin=swap_cols(spin, axis,3)
    return spin

def getDilatorSequence(particle=0, axis=0, spin='half'):
    hp = 1e-9
    he = hp * 1837
    ident = np.identity(4)
    rotate = getSpin(axis=axis)
    rotationMatrix = [ident,rotate,ident,rotate]
    # Particle Definition
    protonCoeff = np.array([2/3, 2/3, -1/3,hp]).T
    electronCoeff = np.array([0,-2/3,-1/3,he]).T
    positronCoeff = np.array([0,2/3,1/3,-he]).T
    antiprotonCoeff = np.array([-2/3, -2/3, 1/3,-hp]).T
    if(spin=='half'):
        listA = [protonCoeff, electronCoeff,antiprotonCoeff, positronCoeff,protonCoeff, electronCoeff,antiprotonCoeff, positronCoeff]
    else:
        listA=[protonCoeff,positronCoeff ,antiprotonCoeff, electronCoeff,protonCoeff,positronCoeff ,antiprotonCoeff,electronCoeff ]
    listA = listA[particle:(particle+4)]
    dilatorSequence = [np.dot(rotationMatrix[i],listA[i]) for i in np.arange(4)]
    A = [x[0:3] for x in dilatorSequence]
    return A


# The actual amplitude of the metric distorsion is not know. Considering that it is very, very small
# the metric displacement will be approximated by the sum of the 3D coefficients times the radial thickness
# hp is unknown
class dilator(object):
        def __init__(self,particle,axis,spin,ax,position=[0,0]):
            self.unit = {}
            self.ax=ax
            self.particle=particle
            self.dilatorSeq=getDilatorSequence(particle=particle, axis=axis, spin=spin)
            self.axis=axis
            self.center = [position + [i*np.pi/2 ]for i in np.arange(5)]
            self.spin=spin
        def plotMe(self):
            i=0
            max_radius = 2.5 * np.pi
            for t in self.dilatorSeq:
                self.unit[i]=unit(t,self.ax,self.center[i]).plotMe(ax)
                i=i+1
            plt.show()

# Radii corresponding to the coefficients:
class unit(object):
    def __init__(self,coeffs,ax,center=(0,0)):
        self.ax = ax
        self.coeffs=coeffs
        self.charge=np.sum(coeffs)
        print(self.charge)
        self.center=center
        # Scaling factor
        a=2
        self.rx, self.ry, self.rz = [(e/a+1.0) for e in coeffs]
        # Set of all spherical angles:
        self.u = np.linspace(0, 2 * np.pi, 100)
        self.v = np.linspace(0, np.pi, 100)
    def surface(self,center=(0,0,0)):
        # Cartesian coordinates that correspond to the spherical angles:
        # (this is the equation of an ellipsoid):
        u=self.u
        v=self.v
        x = (self.rx-1) * np.outer(np.cos(u), np.sin(v))+self.center[0]
        y = (self.ry-1) * np.outer(np.sin(u), np.sin(v))+self.center[1]
        z = (self.rz-1) * np.outer(np.ones_like(u), np.cos(v))+self.center[2]
        return x,y,z
    def plotMe(self,ax):
        # Plot:
        x,y,z = self.surface()
        color='g'
        if(self.charge<0):
            color='r'
        self.ax.plot_surface(x, y, z,  rstride=4, cstride=4, color=color)

if(__name__=='__main__'):
    # for spin in ['half', 'minus-half']:
    #     print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Spin=  ',spin)
    #     for particle in np.arange(4):
    #         print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  Particle=', particle)
    #         for axis in np.arange(3):
    #             print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  Axis=', axis)
    #             A = getDilatorSequence(particle=particle, axis=axis, spin=spin)
    #             print(' spin = ', spin, ' particle = ', particle, ' axis = ', axis)
    #             for t in A:
    #                 print(t)
    #             print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    fig = plt.figure(figsize=plt.figaspect(1))
    # Square figure
    ax = fig.add_subplot(111, projection='3d')
    getattr(ax, 'set_{}lim'.format('x'))((-np.pi / 4, np.pi / 4))
    getattr(ax, 'set_{}lim'.format('y'))((-np.pi / 4, np.pi / 4))
    getattr(ax, 'set_{}lim'.format('z'))((-np.pi / 4, 2.25 * np.pi))
    proton = dilator(particle=0,axis=0,ax=ax,spin='half',position=[0,0])
    proton.plotMe()
    a=1


