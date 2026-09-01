# Shortcuts

The `groupsmath.shortcuts` module provides short aliases for several group constructors defined in `groupsmath`.

Instead of writing the complete constructor name, the module allows common groups to be created using a shorter notation.

```python
from groupsmath.shortcuts import *

G = C(5)
```

This is equivalent to using:

```python
from groupsmath.core import cyclic_group

G = cyclic_group(5)
```

The module itself does not implement new group types or new mathematical operations. It only exposes alternative names for constructors imported from `core`.

---

## Available shortcuts

The module defines the following aliases:

| Shortcut | Original constructor | Meaning |
|---|---|---|
| `C` | `cyclic_group` | Cyclic group |
| `S` | `symmetric_group` | Symmetric group |
| `A` | `alternating_group` | Alternating group |
| `D` | `dihedric_group` | Dihedral group |
| `U` | `units_group` | Group of units |
| `Dic` | `dicyclic_group` | Dicyclic group |
| `Tet` | `tetrahedral_group` | Tetrahedral group |
| `Cub` | `octahedral_group` | Octahedral group |
| `Oct` | `octahedral_group` | Octahedral group |
| `Dod` | `icosahedral_group` | Icosahedral group |
| `Ico` | `icosahedral_group` | Icosahedral group |

The aliases are assigned directly:

```python
C = cyclic_group
S = symmetric_group
A = alternating_group
D = dihedric_group
U = units_group
Dic = dicyclic_group
Tet = tetrahedral_group
Cub = octahedral_group
Oct = octahedral_group
Dod = icosahedral_group
Ico = icosahedral_group
```

Therefore, each shortcut is the same Python callable as its corresponding constructor.

---

# `C` — Cyclic groups

```python
C = cyclic_group
```

`C` is the shortcut for `cyclic_group`.

For example:

```python
G = C(6)
```

is equivalent to:

```python
G = cyclic_group(6)
```

The exact arguments accepted by `C` are therefore the same as those accepted by `cyclic_group`.

---

# `S` — Symmetric groups

```python
S = symmetric_group
```

`S` is the shortcut for `symmetric_group`.

For example:

```python
G = S(4)
```

is equivalent to:

```python
G = symmetric_group(4)
```

---

# `A` — Alternating groups

```python
A = alternating_group
```

`A` is the shortcut for `alternating_group`.

For example:

```python
G = A(5)
```

is equivalent to:

```python
G = alternating_group(5)
```

---

# `D` — Dihedral groups

```python
D = dihedric_group
```

`D` is the shortcut for `dihedric_group`.

For example:

```python
G = D(4)
```

is equivalent to:

```python
G = dihedric_group(4)
```

The shortcut preserves the spelling used by the underlying constructor: `dihedric_group`.

---

# `U` — Groups of units

```python
U = units_group
```

`U` is the shortcut for `units_group`.

For example:

```python
G = U(10)
```

is equivalent to:

```python
G = units_group(10)
```

The shortcut is particularly convenient when working with several standard group constructions in the same file.

---

# `Dic` — Dicyclic groups

```python
Dic = dicyclic_group
```

`Dic` is the shortcut for `dicyclic_group`.

For example:

```python
G = Dic(3)
```

is equivalent to:

```python
G = dicyclic_group(3)
```

---

# `Tet` — Tetrahedral groups

```python
Tet = tetrahedral_group
```

`Tet` is intended as the shortcut for `tetrahedral_group`.

The alias is defined directly in `shortcuts.py`:

```python
Tet = tetrahedral_group
```

Therefore:

```python
Tet(...)
```

calls the same function as:

```python
tetrahedral_group(...)
```

The exact arguments and behaviour are inherited from `tetrahedral_group` in `core.py`.

---

# `Cub` and `Oct` — Octahedral groups

The module defines:

```python
Cub = octahedral_group
Oct = octahedral_group
```

Thus both `Cub` and `Oct` refer to the **same constructor**:

```python
octahedral_group
```

Consequently:

```python
Cub(...)
```

and:

```python
Oct(...)
```

are equivalent.

The names are provided as separate shortcuts, presumably to offer both a cube-oriented and octahedron-oriented abbreviation, but they do not currently refer to different constructors.

In particular:

```python
Cub is Oct
```

is true because both variables point to the same function object imported from `core`.

---

# `Dod` and `Ico` — Icosahedral groups

Similarly, the module defines:

```python
Dod = icosahedral_group
Ico = icosahedral_group
```

Both shortcuts therefore refer to the same constructor:

```python
icosahedral_group
```

Thus:

```python
Dod(...)
```

and:

```python
Ico(...)
```

are equivalent.

As with `Cub` and `Oct`, the two names provide alternative terminology without creating different group constructors.

---

# Why use shortcuts?

The main purpose of `shortcuts` is convenience.

Compare:

```python
from groupsmath.core import (
    cyclic_group,
    symmetric_group,
    alternating_group,
    dihedric_group
)

C5 = cyclic_group(5)
S4 = symmetric_group(4)
A5 = alternating_group(5)
D4 = dihedric_group(4)
```

with:

```python
from groupsmath.shortcuts import *

C5 = C(5)
S4 = S(4)
A5 = A(5)
D4 = D(4)
```

The second form is shorter and can make examples involving many standard groups more compact.

---

# The module does not wrap the constructors

The shortcuts are direct aliases, not wrapper functions.

For example:

```python
C = cyclic_group
```

does not create a new function that calls `cyclic_group`.

It simply gives the existing function another name.

Therefore the following are equivalent:

```python
C(5)
```

and:

```python
cyclic_group(5)
```

The same applies to every shortcut in the module.

---

# Complete shortcut table

The complete mapping implemented by `shortcuts.py` is:

```text
C      → cyclic_group
S      → symmetric_group
A      → alternating_group
D      → dihedric_group
U      → units_group
Dic    → dicyclic_group
Tet    → tetrahedral_group
Cub    → octahedral_group
Oct    → octahedral_group
Dod    → icosahedral_group
Ico    → icosahedral_group
```

There are two pairs of alternative names:

```text
Cub = Oct = octahedral_group
Dod = Ico = icosahedral_group
```

while `Tet` is mapped independently to `tetrahedral_group`.

---

# Usage example

```python
from groupsmath.shortcuts import *

C5 = C(5)
S3 = S(3)
A5 = A(5)
D4 = D(4)
U8 = U(8)
Dic3 = Dic(3)

TetG = Tet()
CubG = Cub()
OctG = Oct()
DodG = Dod()
IcoG = Ico()
```

The last four names illustrate the aliasing behaviour:

```python
CubG = Cub()
OctG = Oct()
```

use the same underlying constructor, while:

```python
DodG = Dod()
IcoG = Ico()
```

also use the same underlying constructor.

---

## Summary

`groupsmath.shortcuts` is a convenience module.

It exposes short names for standard group constructors already implemented in `groupsmath.core`:

- `C` → cyclic
- `S` → symmetric
- `A` → alternating
- `D` → dihedral
- `U` → units
- `Dic` → dicyclic
- `Tet` → tetrahedral
- `Cub` → octahedral
- `Oct` → octahedral
- `Dod` → icosahedral
- `Ico` → icosahedral

No new group implementation is introduced by this module. All mathematical behaviour comes from the corresponding functions in `core.py`.
