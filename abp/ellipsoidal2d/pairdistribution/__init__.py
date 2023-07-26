# -*- coding: utf-8 -*-

"""Module for approximating the pair distribution function of a 
    two-dimensional suspension of active Brownian ellipsoids."""

from ._reconstruct import *
# Trick pdoc3 into documenting submodule contents as members of this module
from ._reconstruct import __all__ as reconstruct_all
__all__ = reconstruct_all

__author__ = "Stephan Bröker, Michael te Vrugt, Raphael Wittkowski"
__copyright__ = "Copyright (c) 2023 Stephan Bröker, Michael te Vrugt, Raphael Wittkowski"
__license__ = "MIT"
__version__ = "1.0"
