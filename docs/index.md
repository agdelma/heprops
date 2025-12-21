# heprops

`heprops` is a simple python package implementing useful properties of the chemical element helium at low temperature

It includes experimental data and interpolation for the data found in the incredible and useful paper:

- James S. Brooks and Russell J. Donnelly, *The calculated thermodynamic properties of superfluid helium-4*, [J. Phys. Chem. Ref. Data **6** 51 (1977).](https://aip.scitation.org/doi/10.1063/1.555549)

Most of the data in this paper is available on the late Russel Donnelly's former website <http://pages.uoregon.edu/rjd> which may be taken offline but it is still available via a 2015 snapshot on the [WayBackMachine](https://web.archive.org/web/20150620225058/http://pages.uoregon.edu/rjd/bd.htm).

The library also implements a number of historical and modern intramolecular interaction potentials for helium atoms.  Details of these are taken from the following papers:

- R. A. Aziz, V. P. S. Nain, J. S. Carley, W. L. Taylor, and G. T. McConville, *An accurate intermolecular potential for helium*, [J. of Chem. Phys. 70, 4330 (1979).](https://doi.org/10.1063/1.438007)
- R. A. Aziz, F. McCourt, and C. Wong, *A new determination of the ground state interatomic potential for He<sub>2</sub>*, [Mol. Phys. 61, 1487 (1987).](https://doi.org/10.1080/00268978700101941)
- R. A. Aziz, A. R. Janzen, and M. R. Moldover, *Ab Initio Calculations for Helium: A Standard for Transport Property Measurements*, [Phys. Rev. Lett. 74, 1586 (1995).](https://doi.org/10.1103/PhysRevLett.74.1586)
- M. Przybytek, W. Cencek, J. Komasa, G. Łach, B. Jeziorski, and K. Szalewicz, *Relativistic and Quantum Electrodynamics Effects in the Helium Pair Potential*, [Phys. Rev. Lett. 104, 183003 (2010).](https://doi.org/10.1103/PhysRevLett.104.183003)
- W. Cencek, M. Przybytek, J. Komasa, J. B. Mehl, B. Jeziorski, and K. Szalewicz, *Effects of adiabatic, relativistic, and quantum electrodynamics interactions on the pair potential and thermophysical properties of helium*, [J. Chem. Phys. 136, 224303 (2012).](https://doi.org/10.1063/1.4712218)

Source code: `agdelma/heprops` on GitHub.

## Citation
[![DOI](https://zenodo.org/badge/261878594.svg)](https://zenodo.org/badge/latestdoi/261878594)

```bibtex 
@article{HePropsSoftware,
  author = {Adrian {Del} Maestro},
  title = {{agdelma/heprops: Low Temperatue Properties of Helium}},
  journal = {\url{https://github.com/agdelma/heprops}},
  publisher = {Zenodo},
  year = {2021},
  doi = {10.5281/zenodo.4601527},
  url = {https://doi.org/10.5281/zenodo.4601527}
}
```

## Quick start

```python
from heprops import helium, potential
import numpy as np

# Temperature grid (Kelvin)
T = np.linspace(0.5, 2.5, 5)

# Superfluid fraction along SVP
rho_s_over_rho = helium.superfluid_fraction_SVP(T)

# Coherence length (Å). Note: the function name is the Greek letter xi.
xi = helium.ξ(T)

# One of the implemented He–He pair potentials
V = potential.szalewicz_2012
r = np.linspace(2.5, 5.0, 1000)  # Å
r_min = r[np.argmin(V(r))]

print(rho_s_over_rho)
print(xi)
print(r_min)
```
