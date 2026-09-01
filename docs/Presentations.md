# Group presentations

![Experimental feature](https://raw.githubusercontent.com/MarioSultan/GroupsMath/main/expf.png)

GroupMaker provides experimental support for groups defined by generators and relations through the `PresentedGroup` class.

A group presentation has the form

$$
G=\langle x_1,\ldots,x_n\mid r_1,\ldots,r_m\rangle,
$$

where the $x_i$ are generators and the $r_i$ are relations that are required to represent the identity element.

The presentation system works with words in generators and their inverses, reduces them freely, and then applies rewriting rules derived from the defining relations.

```python
from groupsmath.presentations import Word, PresentedGroup
```

---

## Words

Words are represented by the `Word` class.

A word is created from a string:

```python
w = Word("abBA")
```

Each lowercase letter represents a generator and its corresponding uppercase letter represents its inverse:

```text
a  -> a
A  -> a⁻¹
b  -> b
B  -> b⁻¹
```

The empty word represents the identity element. It can be created using either:

```python
Word("")
```

or:

```python
Word("e")
```

Both represent:

$$
e.
$$

The string representation of the identity is:

```python
str(Word(""))
# 'e'
```

The letter `e` is notation for the identity rather than a generator.

---

## Valid generators

Generators must be single lowercase Latin letters.

For example:

```python
Word("a")
Word("b")
Word("x")
```

are valid words.

A `PresentedGroup` therefore uses generator names such as:

```python
[a, b, c]
```

where each generator is represented by a `Word`.

Generator names must be unique.

For every generator, the corresponding uppercase letter is automatically assigned as its inverse. Thus:

```text
a <-> A
b <-> B
```

---

## Multiplication of words

Words can be multiplied using `*`.

For example:

```python
a = Word("a")
b = Word("b")

w = a * b
```

gives:

```text
ab
```

Multiplication corresponds to concatenation:

$$
ab\cdot cd=abcd.
$$

The order of the letters is preserved.

Multiplication also accepts strings:

```python
a * "b"
```

and:

```python
"a" * b
```

are both supported.

---

## Powers of words

Words support integer powers using `**`.

For a positive integer:

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
# e
```

Negative powers use the inverse word:

```python
Word("a") ** -1
# A
```

For example:

```python
Word("ab") ** -1
```

produces:

```text
BA
```

because

$$
(ab)^{-1}=b^{-1}a^{-1}.
$$

---

## Inverses of words

The inverse of a word can be obtained with:

```python
w.inverse()
```

or with the `~` operator:

```python
~w
```

For example:

```python
w = Word("abC")
w.inverse()
```

gives:

```text
cBA
```

The inverse reverses the word and replaces every generator by its inverse.

For

$$
w=x_1x_2\cdots x_n,
$$

we have

$$
w^{-1}=x_n^{-1}\cdots x_2^{-1}x_1^{-1}.
$$

---

## Free reduction

Words are freely reduced before relations are applied.

A generator and its inverse cancel:

$$
xx^{-1}=e,
\qquad
x^{-1}x=e.
$$

For example:

```text
aAbB -> e
abBA -> e
```

and:

```text
abBa -> aa
```

after the inverse pair `bB` is cancelled.

Free reduction is independent of the defining relations of the group.

---

# Presented groups – ⚠️ under development

## Creating a presentation

A presented group is created with:

```python
PresentedGroup(generators, relations)
```

For example, the cyclic group of order $3$ can be presented as

$$
C_3=\langle a\mid a^3=e\rangle.
$$

In GroupMaker:

```python
a = Word("a")

C3 = PresentedGroup(
    [a],
    [a**3]
)
```

Every supplied relation is interpreted as being equal to the identity.

---

## Multiple generators

Presentations can contain several generators.

For example,

$$
G=\langle a,b\mid a^2,b^2,(ab)^3\rangle
$$

can be written as:

```python
a = Word("a")
b = Word("b")

G = PresentedGroup(
    [a, b],
    [a**2, b**2, (a*b)**3]
)
```

---

## Relations

Relations can be supplied as `Word` objects or as strings.

For example:

```python
G = PresentedGroup(
    [Word("a")],
    ["aaa"]
)
```

is equivalent to:

```python
G = PresentedGroup(
    [Word("a")],
    [Word("aaa")]
)
```

Relations are checked to ensure that they only contain generators belonging to the presentation and their inverses.

For example, if the generators are `a` and `b`, then:

```text
abBA
```

is valid.

A word containing an unrelated generator is rejected.

---

## Stored relations

Relations are freely reduced when the presentation is created.

The resulting relations are stored in:

```python
G.relations
```

For example, inverse pairs contained in a relation are removed before the relation is stored.

---

# Reducing words using relations

## The reduction process

For a presentation

$$
G=\langle X\mid R\rangle,
$$

GroupMaker attempts to obtain a shorter representative of a word using the defining relations.

Reduction takes place in two stages:

1. Free reduction.
2. Reduction using rules derived from the defining relations.

The relation-reduction process repeatedly applies rules while they produce a strictly shorter word.

---

## Relation rewriting rules

For every defining relation

$$
r=e,
$$

GroupMaker constructs rewriting rules.

The relator and its inverse can be replaced by the identity:

$$
r\to e,
\qquad
r^{-1}\to e.
$$

Additional rules are derived by isolating each generator or inverse appearing in the relation.

For example, from:

$$
aaa=e,
$$

the system can derive:

$$
A\to aa
$$

and the shorter normal-form rule:

$$
aa\to A.
$$

These rules are generated automatically by `_relation_rules()`.

---

## Reducing a word

The complete reduction is performed internally by `_reduce()`.

For normal use, this private method should not need to be called directly. Public group operations automatically reduce their results.

For example:

```python
G.operation("a", "aa")
```

concatenates the two words and reduces the result.

Likewise:

```python
G.inverse("a")
```

calculates and reduces the inverse.

---

# Group operations

## The group operation

`PresentedGroup` implements the group operation through:

```python
G.operation(elem1, elem2)
```

The arguments may be `Word` objects or strings.

For example:

```python
a = Word("a")

G = PresentedGroup(
    [a],
    [a**3]
)

G.operation("a", "aa")
```

The words are concatenated and then reduced using the defining relations.

For

$$
\langle a\mid a^3\rangle,
$$

the result represents:

$$
a\cdot a^2=a^3=e.
$$

---

## Identity

The identity element is returned by:

```python
G.identity()
```

For a `PresentedGroup`, this is:

```python
Word("e")
```

---

## Inverses

The inverse of an element can be obtained with:

```python
G.inverse(element)
```

For example:

```python
G.inverse("a")
```

returns the reduced inverse word.

For a generator `a`, the uppercase letter `A` represents $a^{-1}$.

Relations may reduce this inverse further. For example, from

$$
a^3=e,
$$

we obtain

$$
a^{-1}=a^2.
$$

---

# Converting a presentation into a finite group

## `toCayleyGroup()`

A `PresentedGroup` does not initially store its elements as a Cayley table.

Its elements are represented by reduced words.

A finite group can be enumerated and converted into a `CayleyGroup` using:

```python
G.toCayleyGroup()
```

The conversion explores the group using breadth-first search (BFS).

Starting from the identity, GroupMaker repeatedly multiplies each discovered element by every generator and every inverse generator.

---

## Breadth-first exploration

Suppose the generators are:

```text
a, b
```

The enumeration starts at:

```text
e
```

and explores products with:

```text
a, b, A, B
```

New reduced words are added to the enumeration as they are discovered.

Each distinct reduced word receives an internal index.

The resulting correspondence is conceptually:

```text
reduced word -> element index
```

Once all elements have been discovered, GroupMaker constructs the Cayley table by evaluating the product of every pair of discovered words.

---

## Generator and inverse exploration

The enumeration uses both the generators and their inverses.

For generators:

```text
a, b
```

the exploration set is:

```text
a, b, A, B
```

This ensures that the search can move through the group in both directions.

The process starts from the identity and continues until the queue of undiscovered elements is empty.

If the process terminates, the complete finite group has been enumerated.

---

## Maximum number of elements

By default, `toCayleyGroup()` allows at most:

```python
1000
```

discovered elements.

This can be changed using `max_elements`:

```python
G.toCayleyGroup(max_elements=5000)
```

If the enumeration reaches the limit before the group is completely discovered, an `OverflowError` is raised.

This is particularly important for infinite groups and very large finite groups.

For example:

```python
G.toCayleyGroup(max_elements=100)
```

will stop if more than 100 elements are required.

---

## Caching

The Cayley representation is cached in the `_cayley_cache` attribute.

Therefore, after:

```python
C = G.toCayleyGroup()
```

a subsequent call to:

```python
G.toCayleyGroup()
```

can return the cached representation instead of enumerating the group again.

---

## Order

The order of a `PresentedGroup` is obtained through its Cayley representation:

```python
G.order()
```

Internally, this is equivalent to obtaining the Cayley group and asking for its order.

Consequently, the group must be completely enumerable within the selected element limit.

---

# Converting to an explicit group

A presented group can also be converted to an `ExplicitGroup`:

```python
G.toExplicitGroup()
```

This first obtains the Cayley representation and then converts it into an explicit group.

Therefore, the same finite-enumeration requirements apply.

---

# Inspecting a presentation

The generator names can be inspected using:

```python
G.generators_names
```

For example:

```python
G.generators_names
# ['a', 'b']
```

The defining relations are stored in:

```python
G.relations
```

The complete presentation can be displayed with:

```python
print(G)
```

For example:

```text
〈 a, b | aa, bbb 〉
```

The `__repr__` representation is the same as the string representation.

---

# Membership

A word can be tested for membership in a `PresentedGroup` using `in`.

For example:

```python
"a" in G
```

or:

```python
Word("ab") in G
```

The element is first interpreted as a valid word using the generators and their inverses.

If the object cannot be interpreted as a valid word, membership returns `False`.

---

# A complete example

The following example constructs the cyclic group of order $3$, performs operations using its presentation, and converts it into a Cayley group.

```python
from groupsmath.presentations import Word, PresentedGroup

a = Word("a")

C3 = PresentedGroup(
    [a],
    [a**3]
)

print(C3)
# 〈 a | aaa 〉

print(C3.identity())
# e

print(C3.operation("a", "aa"))
# e

print(C3.inverse("a"))
# aa

C3_cayley = C3.toCayleyGroup()

print(C3_cayley.order())
# 3

C3_cayley.cayley_table(
    title="Cyclic group C3"
)
```

The presentation

$$
\langle a\mid a^3\rangle
$$

therefore provides a compact way of specifying a group through generators and relations, while `toCayleyGroup()` provides a bridge from this symbolic representation to the finite Cayley-table representation used elsewhere in GroupMaker.
