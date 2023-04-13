"""Functions for both fitting procedures of the Fourier coefficients of g.

For the functions of the first fitting procedure the order of arguments matches
the one shown in the row headers for each Fourier coefficient in Interpolation_parameters.csv.
Likewise for the functions of the second fitting procedure matches the order of
arguments shown in the header line in Interpolation_parameters.csv."""

from numpy import sqrt, exp, pi, tanh
from scipy.special import erfc

# -- Functions for first fitting procedure --

def EMG(r, mu, om, la):
    """Exponentially modified Gaussian distribution."""
    return la/2 * exp(la/2 * (la*om**2 - 2*(r-mu))) * \
        erfc((la*om**2 - (r-mu))/sqrt(2)/om)

def Gauss(r, mu, om):
    """ Gauss distribution """
    return 1/(sqrt(2*pi)*om) * exp(-1/2*((r-mu)/om)**2)


def EMG_tanh(r,a,mu,om,la, l2):
    """ Function for first fitting procedure. Sum of EMG and tan hyperbolicus """
    return a*EMG(r,mu,om,la)+(((tanh((r-mu)*l2)+1)*0.5))

def Gauss_plus_Gauss(r, a1, mu1, om1, a2, mu2, om2):
    """ Function for first fitting procedure. Sum of two Gauss functions """
    return a1*Gauss(r, mu1, om1)+ a2*Gauss(r, mu2, om2)

def EMG_quad(r,a,mu,om,la,l1, l2 ):
    """ Function for first fitting procedure. Product of EMG and quadratic polynom """
    return a*EMG(r,mu,om,la)*(r*r + l1*r + l2)    

def Gauss_a(r, a, mu, om):
    """ Function for first fitting procedure. Gauss distribution with factor """
    return a*Gauss(r, mu, om)

def EMG_quad_lin(r,a,mu,om,la,l1, l2, l3):
    """ Function for first fitting procedure. 
        Product of EMG and quadratic and linear polynom """
    return a*EMG(r,mu,om,la)*(r*r + l1*r + l2)*(r - l3)    

def EMG_lin_lin(r,a,mu,om,la,l1, l2 ):
    """ Function for first fitting procedure. 
        Product of EMG and two linear polynoms """    
    return a*EMG(r,mu,om,la)*(r-l1)*(r-l2)    

def EMG_lin(r,a,mu,om,la,l1):
    """ Function for first fitting procedure. 
        Product of EMG and a linear polynom """     
    return a*EMG(r,mu,om,la)*(r-l1)

def EMG_lin_lin_lin(r,a,mu,om,la,l1, l2, l3 ):
    """ Function for first fitting procedure. 
        Product of EMG and three linear polynoms """     
    return a*EMG(r,mu,om,la)*(r-l1)*(r-l2)*(r-l3)

def Gauss_lin_lin(r, a, mu, om, l1, l2):
    """ Function for first fitting procedure. 
        Product of Gauss and two linear polynoms """     
    return Gauss_a(r, a, mu, om)*(r-l1)*(r-l2)

def Gauss_lin(r, a, mu, om, l1):
    """ Function for first fitting procedure. 
        Product of Gauss and a linear polynom. """     
    return Gauss_a(r, a, mu, om)*(r-l1)


FOURIERFITFUNCS = {
    (1,0,0) : EMG_tanh,
    (1,0,1) : Gauss_plus_Gauss,
    (1,0,2) : EMG_quad,
    (1,0,3) : Gauss_a,
    (1,1,0) : EMG_quad,
    (1,1,1) : EMG_quad_lin,
    (1,1,2) : EMG_quad_lin,
    (1,1,3) : Gauss_a,
    (1,2,0) : EMG_lin_lin,
    (1,2,1) : EMG_lin,
    (1,2,2) : EMG_lin,
    (1,2,3) : Gauss_a,
    (1,3,0) : EMG_lin_lin_lin,
    (1,3,1) : Gauss_lin_lin,
    (1,3,2) : EMG_lin,
    (1,3,3) : EMG_lin_lin,
    (2,1,1) : EMG_quad,
    (2,1,2) : EMG_quad,
    (2,1,3) : EMG_lin_lin,
    (2,2,1) : EMG_lin,
    (2,2,2) : EMG_lin_lin,
    (2,2,3) : Gauss_lin_lin,
    (2,3,1) : Gauss_lin,
    (2,3,2) : EMG_lin_lin,
    (2,3,3) : EMG_lin_lin
}
"""Dictionary mapping the index triple (k,h,j) to the corresponding fit function
   k = 1 corresponds to cos cos functions, k = 2 corresponds to sin sin functions, 
   h corresponds to the frequency of the first angle and j to the frequency of the second angle"""

# -- Functions for second fitting procedure --

def h(x, u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u15,u16,u17,u18,u19,u20):
    """Function h for second fitting procedure."""
    Pe, dens = x
    return u1 /Pe + u2 /sqrt(Pe) + u3  + u4 *sqrt(Pe) + u5 *Pe + \
          (u6 /Pe + u7 /sqrt(Pe) + u8  + u9 *sqrt(Pe) + u10*Pe)*dens + \
          (u11/Pe + u12/sqrt(Pe) + u13 + u14*sqrt(Pe) + u15*Pe)*dens**2 +  \
          (u16/Pe + u17/sqrt(Pe) + u18 + u19*sqrt(Pe) + u20*Pe)*dens**3


PARAMETERFITFUNCS = {
    (1,0,0) : [h,h,h,h,h],
    (1,0,1) : [h,h,h,h,h,h],
    (1,0,2) : [h,h,h,h,h,h],
    (1,0,3) : [h,h,h],
    (1,1,0) : [h,h,h,h,h,h],
    (1,1,1) : [h,h,h,h,h,h,h],
    (1,1,2) : [h,h,h,h,h,h,h],
    (1,1,3) : [h,h,h],
    (1,2,0) : [h,h,h,h,h,h],
    (1,2,1) : [h,h,h,h,h],
    (1,2,2) : [h,h,h,h,h],
    (1,2,3) : [h,h,h],
    (1,3,0) : [h,h,h,h,h,h,h],
    (1,3,1) : [h,h,h,h,h],
    (1,3,2) : [h,h,h,h,h],
    (1,3,3) : [h,h,h,h,h,h],
    (2,1,1) : [h,h,h,h,h,h],
    (2,1,2) : [h,h,h,h,h,h],
    (2,1,3) : [h,h,h,h,h,h],
    (2,2,1) : [h,h,h,h,h],
    (2,2,2) : [h,h,h,h,h,h],
    (2,2,3) : [h,h,h,h,h],
    (2,3,1) : [h,h,h,h],
    (2,3,2) : [h,h,h,h,h,h],
    (2,3,3) : [h,h,h,h,h,h]
}
"""Dictionary mapping the index triple (k,h,j) to the corresponding fit parameters of the Former fitting procedure
   k = 1 corresponds to cos cos functions, k = 2 corresponds to sin sin functions, 
   h corresponds to the frequency of the first angle and j to the frequency of the second angle"""
