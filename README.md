`heprops` is a simple python package implementing useful properties of the chemical element helium at low temperature

It includes experimental data and interpolation for the data found in the incredible and useful paper:

- James S. Brooks and Russell J. Donnelly, *The calculated thermodynamic properties of superfluid helium-4*, [J. Phys. Chem. Ref. Data **6** 51 (1977).](https://aip.scitation.org/doi/10.1063/1.555549)


Most of the data in this paper was available on the late Russel Donnelly's former website http://pages.uoregon.edu/rjd which has since been taken offline but it is still available via a 2015 snapshot on the [WayBackMachine](https://web.archive.org/web/20150620225058/http://pages.uoregon.edu/rjd/bd.htm).

## Supported Python Versions
Python >= 3.6 (for f-strings)

## Installation
To install via pip:

    pip install heprops

## Usage
At present the package has a single module `helium` which contains a number of functions that return the thermodynamics properties of helium.  For example:

```python
from heprops import helium
import numpy as np

T = np.linspace(0.5,2.5,5)

# the superfluid fraction
ρsoρ = helium.superfluid_fraction_SVP(T)
print(ρsoρ)

# the coherence length
ξ = helium.ξ(T)
print(ξ)
```
    [1.    0.993 0.889 0.447 0.   ]
    [4.11100244e-10 5.21483803e-10 7.56156315e-10 1.86293613e-09 1.24228114e-09]    

## Support

The creation of this software was supported in part by the National Science Foundation under Award Nos. DMR-1808440 and DMR-1809027.

[<img width="100px" src="https://www.nsf.gov/images/logos/NSF_4-Color_bitmap_Logo.png">](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1808440)

