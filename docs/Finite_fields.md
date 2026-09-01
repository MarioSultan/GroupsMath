# Finite Fields in Matrix Groups

In **GroupsMath**, finite field operations are integrated directly into matrix-based groups via the `MatrixGroup` class using the specification `field="F_p"`.

To work with finite field matrix groups, import the matrix groups module:

```python
from groupsmath.matrixgroups import *
```

---

## Finite field specification

A matrix group over a finite field $\mathbb{F}_p$ is constructed by specifying the parameter `field="F_p"` (or simply passing an integer $p$) along with the prime modulus $p$:

```python
G = MatrixGroup(n, field="F_p", p=p)

```

For convenience, passing an integer $p$ directly as the second argument is automatically recognized:

```python
G = MatrixGroup(n, p)

```

The parameter $p$ must be a prime integer. If $p$ is not prime or is omitted when using `"F_p"`, a `ValueError` is raised.

For example, to instantiate $GL_2(\mathbb{F}_3)$:

```python
from groupsmath.matrixgroups import MatrixGroup

G = MatrixGroup(2, field="F_p", p=3)
# Equivalent shortcut:
G = MatrixGroup(2, 3)

```

---

## Valid elements and field verification

An $n \times n$ matrix $M$ belongs to a finite field matrix group over $\mathbb{F}_p$ if and only if:

1. Its shape is strictly $n \times n$.
2. All entries are integers in the canonical range $\{0, 1, \dots, p-1\}$.
3. Its determinant modulo $p$ is non-zero ($\det(M) \pmod p \neq 0$).
4. Any custom `condition` provided to the `MatrixGroup` constructor evaluates to `True`.

For example, checking membership using the `in` operator:

```python
import numpy as np
from groupsmath.matrixgroups import GL

G = GL(2, p=3)

A = np.array([[1, 2],
              [0, 1]])

A in G
# True

```

An entry outside the set $\{0, 1, \dots, p-1\}$ or a non-integer entry will return `False`:

```python
B = np.array([[1, 5],   # 5 is not in {0, 1, 2}
              [0, 1]])

B in G
# False

```

---

## Arithmetic operations in $\mathbb{F}_p$

Matrix multiplication and inversion over $\mathbb{F}_p$ are performed using modular arithmetic modulo $p$.

### Group Operation (Multiplication)

The product of two matrices $A, B \in M_n(\mathbb{F}_p)$ is computed via `G.operation(A, B)`:

$$(A \cdot B) \pmod p$$

```python
A = np.array([[1, 2], [0, 1]])
B = np.array([[2, 1], [1, 1]])

G.operation(A, B)
# array([[0, 0],
#        [1, 1]])  # Results are reduced modulo p

```

### Identity Element

The identity element is the standard $n \times n$ identity matrix $I_n$ with integer entries:

```python
G.identity()

```

### Inversion

The inverse of a matrix $A$ over $\mathbb{F}_p$ is computed modulo $p$ via modular determinant inversion and the adjugate matrix:

$$A^{-1} = (\det A)^{-1} \text{adj}(A) \pmod p$$

In GroupsMath, this is accessed via:

```python
G.inverse(A)

```

---

## Standard matrix groups over $\mathbb{F}_p$

Several helper functions allow immediate construction of standard matrix groups over finite fields by passing the prime $p$ as an integer argument or keyword argument.

### General Linear Group: `GL(n, p)`

Constructs $GL_n(\mathbb{F}_p) = \{A \in M_n(\mathbb{F}_p) \mid \det(A) \pmod p \neq 0\}$:

```python
from groupsmath.matrixgroups import GL

G = GL(2, p=5)
# or GL(2, 5)

```

### Special Linear Group: `SL(n, p)`

Constructs $SL_n(\mathbb{F}_p) = \{A \in GL_n(\mathbb{F}_p) \mid \det(A) \equiv 1 \pmod p\}$:

```python
from groupsmath.matrixgroups import SL

G = SL(2, p=3)

```

### Symplectic Group: `Sp(n, p)`

For an even dimension $n = 2k$, constructs $Sp_n(\mathbb{F}_p) = \{A \in M_n(\mathbb{F}_p) \mid A^T J A \equiv J \pmod p\}$, where $J = \begin{pmatrix} 0 & I_k \\ -I_k & 0 \end{pmatrix}$:

```python
from groupsmath.matrixgroups import Sp

G = Sp(4, p=3)

```

---

## Finiteness, Enumeration, and Conversions

Since $\mathbb{F}_p$ is a finite set, any `MatrixGroup` defined over `"F_p"` is finite.

### Group Order

The exact order $\vert{}G\vert{}$ is computed by enumerating all valid matrices over $\mathbb{F}_p$:

```python
G = GL(2, 2)
G.order()   # 6

```

### Element Generator

Elements can be iterated over using the generator method `G.elements()`:

```python
for A in G.elements():
    print(A)

```

Matrices are yielded as nested tuples of integers:

```text
((1, 0), (0, 1))
((1, 0), (1, 1))
...

```

### Conversion to `CayleyGroup` and `ExplicitGroup`

Finite field matrix groups can be seamlessly converted into `CayleyGroup` or `ExplicitGroup` instances to access abstract group-theoretic operations (such as subgroup structures, centralizers, derived series, and automorphism groups):

```python
C = G.toCayleyGroup()
E = G.toExplicitGroup()

C.is_abelian()          # False
C.order_distribution()  # {1: 1, 2: 3, 3: 2}

```

---

## Complete Example

```python
import numpy as np
from groupsmath.matrixgroups import SL

# Construct SL(2, F_3)
G = SL(2, 3)

print("Order of SL(2, F_3):", G.order())

# Fetch elements and perform operations
elems = list(G.elements())
A = np.array(elems[1])

print("Matrix A:")
print(A)

print("Inverse of A in F_3:")
print(G.inverse(A))

# Convert to CayleyGroup to analyze group properties
C = G.toCayleyGroup()
print("Is SL(2, F_3) simple?", C.is_simple())
print("Center indices:", C.center())
````
