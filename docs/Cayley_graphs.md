# Cayley graphs

A Cayley graph is a graphical representation of a group together with a chosen generating set.

![S3 graph](https://raw.githubusercontent.com/MarioSultan/GroupsMath/main/imgs/graph_S3.png)

For a group $G$ and a generating set $S=\{s_1,\ldots,s_k\}$, the Cayley graph has one vertex for every element of $G$ and a directed edge

$$
g\longrightarrow gs
$$

for every $g\in G$ and $s\in S$.

GroupMaker provides `cayley_graph()` for constructing and displaying these graphs. The implementation uses NetworkX for the graph and Matplotlib for the final visualization.

---

## Creating a Cayley graph

A Cayley graph is displayed with:

```python
G.cayley_graph()
```

For example:

```python
from groupsmath.precooked import C4

C4.cayley_graph()
```

If no generating set is supplied, GroupMaker automatically obtains one using `G.generators()`

---

## Choosing the generators

The `generators` argument specifies the elements used to construct the graph:

```python
C4.cayley_graph(
    generators=["r"]
)
```

For several generators:

```python
G.cayley_graph(
    generators=["a", "b"]
)
```

Every element $g$ then receives edges corresponding to $g\to ga,\qquad g\to gb.$ The same group can therefore have different Cayley graphs depending on the chosen generating set.

> The supplied elements must generate the whole group. If they do not generate $G$, a `ValueError` is raised. This ensures that the resulting graph represents the whole group rather than only a proper subgroup.


---

## Mathematical mode

By default:

```python
math_mode=True
```

Node names are wrapped in `$...$` so that Matplotlib renders them as mathematical text.

For example:

```python
C4.cayley_graph(math_mode=True)
```

can display names such as:

```text
e, r, r², r³
```

To use ordinary text instead:

```python
C4.cayley_graph(math_mode=False)
```

---

## Showing node names

The `names` argument controls whether node labels are displayed:

```python
G.cayley_graph(names=True)
```

or:

```python
G.cayley_graph(names=False)
```

When `names=False`, the graph is drawn without node labels.

If `names=None`, GroupMaker chooses automatically:

- groups with at most 20 elements: names are shown;
- groups with more than 20 elements: names are hidden.

This keeps larger graphs readable.


---

## Edge labels

Each generated edge is associated internally with the generator that produced it.

For example, with generators `a` and `b`:

$$
g\xrightarrow{a}ga,
\qquad
g\xrightarrow{b}gb.
$$

The `edgenames` argument exists in the current method signature:

```python
G.cayley_graph(edgenames=...)
```

Use `True` to show the labels and `False` to disable.

---

## Coloring generators

Different generators can be distinguished by assigning different colors to their edges.

The `colormap` argument controls these colors:

```python
G.cayley_graph(
    generators=["a", "b"],
    colormap=["#ff0000", "#0000ff"]
)
```

The first color corresponds to the first generator, the second color to the second generator, and so on.

Thus, $g\xrightarrow{a}ga$ and $g\xrightarrow{b}gb$ can be visually distinguished.

The default value is `standard`, which is a predefined sequence of colors in GroupMaker.

---

## Node size

The `node_size` argument controls the node size:

```python
G.cayley_graph(node_size=1500)
```

The default value is:

```python
node_size=1000
```

When `names=False`, the current implementation uses a fixed node size of `250`.

---

## Layout

GroupMaker uses NetworkX's spring layout to determine the positions of the vertices.

```python
nx.spring_layout(gr)
```

The positions are therefore determined by the graph layout algorithm rather than by any intrinsic geometric position associated with the group elements. The important mathematical information is contained in the vertices and edges, not in their particular positions on the page.

---

## Adding a title

A title can be supplied with `title`:

```python
C4.cayley_graph(
    title="Cayley graph of C4"
)
```

---

# Understanding the construction

Suppose the group has elements

```text
e, a, b, c
```

and the generating set is

```text
a, b
```

For every element `g`, GroupMaker computes:

```python
G.operation(g, a)
G.operation(g, b)
```

and creates the corresponding edges:

```text
g -> ga
g -> gb
```

Therefore, the graph is generated directly from the group operation.

For a finite group of order $n$ and a generating set containing $k$ elements, the construction attempts to create $nk$ directed generator edges.


---

## A complete example

```python
from groupsmath.precooked import S3

S3.cayley_graph(
    generators=["(12)", "(23)"],
    title="Cayley graph of S3",
    colormap=["#24e3d3", "#f875dc"],
    names=True,
    math_mode=True,
    node_size=1200
)
```

The output is:

![S3 graph](https://raw.githubusercontent.com/MarioSultan/GroupsMath/main/imgs/graph_S3.png)

Each vertex represents an element of $S_3$.

The cyan edges correspond to multiplication by $(12)$, while the pink edges correspond to multiplication by $(23)$.

Following a path through the graph therefore corresponds to successively multiplying by the selected generators.

---

## Summary

The main interface is:

```python
G.cayley_graph(
    generators=None,
    title="",
    colormap=standard,
    names=None,
    edgenames=None,
    math_mode=True,
    node_size=1000
)
```

| Argument | Purpose |
|---|---|
| `generators` | Generating set used to construct the graph |
| `title` | Title displayed above the graph |
| `colormap` | Colors assigned to generator edges |
| `names` | Whether element names are displayed |
| `edgenames` | Reserved for edge-label customization |
| `math_mode` | Whether node names use mathematical text |
| `node_size` | Size of labelled nodes |

The resulting graph is directed, has one node for each group element, and represents right multiplication by the selected generators.

In this way, `cayley_graph()` provides a direct visual connection between the algebraic structure of a group and graph theory.
