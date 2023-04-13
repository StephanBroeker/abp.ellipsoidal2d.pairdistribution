import argparse

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

import abellipsoids2d

# -- Parse args --

parser = argparse.ArgumentParser(
    description=r"""Display the pair distribution function for a given particle
        distance, Peclet number and packing density and one fixed angle at a certain value.
        The default values are the same as in Fig. 3 of the accompanying
        article by S. Broeker and R. Wittkowski.
        """)
parser.add_argument(
    "-r", metavar="dist", dest="dist", type=float, default=1.0,
    help="Particle distance in multiples of sigma (default: 1)")
parser.add_argument(
    "-d", metavar="Phi", dest="Phi", type=float, default=0.2,
    help="Packing density (default: 0.2)")
parser.add_argument(
    "-p", metavar="peclet", dest="peclet", type=float, default=10.0,
    help="Peclet number (default: 10)")


args = parser.parse_args()

# Validate args

r_min = 0.0
r_max = 10
if args.dist < r_min or args.dist > r_max:
    print("Warning: Distance is outside of approximation bounds!")

if args.peclet < 0:
    print("Warning: Unphysical argument for Peclet number")
if args.Phi < 0 or args.Phi > 1:
    print("Warning: Unphysical argument for packing density")

# -- Calculate pair distribution function --

# Generate arrays for r, phi1 and phi2

resolution = 180
phi1 = np.linspace(0, 2*np.pi, resolution, endpoint=False)
phi2 = np.linspace(0, 2*np.pi, resolution, endpoint=False)
r = args.dist  # Just take a single distance
phi1, phi2 = np.meshgrid(phi1, phi2, indexing='ij')
# Calculate g
g = abellipsoids2d.reconstruct_g(r, phi1, phi2, args.peclet, args.Phi)[0]


# g is two dimensional;



xlabel = r"$\phi_1$"
ylabel = r"$\phi_2$"

# -- Plotting code --

fig, ax = plt.subplots(1)

g = np.roll(g, 90, 0)
cax = ax.imshow(g.T, cmap="inferno", origin="lower",
                extent=(0, g.shape[0], 0, g.shape[0]))
cbar = fig.colorbar(cax)

cbar.set_label("$g$")

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

ax.set_xticks([0, g.shape[0]//2, g.shape[0]])
ax.set_xticklabels([r"$-\pi$", r"0", r"$\pi$"])
ax.xaxis.set_minor_locator(MultipleLocator(g.shape[0]//4))

ax.set_yticks([0, g.shape[0]//2, g.shape[0]])
ax.set_yticklabels(["0", r"$\pi$", r"$2\pi$"])
ax.yaxis.set_minor_locator(MultipleLocator(g.shape[0]//4))

plt.title(r"$r = " + str(r) + r"$")
plt.show()
