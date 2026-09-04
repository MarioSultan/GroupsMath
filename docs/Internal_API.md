# GroupsMath Internal API

A structural reference to the functions, methods, classes, and module-level variables found in the supplied source files. Each identifier is quoted for readability; descriptions are intentionally brief and reflect the implementation.

---

# `core.py`

## Module-level variables

- **`"__version__"`** — Stores the current library version string.
- **`"__errorcolor__"`** — Stores the ANSI escape sequence used to color error messages.
- **`"tgl_color"`** — Stores the base color used by the `tgl` colormap.
- **`"white"`** — Provides a white-only matplotlib colormap.
- **`"tgl"`** — Provides a two-color matplotlib colormap based on `tgl_color`.
- **`"rainbow"`** — Provides the library's six-color matplotlib colormap.
- **`"rainbow8"`** — Provides the library's eight-color matplotlib colormap.
- **`"standard"`** — Stores the standard palette used by visualization helpers.

## Classes

### `"Group"`

Defines a class used by the module.

#### Methods

- **`"operation(self, a, b)"`** — Implements the `operation` operation for the class.
- **`"identity(self)"`** — Implements the `identity` operation for the class.
- **`"inverse(self, a)"`** — Implements the `inverse` operation for the class.

### `"ExplicitGroup"`

Defines a class used by the module.

#### Methods

- **`"__init__(self, elements, function, _skip_validation)"`** — Initializes an instance and stores or validates its main configuration.
- **`"__str__(self)"`** — Returns a human-readable string representation.
- **`"__len__(self)"`** — Returns the relevant size or order.
- **`"__contains__(self, element)"`** — Checks whether an item belongs to the object.
- **`"__mul__(self, other)"`** — Implements multiplication or the module's group-product operation.
- **`"__pow__(self, n)"`** — Implements exponentiation of the object.
- **`"__truediv__(self, subgroup)"`** — Implements division using the module's quotient operation.
- **`"toCayleyGroup(self)"`** — Implements the `toCayleyGroup` operation for the class.
- **`"_cayley(self)"`** — Implements the `_cayley` operation for the class.
- **`"operation(self, a, b)"`** — Implements the `operation` operation for the class.
- **`"identity(self)"`** — Implements the `identity` operation for the class.
- **`"inverse(self, a)"`** — Implements the `inverse` operation for the class.
- **`"order(self)"`** — Implements the `order` operation for the class.
- **`"element_orders(self)"`** — Implements the `element_orders` operation for the class.
- **`"order_distribution(self)"`** — Implements the `order_distribution` operation for the class.
- **`"is_cyclic(self)"`** — Implements the `is_cyclic` operation for the class.
- **`"center(self)"`** — Implements the `center` operation for the class.
- **`"is_abelian(self)"`** — Implements the `is_abelian` operation for the class.
- **`"cayley_table(self, title, colormap, names, math_mode)"`** — Implements the `cayley_table` operation for the class.
- **`"cayley_graph(self, generators, title, colormap, names, edgenames, math_mode, node_size)"`** — Implements the `cayley_graph` operation for the class.
- **`"proper_subgroups(self)"`** — Implements the `proper_subgroups` operation for the class.
- **`"subgroups(self)"`** — Implements the `subgroups` operation for the class.
- **`"normal_subgroups(self)"`** — Implements the `normal_subgroups` operation for the class.
- **`"is_simple(self)"`** — Implements the `is_simple` operation for the class.
- **`"quotient(self, subgroup)"`** — Implements the `quotient` operation for the class.
- **`"centralizer(self, element)"`** — Implements the `centralizer` operation for the class.
- **`"conjugacy_class(self, element)"`** — Implements the `conjugacy_class` operation for the class.
- **`"conjugacy_classes(self)"`** — Implements the `conjugacy_classes` operation for the class.
- **`"commutator(self, a, b)"`** — Implements the `commutator` operation for the class.
- **`"commutator_subgroup(self)"`** — Implements the `commutator_subgroup` operation for the class.
- **`"derived_subgroup(self, n)"`** — Implements the `derived_subgroup` operation for the class.
- **`"derived_series(self)"`** — Implements the `derived_series` operation for the class.
- **`"abelianization(self)"`** — Implements the `abelianization` operation for the class.
- **`"is_solvable(self)"`** — Implements the `is_solvable` operation for the class.
- **`"is_automorphism(self, phi)"`** — Implements the `is_automorphism` operation for the class.
- **`"automorphisms(self)"`** — Implements the `automorphisms` operation for the class.
- **`"automorphism_group(self)"`** — Implements the `automorphism_group` operation for the class.
- **`"generators(self)"`** — Devuelve un conjunto de generadores que genera todo el grupo.
- **`"generates(self, subset)"`** — Comprueba si un subconjunto de elementos genera el grupo.
- **`"is_isomorphic_to(self, target)"`** — Implements the `is_isomorphic_to` operation for the class.

### `"CayleyGroup"`

Defines a class used by the module.

#### Methods

- **`"__init__(self, cayley, elements, _skip_validation)"`** — Initializes an instance and stores or validates its main configuration.
- **`"__str__(self)"`** — Returns a human-readable string representation.
- **`"__len__(self)"`** — Returns the relevant size or order.
- **`"__contains__(self, element)"`** — Checks whether an item belongs to the object.
- **`"__mul__(self, other)"`** — Implements multiplication or the module's group-product operation.
- **`"__pow__(self, n)"`** — Implements exponentiation of the object.
- **`"__truediv__(self, subgroup)"`** — Implements division using the module's quotient operation.
- **`"toExplicitGroup(self)"`** — Implements the `toExplicitGroup` operation for the class.
- **`"operation(self, a, b)"`** — Implements the `operation` operation for the class.
- **`"identity(self)"`** — Implements the `identity` operation for the class.
- **`"inverse(self, a)"`** — Implements the `inverse` operation for the class.
- **`"_print_group(self)"`** — Implements the `_print_group` operation for the class.
- **`"order(self)"`** — Implements the `order` operation for the class.
- **`"element_orders(self)"`** — Implements the `element_orders` operation for the class.
- **`"order_distribution(self)"`** — Implements the `order_distribution` operation for the class.
- **`"is_cyclic(self)"`** — Implements the `is_cyclic` operation for the class.
- **`"center(self)"`** — Implements the `center` operation for the class.
- **`"is_abelian(self)"`** — Implements the `is_abelian` operation for the class.
- **`"cayley_table(self, title, colormap, names, math_mode)"`** — Implements the `cayley_table` operation for the class.
- **`"delete_names(self)"`** — Implements the `delete_names` operation for the class.
- **`"cayley_graph(self, generators, title, colormap, names, edgenames, math_mode, node_size)"`** — Implements the `cayley_graph` operation for the class.
- **`"proper_subgroups(self)"`** — Implements the `proper_subgroups` operation for the class.
- **`"subgroups(self)"`** — Implements the `subgroups` operation for the class.
- **`"normal_subgroups(self)"`** — Implements the `normal_subgroups` operation for the class.
- **`"is_simple(self)"`** — Implements the `is_simple` operation for the class.
- **`"quotient(self, subgroup)"`** — Implements the `quotient` operation for the class.
- **`"centralizer(self, element)"`** — Implements the `centralizer` operation for the class.
- **`"conjugacy_class(self, element)"`** — Implements the `conjugacy_class` operation for the class.
- **`"conjugacy_classes(self)"`** — Implements the `conjugacy_classes` operation for the class.
- **`"commutator(self, a, b)"`** — Implements the `commutator` operation for the class.
- **`"commutator_subgroup(self)"`** — Implements the `commutator_subgroup` operation for the class.
- **`"derived_subgroup(self, n)"`** — Implements the `derived_subgroup` operation for the class.
- **`"derived_series(self)"`** — Implements the `derived_series` operation for the class.
- **`"abelianization(self)"`** — Implements the `abelianization` operation for the class.
- **`"is_solvable(self)"`** — Implements the `is_solvable` operation for the class.
- **`"hasse_diagram(self)"`** — Implements the `hasse_diagram` operation for the class.
- **`"is_automorphism(self, phi)"`** — Implements the `is_automorphism` operation for the class.
- **`"automorphisms(self)"`** — Calcula automorfismos propagando asignaciones sobre los generadores del grupo.
- **`"automorphism_group(self)"`** — Implements the `automorphism_group` operation for the class.
- **`"generators(self)"`** — Devuelve una lista con los elementos de un conjunto generador minimal.
- **`"generates(self, subset)"`** — Comprueba si un subconjunto de elementos genera el grupo.
- **`"is_isomorphic_to(self, target)"`** — Comprueba si el grupo actual es isomorfo al grupo 'target'.

### `"Subgroup"`

Defines a class used by the module.

### `"ExplicitSubgroup"`

Defines a class used by the module.

#### Methods

- **`"__init__(self, subgroup, group)"`** — Initializes an instance and stores or validates its main configuration.
- **`"__truediv__(self, other)"`** — Implements division using the module's quotient operation.
- **`"__le__(self, group)"`** — Implements the less-than-or-equal comparison.
- **`"__lt__(self, group)"`** — Implements the strict less-than comparison.
- **`"coset(self, element, side, return_names)"`** — Implements the `coset` operation for the class.
- **`"is_normal(self)"`** — Implements the `is_normal` operation for the class.
- **`"quotient(self)"`** — Calcula el grupo cociente G/H devolviendo una instancia de ExplicitGroup.

### `"CayleySubgroup"`

Defines a class used by the module.

#### Methods

- **`"__init__(self, subgroup, group)"`** — Initializes an instance and stores or validates its main configuration.
- **`"__truediv__(self, other)"`** — Permite usar la sintaxis natural G / H o H / H.
- **`"__le__(self, group)"`** — Implements the less-than-or-equal comparison.
- **`"__lt__(self, group)"`** — Implements the strict less-than comparison.
- **`"_isin(self, subgroup)"`** — Implements the `_isin` operation for the class.
- **`"_is_covered(self, other)"`** — Implements the `_is_covered` operation for the class.
- **`"coset(self, element, side, return_names)"`** — Implements the `coset` operation for the class.
- **`"is_normal(self)"`** — Implements the `is_normal` operation for the class.
- **`"quotient(self)"`** — Calcula el grupo cociente G/H devolviendo una instancia de CayleyGroup.

### `"Element"`

Defines a class used by the module.

#### Methods

- **`"__init__(self, element, group)"`** — Initializes an instance and stores or validates its main configuration.
- **`"__str__(self)"`** — Returns a human-readable string representation.
- **`"__mul__(self, other)"`** — Implements multiplication or the module's group-product operation.
- **`"__pow__(self, k)"`** — Implements exponentiation of the object.
- **`"__eq__(self, other)"`** — Compares the object with another compatible object.
- **`"inverse(self)"`** — Implements the `inverse` operation for the class.
- **`"order(self)"`** — Implements the `order` operation for the class.

### `"Automorphism"`

Defines a class used by the module.

#### Methods

- **`"__init__(self, phi, group)"`** — Initializes an instance and stores or validates its main configuration.
- **`"__len__(self)"`** — Returns the relevant size or order.
- **`"__str__(self)"`** — Returns a human-readable string representation.

### `"AutomorphismFunction"`

Defines a class used by the module.

#### Methods

- **`"__init__(self, function, group)"`** — Initializes an instance and stores or validates its main configuration.
- **`"__str__(self)"`** — Returns a human-readable string representation.

## Module-level functions

- **`"groupsmath_info()"`** — Implements a module-level operation.
- **`"_obtener_nombre(var_obj)"`** — Implements a module-level operation.
- **`"_is_closed(tabla)"`** — Implements a module-level operation.
- **`"_check_cayley_group(tabla)"`** — Implements a module-level operation.
- **`"_check_explicit_group(elements, operation)"`** — Implements a module-level operation.
- **`"_identity(G)"`** — Implements a module-level operation.
- **`"_subset(G, elements)"`** — Implements a module-level operation.
- **`"_form_subgroup(G, elements)"`** — Implements a module-level operation.
- **`"_sign(p)"`** — Devuelve: 1 -> permutación par -1 -> permutación impar.
- **`"_renamed_elements(G, L)"`** — Implements a module-level operation.
- **`"_get_elements(G)"`** — Devuelve una lista con todos los elementos/nombres únicos que aparecen dentro de la tabla de Cayley G, conservando el orden de primera aparición.
- **`"_min_div(n)"`** — Implements a module-level operation.
- **`"_graded_power_set_with_id(orders)"`** — Implements a module-level operation.
- **`"_is_closed_subset(G_cayley, indices)"`** — Comprueba clausura en O(|H|^2) usando un conjunto de índices.
- **`"_operate_cosets(G, C, A, B)"`** — Implements a module-level operation.
- **`"_subgroup_generated_by(cayley, generators_indices)"`** — Implements a module-level operation.
- **`"_order_preserving_permutations(orders)"`** — Implements a module-level operation.
- **`"direct_product(A, B)"`** — Implements a module-level operation.
- **`"direct_power(G, n)"`** — Implements a module-level operation.
- **`"semidirect_product(A, B, f)"`** — Implements a module-level operation.
- **`"are_isomorphic(G, H)"`** — Devuelve True si los grupos G y H son isomorfos, False en caso contrario.
- **`"cyclic_group(n)"`** — Implements a module-level operation.
- **`"symmetric_group(n)"`** — Implements a module-level operation.
- **`"alternating_group(n)"`** — Implements a module-level operation.
- **`"dihedric_group(n)"`** — Implements a module-level operation.
- **`"quaternion_group()"`** — Implements a module-level operation.
- **`"units_group(n)"`** — Implements a module-level operation.
- **`"dicyclic_group(n)"`** — Genera la tabla de Cayley del grupo dicíclico Dic_n (de orden 4n).
- **`"tetrahedral_group()"`** — Full symmetry group of the tetrahedron.
- **`"octahedral_group()"`** — Full symmetry group of the cube/octahedron.
- **`"icosahedral_group()"`** — Full symmetry group of the icosahedron/dodecahedron.
- **`"cayley_table(G, title, colormap, names, renaming, math_mode)"`** — Implements a module-level operation.
- **`"_renaming_C(n)"`** — Implements a module-level operation.
- **`"_renaming_S(n)"`** — Renombrado para S_n en notación de ciclos.
- **`"_renaming_A(n)"`** — Renombrado para A_n en notación de ciclos.
- **`"_renaming_D(n)"`** — Implements a module-level operation.
- **`"_renaming_Q8()"`** — Implements a module-level operation.
- **`"_renaming_U(n)"`** — Implements a module-level operation.
- **`"_renaming_Dic(n)"`** — Implements a module-level operation.
- **`"_reset_renaming(G)"`** — Implements a module-level operation.

## Nested/internal functions

- **`"quaternion_group.multiply(a, b)"`** — Internal helper used only within its enclosing function.
- **`"_renaming_S.tuple_to_cycle(p)"`** — Internal helper used only within its enclosing function.
- **`"_renaming_A.tuple_to_cycle(p)"`** — Internal helper used only within its enclosing function.
- **`"proper_subgroups.is_closed(elem, func)"`** — Internal helper used only within its enclosing function.
- **`"toExplicitGroup.op(a, b)"`** — Internal helper used only within its enclosing function.
- **`"quotient.quotient_op(coset_name_a, coset_name_b)"`** — Internal helper used only within its enclosing function.

---

# `matrixgroups.py`

## Classes

### `"MatrixGroup"`

Defines a class used by the module.

#### Methods

- **`"__init__(self, n, field, condition, p)"`** — Initializes an instance and stores or validates its main configuration.
- **`"__contains__(self, matrix)"`** — Checks whether an item belongs to the object.
- **`"operation(self, A, B)"`** — Implements the `operation` operation for the class.
- **`"identity(self)"`** — Implements the `identity` operation for the class.
- **`"inverse(self, A)"`** — Implements the `inverse` operation for the class.
- **`"_determinant(self, A)"`** — Implements the `_determinant` operation for the class.
- **`"_cayley(self)"`** — Implements the `_cayley` operation for the class.
- **`"toCayleyGroup(self)"`** — Implements the `toCayleyGroup` operation for the class.
- **`"toExplicitGroup(self)"`** — Implements the `toExplicitGroup` operation for the class.
- **`"_is_finite(self)"`** — Implements the `_is_finite` operation for the class.
- **`"order(self)"`** — Implements the `order` operation for the class.
- **`"elements(self)"`** — Implements the `elements` operation for the class.
- **`"cayley_table(self, title, colormap, names)"`** — Implements the `cayley_table` operation for the class.

### `"MatrixSubgroup"`

Defines a class used by the module.

#### Methods

- **`"__init__(self, subgroup, group)"`** — Initializes an instance and stores or validates its main configuration.

## Module-level functions

- **`"_is_prime(n)"`** — Implements a module-level operation.
- **`"_check_field(M, field, p)"`** — Implements a module-level operation.
- **`"_matrix_to_str(M)"`** — Implements a module-level operation.
- **`"GL(n, field, p)"`** — General Linear Group GL_n(F).
- **`"SL(n, field, p)"`** — Special Linear Group SL_n(F).
- **`"O(n, field, p)"`** — Orthogonal Group O_n(R).
- **`"SO(n, field, p)"`** — Special Orthogonal Group SO_n(R).
- **`"U(n)"`** — Unitary Group U(n).
- **`"SU(n)"`** — Special Unitary Group SU(n).
- **`"Sp(n, field, p)"`** — Symplectic Group Sp(n, R).

---

# `precooked.py`

## Module-level variables

- **`"I"`** — Stores a module-level value used by the module's implementation.
- **`"C1"`** — Stores a module-level value used by the module's implementation.
- **`"C2"`** — Stores a module-level value used by the module's implementation.
- **`"C3"`** — Stores a module-level value used by the module's implementation.
- **`"C4"`** — Stores a module-level value used by the module's implementation.
- **`"C5"`** — Stores a module-level value used by the module's implementation.
- **`"C6"`** — Stores a module-level value used by the module's implementation.
- **`"C7"`** — Stores a module-level value used by the module's implementation.
- **`"C8"`** — Stores a module-level value used by the module's implementation.
- **`"C9"`** — Stores a module-level value used by the module's implementation.
- **`"C10"`** — Stores a module-level value used by the module's implementation.
- **`"C11"`** — Stores a module-level value used by the module's implementation.
- **`"C12"`** — Stores a module-level value used by the module's implementation.
- **`"C13"`** — Stores a module-level value used by the module's implementation.
- **`"C14"`** — Stores a module-level value used by the module's implementation.
- **`"C15"`** — Stores a module-level value used by the module's implementation.
- **`"C16"`** — Stores a module-level value used by the module's implementation.
- **`"C17"`** — Stores a module-level value used by the module's implementation.
- **`"C18"`** — Stores a module-level value used by the module's implementation.
- **`"C19"`** — Stores a module-level value used by the module's implementation.
- **`"C20"`** — Stores a module-level value used by the module's implementation.
- **`"A1"`** — Stores a module-level value used by the module's implementation.
- **`"A2"`** — Stores a module-level value used by the module's implementation.
- **`"A3"`** — Stores a module-level value used by the module's implementation.
- **`"A4"`** — Stores a module-level value used by the module's implementation.
- **`"S1"`** — Stores a module-level value used by the module's implementation.
- **`"S2"`** — Stores a module-level value used by the module's implementation.
- **`"S3"`** — Stores a module-level value used by the module's implementation.
- **`"S4"`** — Stores a module-level value used by the module's implementation.
- **`"D1"`** — Stores a module-level value used by the module's implementation.
- **`"D2"`** — Stores a module-level value used by the module's implementation.
- **`"D3"`** — Stores a module-level value used by the module's implementation.
- **`"D4"`** — Stores a module-level value used by the module's implementation.
- **`"D5"`** — Stores a module-level value used by the module's implementation.
- **`"D6"`** — Stores a module-level value used by the module's implementation.
- **`"D7"`** — Stores a module-level value used by the module's implementation.
- **`"D8"`** — Stores a module-level value used by the module's implementation.
- **`"D9"`** — Stores a module-level value used by the module's implementation.
- **`"D10"`** — Stores a module-level value used by the module's implementation.
- **`"V4"`** — Stores a module-level value used by the module's implementation.
- **`"Q8"`** — Stores a module-level value used by the module's implementation.
- **`"U2"`** — Stores a module-level value used by the module's implementation.
- **`"U3"`** — Stores a module-level value used by the module's implementation.
- **`"U4"`** — Stores a module-level value used by the module's implementation.
- **`"U5"`** — Stores a module-level value used by the module's implementation.
- **`"U6"`** — Stores a module-level value used by the module's implementation.
- **`"U7"`** — Stores a module-level value used by the module's implementation.
- **`"U8"`** — Stores a module-level value used by the module's implementation.
- **`"U9"`** — Stores a module-level value used by the module's implementation.
- **`"U10"`** — Stores a module-level value used by the module's implementation.
- **`"U11"`** — Stores a module-level value used by the module's implementation.
- **`"U12"`** — Stores a module-level value used by the module's implementation.
- **`"U13"`** — Stores a module-level value used by the module's implementation.
- **`"U14"`** — Stores a module-level value used by the module's implementation.
- **`"U15"`** — Stores a module-level value used by the module's implementation.
- **`"U16"`** — Stores a module-level value used by the module's implementation.
- **`"U17"`** — Stores a module-level value used by the module's implementation.
- **`"U18"`** — Stores a module-level value used by the module's implementation.
- **`"U19"`** — Stores a module-level value used by the module's implementation.
- **`"U20"`** — Stores a module-level value used by the module's implementation.
- **`"Dic2"`** — Stores a module-level value used by the module's implementation.
- **`"Dic3"`** — Stores a module-level value used by the module's implementation.
- **`"Dic4"`** — Stores a module-level value used by the module's implementation.

---

# `presentations.py`

## Classes

### `"Word"`

Defines a class used by the module.

#### Methods

- **`"__init__(self, word, _skip_validation)"`** — Initializes an instance and stores or validates its main configuration.
- **`"__mul__(self, other)"`** — Implements multiplication or the module's group-product operation.
- **`"__rmul__(self, other)"`** — Implements the `__rmul__` operation for the class.
- **`"__pow__(self, n)"`** — Implements exponentiation of the object.
- **`"__eq__(self, other)"`** — Compares the object with another compatible object.
- **`"__invert__(self)"`** — Implements unary inversion.
- **`"__len__(self)"`** — Returns the relevant size or order.
- **`"__str__(self)"`** — Returns a human-readable string representation.
- **`"__hash__(self)"`** — Implements the `__hash__` operation for the class.
- **`"inverse(self)"`** — Implements the `inverse` operation for the class.

### `"PresentedGroup"`

Defines a class used by the module.

#### Methods

- **`"__init__(self, generators, relations)"`** — Initializes an instance and stores or validates its main configuration.
- **`"_validate_word_alphabet(self, word)"`** — Implements the `_validate_word_alphabet` operation for the class.
- **`"_to_word(self, element)"`** — Implements the `_to_word` operation for the class.
- **`"_free_reduce(self, word)"`** — Reduce libremente una palabra eliminando pares xx^{-1} y x^{-1}x.
- **`"_relation_rules(self)"`** — Construye reglas de reescritura a partir de las relaciones.
- **`"_relation_reduce_once(self, word)"`** — Aplica una regla de reescritura una sola vez.
- **`"_reduce(self, word)"`** — Reducción completa de una palabra.
- **`"operation(self, elem1, elem2)"`** — Implements the `operation` operation for the class.
- **`"identity(self)"`** — Implements the `identity` operation for the class.
- **`"inverse(self, elem)"`** — Implements the `inverse` operation for the class.
- **`"__contains__(self, elem)"`** — Checks whether an item belongs to the object.
- **`"toCayleyGroup(self, max_elements)"`** — Construye una representación mediante tabla de Cayley explorando el grupo mediante BFS.
- **`"toExplicitGroup(self)"`** — Implements the `toExplicitGroup` operation for the class.
- **`"order(self)"`** — Implements the `order` operation for the class.
- **`"__str__(self)"`** — Returns a human-readable string representation.
- **`"__repr__(self)"`** — Returns a developer-oriented representation.

## Nested/internal functions

- **`"inverse._invert(a)"`** — Internal helper used only within its enclosing function.

---

# `shortcuts.py`

## Module-level variables

- **`"C"`** — Stores a module-level value used by the module's implementation.
- **`"S"`** — Stores a module-level value used by the module's implementation.
- **`"A"`** — Stores a module-level value used by the module's implementation.
- **`"D"`** — Stores a module-level value used by the module's implementation.
- **`"U"`** — Stores a module-level value used by the module's implementation.
- **`"Dic"`** — Stores a module-level value used by the module's implementation.
- **`"Tet"`** — Stores a module-level value used by the module's implementation.
- **`"Cub"`** — Stores a module-level value used by the module's implementation.
- **`"Oct"`** — Stores a module-level value used by the module's implementation.
- **`"Dod"`** — Stores a module-level value used by the module's implementation.
- **`"Ico"`** — Stores a module-level value used by the module's implementation.

---

# `structure.py`

## Module-level functions

- **`"structure_description(G)"`** — Characterizes the algebraic structure of group `"G"` without using pre-defined tables, returning group notation (e.g., `'C2 x C2'`, `'S3'`).

## Hidden functions

- **`"_decompose_abelian(G)"`** — Decomposes an abelian group `"G"` into direct product cyclic factors such as `'C_d1 x C_d2'`.
- **`"_find_complement(G, N)"`** — Searches for a subgroup `"H"` of `"G"` satisfying `"N & H = {e}"` and `"|N| * |H| = |G|"`.
- **`"_describe_simple(G)"`** — Identifies and returns the family name of a simple group `"G"` based on its order and properties.
