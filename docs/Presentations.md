# Group presentations

![Experimental feature](https://raw.githubusercontent.com/MarioSultan/GroupsMath/main/expf.png)

The `groupsmath.presentations` module provides a way to represent finitely presented groups using generators and relations.

A presented group is written in the form

$$
\langle x_1,x_2,\ldots \mid r_1,r_2,\ldots\rangle,
$$

where the generators describe the symbols used to build group elements and the relations specify which words are identified with the identity.

The implementation represents elements as `Word` objects and reduces words using free cancellation and rewriting rules derived from the relations.

---

## `Word`

The basic object used by the presentation machinery is:

```python
Word(word)
```

A `Word` is a sequence of generator symbols.

The empty word represents the identity:

```python
Word("")
```

and can also be written:

```python
Word("e")
```

Both are displayed as:

```text
e
```

### Alphabet

Words use Latin letters to distinguish generators from their inverses:

- lowercase letter = generator
- uppercase letter = inverse generator

For example:

```text
a
A
```

represent `a` and `a⁻¹`.

The `Word` class accepts Latin letters except `e`/`E`, because `e` is reserved for the identity.

---

## Multiplication of words

Words can be concatenated using `*`:

```python
Word("ab") * Word("c")
```

gives:

```text
abc
```

The operation is concatenation; it does not by itself apply the presentation relations.

Strings can also be used directly:

```python
Word("ab") * "c"
```

---

## Powers

Words support integer powers:

```python
Word("a") ** 3
```

gives:

```text
aaa
```

The zeroth power is the identity:

```python
Word("a") ** 0
```

gives:

```text
e
```

Negative powers use the inverse:

```python
Word("a") ** -1
```

gives:

```text
A
```

---

## Inverses

The inverse of a word is obtained by:

1. reversing the word;
2. replacing every generator by its inverse.

For example:

```text
abC
```

has inverse:

```text
cBA
```

The inverse can be obtained with:

```python
word.inverse()
```

or:

```python
~word
```

The identity is its own inverse.

---

# `PresentedGroup`

A presented group is created with:

```python
PresentedGroup(generators, relations)
```

For example:

```python
G = PresentedGroup(
    ["a", "b"],
    ["a3", "b2", "abAB"]
)
```

corresponds to the presentation:

$$
\langle a,b\mid a^3,b^2,aba^{-1}b^{-1}\rangle.
$$

The relations are interpreted as words equal to the identity.

---

## Generators

Generators must be:

- single lowercase Latin letters;
- distinct.

For example:

```python
["a", "b", "c"]
```

is valid.

But:

```python
["a", "A"]
```

is not valid, because generators must be lowercase.

Likewise, generators cannot contain multiple characters.

The class automatically constructs the inverse map:

```text
a ↔ A
b ↔ B
c ↔ C
```

---

## Relations

Relations can be supplied as strings or `Word` objects:

```python
PresentedGroup(
    ["a", "b"],
    ["aaa", "bb", "abAB"]
)
```

Each relation is interpreted as:

$$
r=e.
$$

Before being stored, the relation is freely reduced.

Thus redundant free cancellations are removed immediately.

---

# Free reduction

The method:

```python
_free_reduce(word)
```

performs the standard free-group cancellations:

$$
xx^{-1}\rightarrow e
$$

and

$$
x^{-1}x\rightarrow e.
$$

For example:

```text
aAbB
```

reduces to:

```text
e
```

and:

```text
abBa
```

reduces to:

```text
aa
```

The implementation performs this efficiently with a stack.

Importantly, free reduction uses only inverse pairs. It does not use the defining relations of the presented group.

---

# Reduction using relations

After free reduction, the presentation can apply its defining relations.

The main method is:

```python
_reduce(word)
```

It performs:

1. free reduction;
2. relation rewriting;
3. free reduction again;
4. repetition until no further reduction is possible.

The goal is to replace a word with a shorter equivalent word.

---

## Relation rewriting rules

For every relation

$$
x_1x_2\cdots x_n=e,
$$

the implementation creates rewriting rules.

The original relator is converted to the identity:

```text
x1x2...xn -> e
```

and its inverse is also converted to the identity.

The implementation additionally derives rules by isolating each generator.

If:

$$
LxR=e,
$$

then:

$$
x^{-1}=RL.
$$

This gives a rewriting rule for the inverse of `x`.

The implementation also derives the corresponding rule for `x` itself.

---

## Example: `aaa = e`

Consider the relation:

```text
aaa
```

which means:

$$
a^3=e.
$$

The presentation can derive:

$$
a^{-1}=a^2.
$$

In the module's notation:

```text
A -> aa
```

It can also derive the reverse form:

```text
aa -> A
```

when that produces a shorter word.

Thus a word containing `aa` may be reduced to `A`.

---

## Only shortening rules are applied

`_relation_reduce_once()` searches for a rewriting rule and applies it only when the resulting word is shorter than the original.

This is an important part of the current implementation.

Therefore, a mathematically valid relation is not necessarily used in both directions if one direction would increase the word length.

This gives the reduction procedure a practical stopping condition.

---

# Group operation

The group operation of a `PresentedGroup` is:

```python
G.operation(elem1, elem2)
```

The two elements are converted into `Word` objects, concatenated, and reduced.

Conceptually:

$$
[u]\cdot[v]=[uv].
$$

For example:

```python
G.operation("ab", "BA")
```

first forms:

```text
abBA
```

and then reduces it according to free cancellation and the presentation relations.

The result is returned as a `Word`.

---

## Identity

The identity element is:

```python
G.identity()
```

and is represented by:

```text
e
```

Internally this is an empty word.

---

## Inverse

The inverse of a presented-group element is calculated by reversing and inverting the word and then reducing it:

```python
G.inverse("ab")
```

The result represents:

$$
(ab)^{-1}=b^{-1}a^{-1}.
$$

---

# Membership

`PresentedGroup` accepts a word if it uses only the group's generators and their inverses.

For example, if the generators are:

```text
a, b
```

then these are valid:

```text
a
A
ab
aBbA
```

but a word containing an unrelated generator is rejected.

The membership test checks that the word can be converted and validated against the presentation's alphabet.

> Membership here means that the expression is a valid word in the presentation's generators. It is not a test for whether two arbitrary words represent different group elements.

---

# Converting a presentation to a `CayleyGroup`

The most important transformation provided by the module is:

```python
G.toCayleyGroup()
```

This attempts to enumerate the presented group and construct its Cayley table.

The enumeration is performed with **breadth-first search (BFS)**.

---

## BFS enumeration

The search starts with the identity:

```text
e
```

and explores the group by multiplying known elements by every generator and every generator inverse.

If the generators are:

```text
a, b
```

the search uses:

```text
a, b, A, B
```

as its generating set for the exploration.

Every newly discovered reduced word is added to the queue.

This continues until no new elements are found.

Therefore, if the presented group is finite, BFS can eventually discover all its elements, assuming the maximum-element limit is not reached.

---

## `max_elements`

The conversion accepts:

```python
G.toCayleyGroup(max_elements=1000)
```

The default limit is:

```text
1000
```

If the search discovers that the group contains at least that many elements before the enumeration finishes, an `OverflowError` is raised.

This prevents an infinite or very large presented group from causing an unbounded enumeration.

For a larger finite group, the limit can be increased:

```python
G.toCayleyGroup(max_elements=10000)
```

---

## Cayley table construction

After BFS has discovered all elements, the module creates an indexed list:

```text
0, 1, 2, ...
```

for the discovered words.

It then computes every product:

$$
g_i g_j
$$

and stores the index of the resulting word in the Cayley table.

The resulting object is a normal `CayleyGroup`.

The names of its elements are the corresponding reduced words.

---

# Caching

The first call to:

```python
G.toCayleyGroup()
```

performs the enumeration.

The resulting `CayleyGroup` is stored in:

```python
G._cayley_cache
```

Subsequent calls return the cached object instead of enumerating the presentation again.

This is especially useful because constructing the complete Cayley table can be expensive.

---

# `toExplicitGroup()`

A presented group can also be converted directly to an `ExplicitGroup`:

```python
G.toExplicitGroup()
```

Internally, this first constructs the corresponding `CayleyGroup` and then converts it to an `ExplicitGroup`.

Therefore the same enumeration limitations apply.

---

# `order()`

The order of a `PresentedGroup` is obtained through its Cayley representation:

```python
G.order()
```

Conceptually:

1. enumerate the group;
2. construct the Cayley group;
3. count its elements.

For a finite presented group this gives its order.

For an infinite group, however, the enumeration will not terminate naturally; the `max_elements` limit is therefore important.

---

# Presentation notation

The string representation of a presented group is:

```text
〈 generators | relations 〉
```

For example:

```python
G = PresentedGroup(
    ["a", "b"],
    ["aaa", "bb", "abAB"]
)

print(G)
```

produces a presentation in the style:

```text
〈 a, b | aaa, bb, abAB 〉
```

This is the standard mathematical notation:

$$
\langle a,b\mid a^3,b^2,aba^{-1}b^{-1}\rangle.
$$

The Python representation uses uppercase letters for inverses rather than writing exponent `-1`.

---

# Complete example

```python
from groupsmath.presentations import Word, PresentedGroup

# The cyclic group C3
C3 = PresentedGroup(
    ["a"],
    ["aaa"]
)

print(C3)
print(C3.operation("a", "aa"))
print(C3.inverse("a"))
print(C3.order())

# A group with two generators
G = PresentedGroup(
    ["a", "b"],
    [
        "aaa",     # a^3 = e
        "bb",      # b^2 = e
        "abAB"     # aba^{-1}b^{-1} = e
    ]
)

print(G)

C = G.toCayleyGroup(max_elements=100)

print("Order:", C.order())
print("Elements:", C.elements())
```

---

# Important implementation limitations

The presentation machinery is currently under development, and its reduction system should not be interpreted as a complete general-purpose implementation of the word problem for finitely presented groups.

In particular:

### Rewriting is heuristic

The module generates shortening rules from the relations and repeatedly applies them. A reduced word is therefore a word that the current rewriting system can no longer shorten.

It is not necessarily a mathematically unique normal form for every possible presentation.

### Finite enumeration is bounded

`toCayleyGroup()` stops with an error once the number of discovered elements reaches `max_elements`.

### Infinite groups cannot be completely enumerated

A presentation may define an infinite group. In that case, complete Cayley-table construction is impossible.

### Enumeration can be expensive

The BFS explores words generated by all generators and their inverses. Even finite groups can become expensive to enumerate as their order grows.

---

## Summary

The `groupsmath.presentations` module provides:

- `Word` objects for group words;
- lowercase generators and uppercase inverses;
- word multiplication and powers;
- word inversion;
- free reduction;
- rewriting from defining relations;
- `PresentedGroup` objects;
- group multiplication and inverses;
- BFS enumeration;
- conversion to `CayleyGroup`;
- conversion to `ExplicitGroup`;
- order calculation for enumerable finite groups;
- a mathematical presentation representation.

The central workflow is:

```text
Presentation
    │
    ▼
Generators + Relations
    │
    ▼
Word
    │
    ├── free reduction
    │
    └── relation reduction
            │
            ▼
       reduced words
            │
            ▼
          BFS
            │
            ▼
       CayleyGroup
            │
            ├── ExplicitGroup
            └── group operations
```

The module therefore acts as a bridge between the compact mathematical description

$$
\langle X\mid R\rangle
$$

and the explicit finite-group machinery already present elsewhere in `GroupsMath`.
