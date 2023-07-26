Python module abp.ellipsoidal2d.pairdistribution
=======================
This folder contains supplementary software for the article

*S. Bröker, M. te Vrugt, and R. Wittkowski, Collective dynamics and pair-distribution function of active Brownian ellipsoids, [TODO: arXiv link] (2023)*

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8186194.svg)](https://doi.org/10.5281/zenodo.8186194)

Contents
--------
* `abp/ellipsoidal2d/pairdistribution/`: Python module for simplified access to the fit parameters of the
Fourier coefficients given in the article as well as routines for
reconstruction of the pair distribution function.
See below for installation instructions.
The abellipsoids2d module includes:
-loadParameterFile         
    this function loads the CSV file from a given path
-reconstruct_g
    Returns an approximation for g in a given range of particle distances and
    positional and orientational angles.
              
* `demo.py`: Demo code for the `abellipsoids2d` module. See `python3 demo.py -h` for more
information.
* `doc/`: HTML documentation for the `abellipsoids2d` module.
* `abp/ellipsoidal2d/pairdistribution/Interpolation_parameters.csv`: Spreadsheet file containing all fit parameters for the
Fourier coefficients given in the article.
* `README.md`: This file.

Installation
------------
Reasonably recent versions of the following software are required to make use of
the supplied code:
* Python 3
* NumPy
* Matplotlib (needed for the demo script)

To install the Python module, copy or link the folder `abp` to a location in
your Python search path. You can find all locations in your search path by
running:

```bash
python3 -c "import sys; print('\n'.join(sys.path))"
```
