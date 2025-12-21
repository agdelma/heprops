# Thermodynamic queries

## Superfluid fraction along SVP

Compute the superfluid fraction as a function of temperature:

```python
from heprops import helium
import numpy as np

T = np.linspace(0.5, 2.5, 200)  # K
rho_s_over_rho = helium.superfluid_fraction_SVP(T)
```

Plotting example:

```python
import matplotlib.pyplot as plt

plt.plot(T, rho_s_over_rho)
plt.xlabel("T [K]")
plt.ylabel(r"$\\rho_s/\\rho$")
plt.grid(True)
plt.show()
```

## Coherence length

The module provides a coherence length function named with the Greek letter xi:

```python
from heprops import helium
import numpy as np

T = np.array([0.7, 1.0, 1.5])  # K
xi = helium.ξ(T)  # Å
```

If you want to avoid typing the Unicode symbol:

```python
xi = getattr(helium, "ξ")(T)
```

## General pattern

Most functions in `heprops.helium` are callable on scalars and NumPy arrays. For a full list, see the [API Reference](../api/helium.md).
