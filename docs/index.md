# GroupsMath

![GroupsMath Logo](https://raw.githubusercontent.com/MarioSultan/GroupsMath/main/logo.png)

**GroupsMath** is an open-source Python library designed to make group theory computational, intuitive, and accessible. It allows you to construct mathematical groups, work directly with their elements, and explore their structure through computations: from basic properties such as element orders, inverses, centers, and commutativity to more advanced concepts such as subgroups, cosets, quotient groups, automorphisms, direct and semidirect products, conjugacy classes, commutators, and matrix groups. GroupsMath also provides ready-to-use families of common groups and tools for visualizing Cayley tables, making it possible to move naturally between abstract mathematical ideas and concrete computational experiments. Its main goal is to provide a practical environment where group theory can be explored, tested, and understood through Python, whether for learning, teaching, experimentation, or mathematical computation.


---

## Installation

To install GroupsMath from PyPI, write in the terminal the following:

```bash
pip install groupsmath
```

If you want to try GroupsMath before installing anything, click this button:

[![Launch Binder](https://raw.githubusercontent.com/MarioSultan/GroupsMath/main/imgs/here.png)](https://mybinder.org/v2/gh/MarioSultan/GroupsMath/main?labpath=GroupsMath_demo.ipynb)

---

## Getting started

GroupsMath allows you to construct groups and study their properties directly in Python, to use it write:

```python
from groupsmath import *
```

From there, you can construct groups, perform operations on their elements, investigate subgroups, automorphisms, products, and other structures.

---

## Documentation

### Basic group methods

- [Groups](Groups.md)
- [Group families and precooked groups](Group_families_and_precooked_groups.md)
- [Group operations and properties](Group_operations_and_properties.md)
- [Elements](Elements.md)
- [Cayley table visualization](Cayley_table_visualization.md)
- [Cayley graphs](Cayley_graphs.md)

### Advanced group methods

- [Subgroups](Subgroups.md)
- [Automorphisms](Automorphisms.md)
- [Products](Products.md)
- [Conjugation and commutators](Conjugation_and_commutators.md)
- [Hasse diagrams (*experimental feature*)](Hasse_diagrams.md)

### Matrix groups

- [Matrix groups](Matrix_groups.md)
- [Finite fields](Finite_fields.md)

### Presented groups
- [Presentations (*experimental feature*)](Presentations.md)

### Structure
- [Structure description (*experimental feature*)](Structure.md)

### Shortcuts
- [Shortcuts](Shortcuts.md)

---

## Project

GroupsMath is an open-source project developed in Python.

The source code is available on [GitHub](https://github.com/MarioSultan/GroupsMath).

---

## License

See the [license](https://github.com/MarioSultan/GroupsMath/blob/main/LICENSE) file for information about the license.
