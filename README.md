[![PyPI version](https://badge.fury.io/py/heprops.svg)](https://badge.fury.io/py/heprops)

`heprops` is a simple python package implementing useful properties of the chemical element helium at low temperature

It includes experimental data and interpolation for the data found in the incredible and useful paper:

- James S. Brooks and Russell J. Donnelly, *The calculated thermodynamic properties of superfluid helium-4*, [J. Phys. Chem. Ref. Data **6** 51 (1977).](https://aip.scitation.org/doi/10.1063/1.555549)

Most of the data in this paper was available on the late Russel Donnelly's former website http://pages.uoregon.edu/rjd which has since been taken offline but it is still available via a 2015 snapshot on the [WayBackMachine](https://web.archive.org/web/20150620225058/http://pages.uoregon.edu/rjd/bd.htm).

The library also implements a number of historical and modern intramolecular interaction potentials for helium atoms.  Details of these are taken from the following papers:

- R. A. Aziz, V. P. S. Nain, J. S. Carley, W. L. Taylor, and G. T. McConville, *An accurate intermolecular potential for helium*, [J. of Chem. Phys. 70, 4330 (1979).](https://doi.org/10.1063/1.438007)
- R. A. Aziz, F. McCourt, and C. Wong, *A new determination of the ground state interatomic potential for He<sub>2</sub>*, [Mol. Phys. 61, 1487 (1987).](https://doi.org/10.1080/00268978700101941)
- R. A. Aziz, A. R. Janzen, and M. R. Moldover, *Ab Initio Calculations for Helium: A Standard for Transport Property Measurements*, [Phys. Rev. Lett. 74, 1586 (1995).](https://doi.org/10.1103/PhysRevLett.74.1586)
- M. Przybytek, W. Cencek, J. Komasa, G. Łach, B. Jeziorski, and K. Szalewicz, *Relativistic and Quantum Electrodynamics Effects in the Helium Pair Potential*, [Phys. Rev. Lett. 104, 183003 (2010).](https://doi.org/10.1103/PhysRevLett.104.183003)
- W. Cencek, M. Przybytek, J. Komasa, J. B. Mehl, B. Jeziorski, and K. Szalewicz, *Effects of adiabatic, relativistic, and quantum electrodynamics interactions on the pair potential and thermophysical properties of helium*, [J. Chem. Phys. 136, 224303 (2012).](https://doi.org/10.1063/1.4712218)


## Supported Python Versions
Python >= 3.6 (for f-strings)

## Installation
To install via pip:

    pip install heprops

Or from within a notebook:

```python
import sys
!{sys.executable} -m pip install heprops
```


## Usage
The package implements two modules: `helium` which contains a number of functions that return the thermodynamics properties of helium and `potential` which implements the pair-potentials.  For example:

```python
from heprops import helium,potential
import numpy as np

T = np.linspace(0.5,2.5,5)

# the superfluid fraction
ρsoρ = helium.superfluid_fraction_SVP(T)
print(f'ρs/ρ(T) = {ρsoρ}')

# the coherence length
ξ = helium.ξ(T)
print(f'ξ(T) = {ξ} Å')

# Interaction Potential
V = potential.szalewicz_2012
r = np.linspace(2.5,5,1000)
rₘ = r[np.argmin(V(r))]
print(f'rₘ = {rₘ:6.3f} Å')
```
    ρs/ρ(T) = [1.    0.993 0.889 0.447 0.   ]
    ξ(T) = [4.11100244e-10 5.21483803e-10 7.56156315e-10 1.86293613e-09 1.24228114e-09] Å
    rₘ =  2.968 Å 

## Examples

A notebook including detailed examples of how to plot and compare the different interaction potentials is included in the `examples` directory at [examples/he_potential_examples.ipynb](./examples/he_potential_examples.ipynb).

<img src="https://raw.githubusercontent.com/agdelma/heprops/master/examples/potential_comparison.svg" width="400px">


## Support

The creation of this software was supported in part by the National Science Foundation under Award Nos. DMR-1808440 and DMR-1809027.

[<img width="100px" src="https://www.nsf.gov/images/logos/NSF_4-Color_bitmap_Logo.png">](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1808440)

