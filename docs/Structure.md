# Group structure

![Experimental feature](https://raw.githubusercontent.com/MarioSultan/GroupsMath/main/expf.png)

The `groupsmath.structure` module provides tools for describing the algebraic structure of a finite group.

Unlike a simple lookup table of known groups, the main function tries to determine the structure from properties of the group itself: its order, whether it is abelian or simple, its normal subgroups, complements, and quotient groups.


## `structure_description(G)`

The main function is:

```python
from groupsmath.structure import structure_description

structure_description(G)
```

It returns a string describing the structure of `G`, using notation such as:

- `C6` — cyclic group of order 6
- `C2 x C2` — direct product of cyclic groups
- `N : H` — semidirect-product notation used by the module
- `N.H` — notation used for a non-split extension
- `S3`, `A5`, etc. — when the implementation recognizes a simple group

The function follows a sequence of cases.

---

## 1. The trivial group

If the group has order 1, the result is simply:

```python
"I"
```

This is checked before any other structural analysis.

---

## 2. Abelian groups

If `G` is abelian, `structure_description()` calls the internal function `_decompose_abelian(G)`.

```python
if G.is_abelian():
    return _decompose_abelian(G)
```

The intended result is a decomposition into cyclic factors:

```text
C_d1 x C_d2 x ...
```

### Cyclic abelian groups

First, the module checks whether the group contains an element whose order is equal to the order of the group.

If so, the group is cyclic and the result is:

```text
C_n
```

For example, an abelian group of order 6 containing an element of order 6 is described as:

```text
C6
```

### Non-cyclic abelian groups

For groups that are not cyclic, the current implementation attempts to obtain cyclic factors by repeatedly looking at the maximum element order.

The code currently contains an intentional `break` after the first reduction step, so the decomposition is only approximate for more complicated abelian groups.

There is also a fallback of the form:

```text
C_max x C_(n // max)
```

This means that the current implementation should be regarded as a work in progress for complete abelian decompositions.

---

## 3. Simple groups

If the group is not abelian, the module next checks:

```python
G.is_simple()
```

A simple group is a group whose only normal subgroups are the trivial subgroup and the group itself. `GroupsMath` determines this from `G.normal_subgroups()`.

For a simple group, `structure_description()` calls:

```python
_describe_simple(G)
```

### Recognized simple groups

The current implementation recognizes the following non-abelian simple groups by their order:

| Order | Description |
|---:|---|
| 60 | `A5` |
| 168 | `PSL(2,7)` |
| 360 | `A6` |

If the order does not match one of these cases, the result is:

```text
SimpleGroup(n)
```

For example:

```text
SimpleGroup(504)
```

The module does not attempt a complete classification of finite simple groups.

---

## 4. Decomposition using normal subgroups

If the group is neither trivial, abelian, nor simple, the module searches for proper non-trivial normal subgroups.

```python
normals = G.normal_subgroups()
proper_normals = [H for H in normals if 1 < H.order() < n]
```

These normal subgroups are sorted from largest to smallest.

For each one, the module tries to find a complement.

### Complements

A subgroup `H` is considered a complement of a normal subgroup `N` when:

- its order satisfies

```text
|N| · |H| = |G|
```

- and their intersection contains only the identity:

```text
N ∩ H = {e}
```

The internal function responsible for this search is:

```python
_find_complement(G, N)
```

It searches through the subgroups of `G` and returns the first subgroup satisfying these conditions.

---

## 5. Direct products

If a complement exists and the complement is also normal, the module describes the group as a direct product:

```text
N x H
```

The two components are themselves passed recursively through `structure_description()`.

For example, the intended style is:

```text
C2 x C2
```

The relevant test is:

```python
if complement.is_normal():
    return f"{name_N} x {name_H}"
```

Thus the structure is recursively described rather than simply reporting the names of the particular subgroups.

---

## 6. Semidirect products

If a complement exists but it is not normal, the module uses semidirect-product notation:

```text
N : H
```

The relevant part of the implementation is:

```python
else:
    return f"{name_N} : {name_H}"
```

For example, a group may be represented in the style:

```text
C3 : C4
```

The colon here is the notation chosen by `GroupMaker`/`GroupsMath` for a semidirect decomposition.

---

## 7. Non-split extensions

If no suitable complement is found, the module falls back to an extension description.

It chooses the largest proper non-trivial normal subgroup `N` and constructs the quotient:

```python
Q = G.quotient(N)
```

The result is then:

```text
structure(N).structure(Q)
```

with a dot between the two descriptions:

```text
N.Q
```

For example, the general form is:

```text
C4.C2
```

This represents the implementation's description of an extension where the selected normal subgroup does not have a complement.

---

# Internal functions

The module contains three helper functions used by `structure_description()`.

## `_decompose_abelian(G)`

```python
_decompose_abelian(G)
```

Attempts to express an abelian group as a product of cyclic groups.

The function:

1. Gets the order of the group.
2. Gets the orders of all elements.
3. Checks whether the maximum element order equals the group order.
4. If so, returns `C_n`.
5. Otherwise, attempts to construct cyclic factors.

The current implementation is explicitly approximate for non-cyclic abelian groups.

---

## `_find_complement(G, N)`

```python
_find_complement(G, N)
```

Searches all subgroups of `G` for a subgroup `H` such that:

```text
|N| · |H| = |G|
```

and

```text
N ∩ H = {e}.
```

It returns the first matching subgroup, or:

```python
None
```

if no complement is found.

The search relies on the subgroup functionality implemented by the core module.

---

## `_describe_simple(G)`

```python
_describe_simple(G)
```

Provides the simple-group names recognized by the current implementation.

For an abelian simple group, it returns:

```text
C_n
```

For non-abelian simple groups, it currently recognizes:

```text
60  -> A5
168 -> PSL(2,7)
360 -> A6
```

Otherwise:

```text
SimpleGroup(n)
```

---

# How the analysis works

In simplified form, `structure_description(G)` follows this decision tree:

```text
                    G
                    │
          ┌─────────┴─────────┐
          │                   │
       |G| = 1?             No
          │                   │
         "I"                  ▼
                    Is G abelian?
                          │
                    ┌─────┴─────┐
                   Yes          No
                    │            │
          Abelian decomposition  ▼
                         Is G simple?
                              │
                       ┌──────┴──────┐
                      Yes            No
                       │              │
                Simple description   ▼
                              Find normal N
                                    │
                              Find complement H
                                    │
                         ┌──────────┴──────────┐
                       Found                 Not found
                         │                       │
                  Is H normal?                 N / G/N
                   │        │                    │
                  Yes       No                   ▼
                   │         │              N.Q
                 N x H      N : H
```

This is therefore not a database lookup of group names. The module tries to build a description recursively from structural properties detected in the group.

## Relationship with `core.py`

`structure.py` depends on the group operations provided by `core.py`. In particular, the structure algorithm uses methods such as:

```python
G.order()
G.element_orders()
G.is_abelian()
G.is_simple()
G.normal_subgroups()
G.subgroups()
G.quotient(N)
```

These methods are implemented for the group's core classes and are therefore part of the machinery that makes structural decomposition possible.

For example, `is_simple()` is implemented by checking that the group has exactly two normal subgroups, while `normal_subgroups()` is obtained by filtering the group's subgroups according to normality.

---

## Current limitations

The module is currently marked as being under development.

The most important limitation visible in the current implementation is the abelian decomposition: `_decompose_abelian()` stops after the first reduction step, so it does not yet implement a complete general decomposition into invariant factors or elementary divisors.

The simple-group identification is also intentionally limited to a few orders rather than implementing the full classification of finite simple groups.

Finally, the complement search is a direct search through the available subgroups, so its cost depends on the number of subgroups that must be examined.

These limitations are part of the current implementation rather than assumptions added by the documentation.
