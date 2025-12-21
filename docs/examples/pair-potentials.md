# Pair potentials

## Evaluate a potential

The `heprops.potential` module exposes several named He–He pair potentials as callables.

Example using the (Przybytek/Cencek/Komasa/Szalewicz) 2012 potential:

```python
from heprops import potential
import numpy as np

V = potential.szalewicz_2012
r = np.linspace(2.0, 10.0, 2000)  # Å
V_r = V(r)
```

## Locate the minimum

```python
r0 = r[np.argmin(V_r)]
V0 = V_r.min()
print(r0, V0)
```

## Plot

```python
import matplotlib.pyplot as plt

plt.plot(r, V_r)
plt.xlabel("r [Å]")
plt.ylabel("V(r)")
plt.grid(True)
plt.show()
```

## Comparing multiple potentials

You can compare any subset of potentials by evaluating each on the same `r` grid and overlaying curves.

The repository also includes a notebook with a more complete comparison:

- `examples/he_potential_examples.ipynb`

For the full list of implemented potentials, see the [API Reference](../api/potential.md).
