"""
potential.py

Author: Adrian Del Maestro
Date: 2020-05-07

Implement various helium-helium interaction potentials.
"""

import numpy as np
import math
import sys
from dataclasses import dataclass
from types import MappingProxyType

import sys
from dataclasses import dataclass

# check for python version to use slots
_dataclass_kwargs = {"frozen": True}
if sys.version_info >= (3, 10):
    _dataclass_kwargs["slots"] = True


# compute some factorials
factorials = [math.factorial(i) for i in range(20)]

# ------------------------------------------------------------------------
def lennard_jones(r,ε=10.956,σ=2.6413813):
    r"""Lennard-Jones potential where ϵ in K and σ in Å.

       \begin{equation}
       V(r) = 4\varepsilon \left[\left(\frac{\sigma}{r}\right)^{12}
              - \left(\frac{\sigma}{r}\right)^6\right]
       \end{equation}
       
       Parameters taken from: R. A. Aziz, A. R. Janzen, and M. R. Moldover, 
       [Phys. Rev. Lett. 74, 1586 (1995)](https://doi.org/10.1103/PhysRevLett.74.1586)

    """
    x = σ/r
    return 4.0*ε*(x**12 - x**6)

# ------------------------------------------------------------------------
# Aziz Potential

@dataclass(**_dataclass_kwargs)
class AzizParams:
    ε: float
    rₘ:float
    D: float
    α: float
    β: float
    A: float
    C6: float
    C8: float
    C10: float
    doi: str

## The aziz parameters for different epochs
_AZIZ_1979 = AzizParams(
    ε=10.8,
    rₘ=2.9673,
    D=1.241314,
    α=13.353384,
    β=0.0,
    A=0.5448504e6,
    C6=1.3732412, 
    C8=0.4253785, 
    C10=0.1781,
    doi="10.1063/1.438007",
)

_AZIZ_1987 = AzizParams(
    ε=10.948,
    rₘ=2.9673,
    D=1.4826,
    α=10.43329537,
    β=-2.27965105,
    A=1.8443101e5,
    C6=1.36745214, 
    C8=0.42123807, 
    C10=0.17473318,
    doi="10.1080/00268978700101941",
)

_AZIZ_1995 = AzizParams(
    ε=10.956,
    rₘ=2.9683,
    D=1.438,
    α=10.5717543,
    β=-2.07758779,
    A=1.86924404e5,
    C6=1.35186623, 
    C8=0.4149514, 
    C10=0.17151143,
    doi="10.1103/PhysRevLett.74.1586",
)

_AZIZ = MappingProxyType({
    "1979": _AZIZ_1979,
    "1987": _AZIZ_1987,
    "1995": _AZIZ_1995,
})
    

# ------------------------------------------------------------------------
def __F(x,D): 
    if x >= D:
        return 1.0
    t = (D/x-1.0)**2
    return np.exp(-t)
F = np.vectorize(__F)

# ------------------------------------------------------------------------
def V_phenom(x, C6, C8, C10, D):
    x = np.asarray(x)
    t = (C6 / x**6) + (C8 / x**8) + (C10 / x**10)
    return F(x, D) * t

# ------------------------------------------------------------------------
def aziz(r, p: AzizParams):
    r"""Aziz Potential in kelvin

    1979: R. A. Aziz, V. P. S. Nain, J. S. Carley, W. L. Taylor, and G. T. McConville, 
    [J. of Chem. Phys. 70, 4330 (1979)](https://doi.org/10.1063/1.438007)

    1987: R. A. Aziz, F. McCourt, and C. Wong, 
    [Mol. Phys. 61, 1487 (1987)](https://doi.org/10.1080/00268978700101941)

    1995: R. A. Aziz, A. R. Janzen, and M. R. Moldover, 
    [Phys. Rev. Lett. 74, 1586 (1995)](https://doi.org/10.1103/PhysRevLett.74.1586)

    \begin{equation}
    V(r)= \varepsilon\left[A \exp (-\alpha x + \beta x^2)-F(x) \sum_{j=0}^{2}\frac{C_{2 j+6}}{x^{2 j+6}}\right]
    \label{eq:Vaziz}
    \end{equation}

    where

    \begin{equation}
    F(x)=
    \begin{cases}
    \exp \left[-\left(\frac{D}{x}-1\right)^{2}\right] &,&  x<D \\
    1 &,& x \geq D
    \end{cases}
    \end{equation}

    and 

    \begin{align}
    \varepsilon=10.8\ \mathrm{K}, & \qquad  C_{6}=1.3732412\\
    r_{m}=2.9673\ Å, &\qquad C_{8}=0.4253785\\
    D = 1.241314, &\qquad C_{10}=0.1781\\
    \alpha=13.353384, &\qquad  A=0.5448504 \times 10^{6} \\
    \beta = 0, & \\
    \end{align}
    """
    x = r / p.rₘ
    return p.ε * (
        p.A * np.exp(-p.α * x + p.β * x**2)
        - V_phenom(x, p.C6, p.C8, p.C10, p.D)
    )
    

def aziz_1995(r):
    r"""Aziz–Janzen–Moldover (1995). DOI: 10.1103/PhysRevLett.74.1586"""
    return aziz(r, _AZIZ_1995)

def aziz_1987(r):
    r"""Aziz-McCourt-Wong (1987). DOI: 10.1080/00268978700101941"""
    return aziz(r, _AZIZ_1987)

def aziz_1979(r):
    r""" Aziz-Nain-Carley-Taylor-McConville (1979). DOI: 10.1063/1.438007"""
    return aziz(r, _AZIZ_1979)


def available_aziz():
    return tuple(_AZIZ.keys())

def get_aziz(year: str):
    return _AZIZ[year]
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
def szalewicz_2012(r):
    r""" Returns the Szalewicz 2012 potential in kelvin

     ## References
     * M. Przybytek, W. Cencek, J. Komasa, G. Łach, B. Jeziorski, and K. Szalewicz, 
       [Phys. Rev. Lett. 104, 183003 (2010)](https://doi.org/10.1103/PhysRevLett.104.183003)
     * W. Cencek, M. Przybytek, J. Komasa, J. B. Mehl, B. Jeziorski, and K. Szalewicz, 
       [J. Chem. Phys. 136, 224303 (2012)](https://doi.org/10.1063/1.4712218)
     
     \begin{equation}
      V(R)= e^{-a R}\sum_{j=0}^{2}P_{j}R^j+e^{-b R}\sum_{j=0}^{1}Q_{j}R^j -\sum_{n=3}^{16} f_{n}(\eta R) \frac{C_{n}}{R^{n}}
     \end{equation}
     
     where $f_n(x)$ is the Tang-Toennies damping function:
     
     \begin{equation}
     f_{n}(x)=1-e^{-x} \sum_{k=0}^{n} \frac{x^{k}}{k !}
     \end{equation}
      
     ## Parameters
     | Parameter | Value | Parameter| Value |
     |-----------|-------|----------|-------|
     |$C_0$|0.0|$a$ | 3.64890303652830|
     |$C_1$|0.0|$b$|2.36824871743591|
     |$C_2$|0.0| η | 4.09423805117871|
     |$C_3$|0.000000577235|$P_0$ | -25.4701669416621|
     |$C_4$|-0.000035322| $P_1$ | 269.244425630616 |
     |$C_5$|0.000001377841|$P_2$ | -56.3879970402079|
     |$C_6$|1.461830|$Q_0$ | 38.7957487310071 |
     |$C_7$|0.0|$Q_1$ | -2.76577136772754|
     |$C_8$|14.12350|||
     |$C_9$|0.0|||
     |$C_{10}$|183.7497|||
     |$C_{11}$|-0.7674e2|||
     |$C_{12}$|0.3372e4|||
     |$C_{13}$|-0.3806e4|||
     |$C_{14}$|0.8534e5|||
     |$C_{15}$|-0.1707e6|||
     |$C_{16}$|0.286e7|||
      
     ## Conversion Factors
     Factors of 315774.65 from atomic units to kelvins and of 0.52917720859 from 
     bohrs to angstroms were assumed.
     """

    # convert from Angstrom to Bohr
    R = r/0.52917720859

    ε = 315774.65
    C = [0.0,
      0.0,
      0.0,
      0.000000577235,
      -0.000035322,
      0.000001377841,
      1.461830,
      0.0,
      14.12350,
      0.0,
      183.7497,
      -0.7674e2,
      0.3372e4,
      -0.3806e4,
      0.8534e5,
      -0.1707e6,
      0.286e7]
    a = 3.64890303652830
    b = 2.36824871743591
    η = 4.09423805117871
    P = [-25.4701669416621, 269.244425630616, -56.3879970402079]
    Q = [38.7957487310071, -2.76577136772754]
        
    t1 = 0.0
    for j in range(3):
        t1 += P[j]*R**j
    t1 *= np.exp(-a*R)
    
    t2 = 0.0
    for j in range(2):
        t2 += Q[j]*R**j
    t2 *= np.exp(-b*R)
    
    t3 = 0.0
    for n in range(3,17):
        t3 += f(n,η*R)*C[n]/R**n
    
    return ε*(t1+t2-t3)

# ------------------------------------------------------------------------
def f(n,x):
    """Tang-Toennies damping function."""
    s1 = 0.0
    for i in range(n+1):
        s1 += x**(i)/factorials[i]
    return 1.0 - (np.exp(-x)*s1)
