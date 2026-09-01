# Finite Fields

GroupsMath supports matrix groups over finite fields through the `F_p` field type. This document explains the finite-field-specific behaviour of `MatrixGroup`, complementing the general matrix-group documentation.

> **Important:** The current implementation supports prime finite fields $\mathbb{F}_p$, where $p$ is prime. It does **not** currently implement general extension fields such as $\mathbb{F}_{p^k}$ for $k>1$.

## What is a finite field?

A finite field is a field containing finitely many elements.

The implementation in `matrixgroups.py` uses the prime field

$$
\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z},
$$

where $p$ is a prime number.

Its elements are represented by the integer representatives

$$
0,1,\ldots,p-1.
$$

For example,

$$
\mathbb{F}_5=\{0,1,2,3,4\}.
$$

Arithmetic is performed modulo $p$.

---

## Creating a matrix group over $\mathbb{F}_p$

A finite-field matrix group can be created with:

```python
from groupsmath.matrixgroups import MatrixGroup

G = MatrixGroup(2, field="F_p", p=5)
```

This represents

$$
GL_2(\mathbb{F}_5),
$$

the group of all invertible $2\times2$ matrices whose entries belong to $\mathbb{F}_5$.

The implementation also accepts the prime directly:

```python
G = MatrixGroup(2, 5)
```

An integer `field` argument is interpreted as the value of `p`, so this is equivalent to:

```python
G = MatrixGroup(2, field="F_p", p=5)
```

---

## The prime `p`

When `field="F_p"`, the constructor requires a value of `p`.

```python
MatrixGroup(2, field="F_p")
```

raises an error because the finite field has not been specified.

The implementation also checks that `p` is prime.

For example:

```python
MatrixGroup(2, field="F_p", p=5)
```

is valid, whereas:

```python
MatrixGroup(2, field="F_p", p=6)
```

raises a `ValueError`.

The primality test is performed internally by `_is_prime()`.

---

## Valid matrix entries

For a matrix group over $\mathbb{F}_p$, entries must be integer representatives in:

$$
\{0,1,\ldots,p-1\}.
$$

For example, for $\mathbb{F}_5$:

```python
A = np.array([
    [1, 2],
    [3, 4]
])
```

is a valid matrix over the field.

However:

```python
A = np.array([
    [1, 5],
    [3, 4]
])
```

is not accepted as a matrix over $\mathbb{F}_5$, because `5` is not one of the chosen representatives.

The implementation checks that entries are:

- integers,
- non-negative,
- smaller than `p`.

Thus the implementation does **not** automatically interpret an arbitrary integer such as `7` as the representative `2` when checking membership.

---

## Matrix multiplication modulo `p`

The group operation is ordinary matrix multiplication followed by reduction modulo $p$.

```python
G.operation(A, B)
```

computes:

$$
AB \pmod p.
$$

Internally this is:

```python
(A @ B) % p
```

For example, over $\mathbb{F}_5$,

$$
\begin{pmatrix}
1&2\\
3&4
\end{pmatrix}
\begin{pmatrix}
2&1\\
1&3
\end{pmatrix}
=
\begin{pmatrix}
4&2\\
0&0
\end{pmatrix}
\pmod 5.
$$

The reduction modulo $p$ is therefore part of every matrix multiplication in a finite-field matrix group.

---

## The identity matrix

The identity is the usual identity matrix:

$$
I_n=
\begin{pmatrix}
1&0&\cdots&0\\
0&1&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&1
\end{pmatrix}.
$$

For a finite-field group, `identity()` returns an integer NumPy matrix.

```python
G.identity()
```

For example, for a $2\times2$ group:

```text
[[1 0]
 [0 1]]
```

---

## Determinants modulo `p`

Membership in a matrix group requires the matrix to be invertible.

For finite fields, the determinant is reduced modulo $p$:

$$
\det(A)\pmod p.
$$

The implementation uses:

```python
G._determinant(A)
```

which computes the numerical determinant and then reduces it modulo `p`.

A matrix is considered invertible when:

$$
\det(A)\not\equiv0\pmod p.
$$

Therefore:

```python
A in G
```

requires the determinant to be non-zero in $\mathbb{F}_p$.

---

## Inverses

For finite fields, the inverse is computed modulo $p$.

Mathematically:

$$
A^{-1}
=
(\det A)^{-1}\operatorname{adj}(A)
\pmod p.
$$

The implementation first computes the determinant modulo $p$, obtains its modular inverse, and then applies the adjugate formula.

```python
G.inverse(A)
```

returns the inverse matrix with entries represented in:

$$
\{0,\ldots,p-1\}.
$$

The modular inverse of a non-zero field element is obtained using Python's modular exponentiation machinery:

```python
pow(det, -1, p)
```

---

## Membership in a finite-field matrix group

For:

```python
A in G
```

the implementation checks several conditions.

### 1. Correct dimensions

The matrix must have shape:

$$
n\times n.
$$

### 2. Valid field representatives

For $\mathbb{F}_p$, every entry must be an integer in:

$$
0\leq a<p.
$$

### 3. Invertibility

The determinant must be non-zero modulo $p$.

### 4. Additional condition

If the matrix group was created with a custom `condition`, that condition must also return `True`.

Thus a finite-field matrix group can impose additional algebraic restrictions beyond invertibility.

---

## `GL(n, p)`

The constructor:

```python
from groupsmath.matrixgroups import GL

G = GL(2, 5)
```

creates:

$$
GL_2(\mathbb{F}_5).
$$

In general:

$$
GL_n(\mathbb{F}_p)
=
\{A\in M_n(\mathbb{F}_p)\mid\det(A)\neq0\}.
$$

Every matrix has entries in $\mathbb{F}_p$ and is invertible.

The order of the general linear group is:

$$
|GL_n(\mathbb{F}_p)|
=
(p^n-1)(p^n-p)(p^n-p^2)\cdots(p^n-p^{n-1}).
$$

For example:

$$
|GL_2(\mathbb{F}_2)|
=
(4-1)(4-2)
=
6.
$$

This agrees with the finite enumeration performed by `GroupsMath`.

---

## `SL(n, p)`

The special linear group can be created with:

```python
from groupsmath.matrixgroups import SL

G = SL(2, 5)
```

It consists of the invertible matrices satisfying:

$$
\det(A)=1
\pmod p.
$$

The implementation uses a membership condition that checks the determinant modulo `p`.

For example:

```python
G = SL(2, 5)
```

represents:

$$
SL_2(\mathbb{F}_5)
=
\{A\in GL_2(\mathbb{F}_5)\mid\det(A)=1\}.
$$

---

## Finite groups and enumeration

A `MatrixGroup` is considered finite exactly when:

```python
field == "F_p"
```

This is implemented by `_is_finite()`.

Consequently:

```python
G.is_finite()
```

is true for finite-field matrix groups and false for groups over `"Z"`, `"R"` or `"C"`.

The elements can then be enumerated with:

```python
G.elements()
```

---

## How enumeration works

The current implementation uses a direct exhaustive search.

For an $n\times n$ matrix over $\mathbb{F}_p$, there are:

$$
p^{n^2}
$$

possible matrices before imposing the group conditions.

The implementation generates every possible tuple of `n*n` entries:

```python
product(range(self.p), repeat=self.n * self.n)
```

reshapes each tuple into an $n\times n$ matrix, and checks:

```python
if M in self:
```

Only matrices satisfying the membership conditions are yielded.

Therefore enumeration becomes expensive very quickly as either $n$ or $p$ increases.

---

## Number of candidate matrices

Before filtering, the search space contains:

$$
p^{n^2}
$$

matrices.

For example:

| Group dimension | Field | Candidate matrices |
|---:|---:|---:|
| 2 | $\mathbb{F}_2$ | $2^4=16$ |
| 2 | $\mathbb{F}_3$ | $3^4=81$ |
| 2 | $\mathbb{F}_5$ | $5^4=625$ |
| 3 | $\mathbb{F}_2$ | $2^9=512$ |
| 3 | $\mathbb{F}_5$ | $5^9=1,953,125$ |
| 4 | $\mathbb{F}_5$ | $5^{16}=152,587,890,625$ |

This is why the current implementation is mainly practical for relatively small finite matrix groups.

---

## `order()`

For a finite matrix group:

```python
G.order()
```

enumerates the elements and counts them.

Conceptually:

$$
|G|=\#\{A\in M_n(\mathbb{F}_p):A\in G\}.
$$

For example:

```python
G = GL(2, 2)
G.order()
```

returns:

```text
6
```

For infinite matrix groups, `order()` returns:

```python
float("inf")
```

---

## Converting a finite-field matrix group to a `CayleyGroup`

A finite matrix group can be converted into a `CayleyGroup`:

```python
C = G.toCayleyGroup()
```

The conversion first enumerates all matrices and then constructs the complete Cayley table from matrix multiplication.

This allows the finite matrix group to use functionality provided by `CayleyGroup`, such as subgroup calculations and other finite-group operations.

For example:

```python
G = GL(2, 2)
C = G.toCayleyGroup()

C.subgroups()
C.is_abelian()
C.automorphisms()
```

This conversion is only possible for finite groups.

---

## Converting to an `ExplicitGroup`

A finite-field matrix group can also be converted with:

```python
E = G.toExplicitGroup()
```

The resulting `ExplicitGroup` stores the matrices explicitly and uses the matrix operation supplied by the original group.

Again, infinite matrix groups cannot be converted this way.

---

## Finite-field matrix subgroups

`MatrixSubgroup` can be used with finite-field matrix groups.

```python
MatrixSubgroup(subgroup, group)
```

The subgroup and parent group must have exactly the same:

- matrix dimension,
- field,
- value of `p`.

For example, a subgroup over $\mathbb{F}_5$ cannot be attached to a parent matrix group over $\mathbb{F}_7$.

The constructor checks:

```python
subgroup.n == group.n
subgroup.field == group.field
subgroup.p == group.p
```

---

## Supported finite fields

The current implementation should be understood as supporting:

$$
\boxed{\mathbb{F}_p\text{ for prime }p}
$$

rather than arbitrary finite fields.

For example, these are supported:

```python
GL(2, 2)
GL(2, 3)
GL(3, 5)
SL(2, 7)
```

But a general field such as:

$$
\mathbb{F}_4,\quad\mathbb{F}_8,\quad\mathbb{F}_9
$$

is **not** represented by the current implementation.

In particular, `p` must be prime. The code does not construct extension fields using irreducible polynomials or represent field elements as polynomials over $\mathbb{F}_p$.

---

## Limitations of the current implementation

There are several important implementation details to keep in mind.

### Prime fields only

Only $\mathbb{F}_p$ is implemented. Finite fields of non-prime order are not currently supported.

### Exhaustive enumeration

`elements()` tests every one of the $p^{n^2}$ possible matrices. This can become prohibitively expensive.

### Numerical determinant calculation

The implementation obtains the determinant using NumPy and then reduces it modulo $p$. It is therefore not a symbolic finite-field linear-algebra implementation.

### Integer representatives

Finite-field entries are expected to already be represented by integers in the range:

```text
0, ..., p-1
```

An integer outside that range is not automatically normalized during membership checking.

---

## Complete example

```python
import numpy as np
from groupsmath.matrixgroups import GL, SL

# General linear group over F_2
G = GL(2, 2)

print("Finite:", G.is_finite())
print("Order:", G.order())

for A in G.elements():
    print(A)

# A finite-field matrix
A = np.array([
    [1, 1],
    [0, 1]
])

print("A in G:", A in G)
print("Inverse:")
print(G.inverse(A))

# Special linear group over F_5
H = SL(2, 5)

print("Order of SL(2,5):", H.order())

# Convert to a Cayley group
C = G.toCayleyGroup()

print("Cayley order:", C.order())
print("Abelian:", C.is_abelian())
```

## Summary

Finite-field support in `GroupsMath` is based on prime fields $\mathbb{F}_p$.

For a `MatrixGroup` over $\mathbb{F}_p`:

- entries are represented by integers from `0` to `p-1`,
- multiplication is performed modulo `p`,
- determinants are evaluated modulo `p`,
- inverses are computed modulo `p`,
- the group is finite,
- elements can be enumerated,
- the group can be converted to `CayleyGroup` or `ExplicitGroup`.

The implementation is therefore suitable for experimenting with small matrix groups over prime finite fields, while general extension fields $\mathbb{F}_{p^k}$ are outside the current scope.
