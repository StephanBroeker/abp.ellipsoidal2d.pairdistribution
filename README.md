Python module abp.ellipsoids2d.pairdistribution
=======================
This folder contains accompanying software for the article

*S. Bröker, M. te Vrugt and R. Wittkowski, Collective dynamics and pair-distribution function
of active Brownian ellipsoids, [TODO: arXiv link] (2023)*

Contents
--------
* `abellipsoids2d/`: Python module for simplified access to the fit parameters of the
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
* `Interpolation_parameters.csv`: Spreadsheet file containing all fit parameters for the
Fourier coefficients given in the article.
* `README.md`: This file.

Installation
------------
Reasonably recent versions of the following software are required to make use of
the supplied code:
* Python 3
* NumPy
* Matplotlib (needed for the demo script)

To install the Python module, copy or link the folder `abellipsoids2d` to a location in
your Python search path. You can find all locations in your search path by
running:

```bash
python3 -c "import sys; print('\n'.join(sys.path))"
```
