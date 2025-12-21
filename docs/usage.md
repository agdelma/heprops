# Usage

`heprops` exposes two main modules:

- `heprops.helium`: thermodynamic properties of helium at low temperature.
- `heprops.potential`: He–He pair interaction potentials.

Most functions are **NumPy-vectorized**: you can pass scalars or `numpy.ndarray` and get back arrays.

## Import pattern

```python
from heprops import helium, potential
```

## Units and conventions

Units follow the conventions used in the original data sources and in the existing package examples. In practice:

- Temperatures are in **Kelvin**.
- Lengths used in the pair potentials are in **Å**.
- Many thermodynamic properties are returned in the units stated in each function docstring.

When in doubt, check the API docs for the specific function.

## Greek-letter function names

The `heprops.helium` module includes at least one function named with a Unicode Greek letter (`ξ`). Depending on your editor and font, you may prefer one of these options:

```python
# Direct attribute access (works if your editor can type the symbol)
xi = helium.ξ(T)

# Or, avoid typing the symbol
xi = getattr(helium, "ξ")(T)
```

If you add ASCII aliases in the code (e.g. `xi = ξ`), mkdocstrings will document both.
