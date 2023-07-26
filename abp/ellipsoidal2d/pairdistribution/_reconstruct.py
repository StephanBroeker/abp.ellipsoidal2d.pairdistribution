#!/usr/bin/env python3

import os.path
import numpy as np

from .fitfuncs import FOURIERFITFUNCS, PARAMETERFITFUNCS

__all__ = ["loadParameterFile", "reconstruct_g"] 

# -- Internal constants for loading the default parameter file --

SCRIPTDIR = os.path.dirname(os.path.abspath(__file__))
FITPARAMSFILE = "Interpolation_parameters.csv"
DEFAULTPATH = os.path.join(SCRIPTDIR, FITPARAMSFILE)
DEFAULTPARAMETERS = None # Lazy loading: will be set when needed

# -- Simulation constants --

EPSILON, SIGMA = 1,1

# -- File input --

def loadParameterFile(filepath):
    r"""Load a parameter CSV file from a given path.

    Args:
        path (str):
            Path to CSV file.

    Returns:
        **params (dict):**
            Dictionary containing all fit parameters
            for the Fourier coefficients.
    """
    params = {}
    # Open file with fit parameters and read line by line every u_i,j
    # or v,w resp.
    with open(filepath) as f:
        for line in f:
            # Extract cells
            cells = line.split(",")
            # Skip lines without label
            if cells[0] == "k index for cos or sin":
                continue
            if cells[0] == "":
                continue                
            # Skip invalid labels
            if not len(cells) in [25]:
                print("Invalid fourier coefficient label: {}".format(cells[:]))
                continue
            coefftype = cells[0] # Either "coscos" or "sinsin"

            h,j = map(int, cells[1:3])

            # Select correct dict
            k = 1 if coefftype == "coscos" else 2

            # Filter empty cells
            # cells = list(filter(lambda x: x != "", cells))
            if not (k,h,j) in params:
                params[(k,h,j)] = []
            params[(k,h,j)].append(list(map(float, cells[5:]))) # Extract data
        return params

# Internally used
def loadDefaultParameterFile():
    global DEFAULTPARAMETERS
    if not DEFAULTPARAMETERS:
        DEFAULTPARAMETERS = loadParameterFile(DEFAULTPATH)
    return DEFAULTPARAMETERS

# -- Reconstruction functions --

def reconstruct_g(
        r, phi1, phi2, Pe, Phi, params=None):
    #    r, phi1, phi2, Pe, Phi, params=None):
    r"""Returns an approximation for $g$ in a given range of particle
    distances and positional and orientational angles.

    Args:
        r (float or array_like): Distance(s) at which $g$ will be calculated

        phi1, phi2 (float, array_like or meshgrid of all): Positional
            and orientational angles at which $g$ will be calculated
        Pe, Phi (float): Peclet number and Packing density for which $g$ 
            will be calculated
        params (dict):
            Parameter dictionary containing all fit parameters necessary for
            reconstruction. If not set, the included default values will be used.
    """
    # If params are not set: load default
    if not params:
        params = loadDefaultParameterFile()
        # if not params_alpha:
        #     params_alpha = params[0]
        # if not params_beta:
        #     params_beta = params[1]
    # r must have dimension 1
    if len(np.shape(r)) == 0:
        r = np.array([r])

    # Allocate array for g
    if len(np.shape(phi1))==2 and len(np.shape(phi2))==2:
        pass
    elif len(np.shape(phi1)) in [0,1] and len(np.shape(phi2)) in [0,1]:
        phi1, phi2 = np.meshgrid(phi1, phi2, indexing = 'ij')
    else:
        print("""I dont know how to interpret the input of phi1 and phi2.\n
        Please either give only onedimensional arrays or floats as input or give only meshgrids. """)




    g = np.zeros((r.shape[0], phi1.shape[0], phi2.shape[1]))


    # Calculate all contributions for k,h,j between for k in [1,2] and h,j in [0,1,2,3] or [1,2,3] 

    for k in [1,2]:
        # cos*cos for k = 1
        # sin*sin for k = 2
        lowest_freq = 0
        fourierfunc = np.cos
        if k==2:
            lowest_freq = 1
            fourierfunc = np.sin
        for h in range(lowest_freq,4,1):
            for j in range(lowest_freq,4,1):


                # Calculate fit parameters a, mu, omega, lambda, la, l1, l2 ...
                # (if necessary)
                fitparams = list(map(lambda x : x[0]((Pe, Phi), *x[1]),
                    zip(PARAMETERFITFUNCS[(k,h,j)], params[(k,h,j)])))
                # Calculate Fourier coefficient
                
                fouriercoeff = FOURIERFITFUNCS[(k,h,j)](r, *fitparams)
                # print(k, " ", h , " ", j , " " , fouriercoeff)
                
                # Add contribution to g
                g += fouriercoeff[:, None,None] * \
                fourierfunc(phi1*h) * fourierfunc(phi2*j)


    return g
