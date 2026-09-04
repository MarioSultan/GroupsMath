# Hasse diagrams

![Experimental feature](https://raw.githubusercontent.com/MarioSultan/GroupsMath/main/expf.png)

A Hasse diagram is a graphical representation of a partially ordered set (poset). In GroupMaker, `hasse_diagram()` is used to visualize the **subgroup lattice** of a finite group. Each node represents a subgroup, and the vertical structure represents subgroup inclusion.

![S3 hasse diagram](https://raw.githubusercontent.com/MarioSultan/GroupsMath/main/imgs/hasse_S3.png)

For a group $G$, the subgroup lattice is

$$
\mathcal L(G)=\{H\mid H\leq G\},
$$

ordered by inclusion.

---

## Creating a Hasse diagram

For a finite group `G`, simply use:

```python
G.hasse_diagram()
```

For example:

```python
from groupsmath.precooked import C4

C4.hasse_diagram()
```

The resulting diagram contains one node for every subgroup of $C_4$.

Nodes are labelled using GroupMaker's structural descriptions of the corresponding subgroups.


---

# Drawing style

The current implementation draws:

- square nodes;
- white node interiors;
- black borders;
- black edges;
- subgroup labels;
- no visible arrows;
- node size `1000`.

The relevant drawing operation is:

```python
nx.draw(
    gr,
    pos,
    with_labels=True,
    labels=labels,
    node_shape="s",
    node_color="white",
    edgecolors="black",
    node_size=1000,
    arrows=False
)
```

These visual properties are currently fixed by the implementation.

---

# What the diagram tells you

A Hasse diagram can reveal several structural properties immediately.

## Subgroup chains

A vertical path

$$
H_0<H_1<\cdots<H_n
$$

represents a chain of nested subgroups.

---

## Maximal subgroups

A subgroup directly connected to $G$ from below is a maximal proper subgroup.

Therefore, the nodes immediately below the node representing $G$ correspond to maximal subgroups.

---

## Minimal non-trivial subgroups

Nodes immediately above the trivial subgroup correspond to minimal non-trivial subgroups.

---

## Incomparable subgroups

If neither of two subgroups contains the other,

$$
H\nleq K,
\qquad
K\nleq H,
$$

they are incomparable.

Branching in the Hasse diagram makes these relationships particularly easy to see.

---

# Examples

## Cyclic group $C_4$

```python
from groupsmath.precooked import C4

C4.hasse_diagram()
```

The subgroup chain is:

$$
\{e\}<\langle r^2\rangle<C_4.
$$

The diagram is therefore:

![C4 hasse diagram](https://raw.githubusercontent.com/MarioSultan/GroupsMath/main/imgs/hasse_C4.png)

---

## A group with several subgroups

```python
from groupsmath.precooked import S3

S3.hasse_diagram()
```

The diagram displays the trivial subgroup, the intermediate subgroups, and the whole group, while omitting non-cover inclusion relations.

![S3 hasse diagram](https://raw.githubusercontent.com/MarioSultan/GroupsMath/main/imgs/hasse_S3.png)

This makes the branching structure of the subgroup lattice visible.
