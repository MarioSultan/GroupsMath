from .core import *
from .core import __errorcolor__
from collections import deque

#################### WARNINGS ####################

print("\033[33m[!] WARNING: The library 'groupsmath.presentations' is under development and it might produce errors.\033[0m")


#################### PRESENTATIONS ####################

class Word():

    def __init__(self,word,_skip_validation=False):

        if type(word)!=str:
            raise ValueError (__errorcolor__+"The word has to be a string.")

        l = []

        if word=="" or word=="e":
            word = ""

        for i in word:
            l.append(i)
            if i not in "qwrtyuiopasdfghjklzxcvbnmQWRTYUIOPASDFGHJKLZXCVBNM":
                raise ValueError (__errorcolor__+"The word must consist of Latin characters except the letters e/E.")
        
        self.word = word
        self.characters = l

    def __mul__(self,other):
        o = other if isinstance(other, Word) else Word(other)
        return Word(self.word+o.word)

    def __rmul__(self,other):
        o = other if isinstance(other, Word) else Word(other)
        return Word(o.word+self.word)

    def __pow__(self,n):
        if n==0:
            return Word("e")
        elif n>0:
            return Word(self.word*n)
        elif n<0:
            return Word(self.inverse().word*-n)

    def __eq__(self,other):
        if not isinstance(other, Word):
            return NotImplemented
        return self.word == other.word

    def __invert__(self):
        return self.inverse()

    def __len__(self):
        return len(self.word)

    def __str__(self):
        if self.word=="":
            return "e"
        return self.word

    def __hash__(self):
        return hash(self.word)

    def inverse(self):

        def _invert(a):
            if a in "qwrtyuiopasdfghjklzxcvbnm":
                return a.upper()
            else:
                return a.lower()

        if self.word=="":
            return self

        I = ""
        n = len(self)

        for i in range(n):
            I+= _invert(self.word[n-i-1])

        return Word(I)

''' Revisar por si aparecen errores '''

class PresentedGroup(Group):

    def __init__(self, generators: list, relations: list):

        # ---------------------------------------------------------
        # 1. GENERADORES
        # ---------------------------------------------------------

        self.generators_names = []

        for g in generators:
            g_str = str(g).strip()

            if len(g_str) != 1 or not g_str.islower() or not g_str.isalpha():
                raise ValueError(
                    __errorcolor__ +
                    f"Generators must be single lowercase Latin letters. Invalid: '{g}'"
                )

            if g_str in self.generators_names:
                raise ValueError(
                    __errorcolor__ +
                    f"Duplicate generator: '{g_str}'"
                )

            self.generators_names.append(g_str)

        # a <-> A
        self.inverses_map = {
            g: g.upper()
            for g in self.generators_names
        }

        self.inverses_map.update({
            g.upper(): g
            for g in self.generators_names
        })

        # ---------------------------------------------------------
        # 2. RELACIONES
        # ---------------------------------------------------------

        self.relations = []

        for r in relations:

            w = r if isinstance(r, Word) else Word(str(r))

            self._validate_word_alphabet(w)

            # Las relaciones se almacenan libremente reducidas.
            w = self._free_reduce(w)

            self.relations.append(w)

        # ---------------------------------------------------------
        # 3. CACHE
        # ---------------------------------------------------------

        self._cayley_cache = None


    # =============================================================
    # VALIDACIÓN
    # =============================================================

    def _validate_word_alphabet(self, word: Word):

        valid_chars = (
            set(self.generators_names)
            |
            set(self.inverses_map.keys())
        )

        for char in word.word:

            if char not in valid_chars:

                raise ValueError(
                    __errorcolor__ +
                    f"Character '{char}' in word '{word}' "
                    f"is not a valid generator for this group."
                )


    def _to_word(self, element) -> Word:

        if isinstance(element, Word):
            w = element

        elif isinstance(element, str):
            w = Word(element)

        else:
            raise TypeError(
                __errorcolor__ +
                f"Element must be a Word or str, "
                f"got {type(element).__name__}"
            )

        self._validate_word_alphabet(w)

        return w


    # =============================================================
    # REDUCCIÓN LIBRE
    # =============================================================

    def _free_reduce(self, word: Word) -> Word:
        """
        Reduce libremente una palabra eliminando pares xx^{-1}
        y x^{-1}x.

        Ejemplo:

            aAbB -> e
            abBA -> e
            a b B a -> aa
        """

        stack = []

        for char in word.word:

            if stack and self.inverses_map.get(stack[-1]) == char:
                stack.pop()

            else:
                stack.append(char)

        return Word(
            "".join(stack),
            _skip_validation=True
        )


    # =============================================================
    # RELACIONES
    # =============================================================

    def _relation_rules(self):
        """
        Construye reglas de reescritura a partir de las relaciones.

        Para una relación:

            r = x1 x2 ... xn = e

        se generan:

        1. El relator y su inverso:
            r -> e
            r^-1 -> e

        2. Reglas derivadas aislando cada generador/inverso.

        Por ejemplo:

            aaa = e

        implica:

            A = aa

        y, para obtener una forma normal más corta:

            aa -> A
        """

        rules = []

        for relation in self.relations:

            relation = self._free_reduce(relation)

            if len(relation) == 0:
                continue

            s = relation.word
            n = len(s)

            # ---------------------------------------------------------
            # 1. RELATOR Y SU INVERSO
            # ---------------------------------------------------------

            rules.append((s, ""))

            inverse = relation.inverse().word

            rules.append((inverse, ""))

            # ---------------------------------------------------------
            # 2. REGLAS DERIVADAS
            # ---------------------------------------------------------

            for i, char in enumerate(s):

                left = s[:i]
                right = s[i + 1:]

                # x^{-1} = right * left
                #
                # porque:
                #
                # left x right = e
                #
                # => x^{-1} = right left

                inverse_char = self.inverses_map[char]

                rhs = right + left

                # Regla:
                #
                # x^{-1} -> rhs
                #
                rules.append((inverse_char, rhs))

                # También podemos utilizar la ecuación
                #
                # x = (right left)^{-1}
                #
                # y obtener:
                #
                # x -> inverse(rhs)

                rhs_inverse = Word(
                    rhs,
                    _skip_validation=True
                ).inverse().word

                rules.append((char, rhs_inverse))

        # -------------------------------------------------------------
        # 3. ELIMINAR DUPLICADOS
        # -------------------------------------------------------------

        unique = []
        seen = set()

        for lhs, rhs in rules:

            if (lhs, rhs) not in seen:

                seen.add((lhs, rhs))
                unique.append((lhs, rhs))

        return unique

    # =============================================================
    # REDUCCIÓN MEDIANTE RELACIONES
    # =============================================================
    
    def _relation_reduce_once(self, word):
        """
        Aplica una regla de reescritura una sola vez.
        """

        s = word.word

        for lhs, rhs in self._relation_rules():

            if not lhs:
                continue

            position = s.find(lhs)

            if position == -1:
                continue

            left = s[:position]
            right = s[position + len(lhs):]

            new_word = Word(
                left + rhs + right,
                _skip_validation=True
            )

            new_word = self._free_reduce(new_word)

            # Solo aceptamos reglas que realmente reduzcan
            # la longitud de la palabra.
            if len(new_word) < len(word):

                return new_word, True

        return word, False

    def _reduce(self, word: Word) -> Word:
        """
        Reducción completa de una palabra.

        Primero realiza reducción libre y posteriormente aplica
        las relaciones hasta que no puede efectuar más reducciones.
        """

        word = self._free_reduce(word)

        while True:

            new_word, changed = self._relation_reduce_once(word)

            if not changed:
                return self._free_reduce(word)

            word = self._free_reduce(new_word)


    # =============================================================
    # OPERACIÓN DE GRUPO
    # =============================================================

    def operation(self, elem1, elem2) -> Word:

        w1 = self._to_word(elem1)
        w2 = self._to_word(elem2)

        return self._reduce(w1 * w2)


    def identity(self) -> Word:
        return Word("e")


    def inverse(self, elem) -> Word:

        w = self._to_word(elem)

        return self._reduce(~w)


    def __contains__(self, elem) -> bool:

        try:
            self._to_word(elem)
            return True

        except (ValueError, TypeError):
            return False


    # =============================================================
    # CONVERSIÓN A CAYLEY GROUP
    # =============================================================

    def toCayleyGroup(self, max_elements: int = 1000) -> CayleyGroup:
        """
        Construye una representación mediante tabla de Cayley
        explorando el grupo mediante BFS.

        La enumeración se realiza sobre palabras reducidas
        módulo las relaciones.
        """

        if self._cayley_cache is not None:
            return self._cayley_cache

        # Generadores e inversos
        all_gens = (
            [Word(g) for g in self.generators_names]
            +
            [Word(g.upper()) for g in self.generators_names]
        )

        # Identidad
        identity = self.identity()

        discovered = [identity]

        word_to_idx = {
            identity: 0
        }

        queue = deque([identity])

        # ---------------------------------------------------------
        # BFS
        # ---------------------------------------------------------

        while queue:

            current_word = queue.popleft()

            for gen in all_gens:

                next_word = self.operation(
                    current_word,
                    gen
                )

                if next_word not in word_to_idx:

                    if len(discovered) >= max_elements:
                        raise OverflowError(
                            __errorcolor__ +
                            f"Group could not be enumerated within "
                            f"the maximum limit of {max_elements} elements."
                        )

                    word_to_idx[next_word] = len(discovered)

                    discovered.append(next_word)

                    queue.append(next_word)

        # ---------------------------------------------------------
        # TABLA DE CAYLEY
        # ---------------------------------------------------------

        n = len(discovered)

        cayley_matrix = [
            [0] * n
            for _ in range(n)
        ]

        for i, w1 in enumerate(discovered):

            for j, w2 in enumerate(discovered):

                prod = self.operation(w1, w2)

                cayley_matrix[i][j] = word_to_idx[prod]

        # ---------------------------------------------------------
        # NOMBRES
        # ---------------------------------------------------------

        names = [
            str(w)
            for w in discovered
        ]

        self._cayley_cache = CayleyGroup(
            cayley_matrix,
            names,
            _skip_validation=True
        )

        return self._cayley_cache


    def toExplicitGroup(self) -> ExplicitGroup:
        return self.toCayleyGroup().toExplicitGroup()


    def order(self) -> int:
        return self.toCayleyGroup().order()


    # =============================================================
    # REPRESENTACIÓN
    # =============================================================

    def __str__(self):

        gens_str = ", ".join(
            self.generators_names
        )

        rels_str = ", ".join(
            str(r)
            for r in self.relations
        )

        return f"〈 {gens_str} | {rels_str} 〉"


    def __repr__(self):
        return self.__str__()
