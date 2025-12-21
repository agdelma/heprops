# Installation

## Install from PyPI

```bash
python -m pip install heprops
```

## Install from source

From a clone of the repository:

```bash
python -m pip install -e .
```

## Local documentation build

From the repository root:

```bash
python -m pip install -e .
python -m pip install -r docs/requirements.txt
mkdocs serve
```

Then open the local URL printed by `mkdocs serve`.

!!! note
    The API reference uses `mkdocstrings`, which imports the package. If you add new dependencies to `heprops`, make sure they are installed in the docs build environment (locally and in CI).
