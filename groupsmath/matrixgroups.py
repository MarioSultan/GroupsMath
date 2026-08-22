from .core import *
from .core import __errorcolor__

#################### MATRIX GROUPS ####################

class MatrixGroup(Group):

    def __init__(self, n: int, field="R", condition=None, p=None):

        if type(field)==int:
            p = field
            field = "F_p"

        if field not in ("Z","R","C","F_p"):
            raise ValueError (__errorcolor__+"The field attribute must be 'Z', 'R', 'C', or 'F_p'")

        if field=="F_p":
            if p is None:
                raise ValueError(__errorcolor__+"Parameter 'p' must be provided for finite field 'F_p'.")
            elif not _is_prime(p):
                raise ValueError (__errorcolor__+"The integer p has to be a prime number.")
        else:
            p = None

        self.n = n
        self.field = field
        self.p = p
        self.condition = condition

    #–> DUNDERS

    def __contains__(self, matrix) -> bool:

        M = np.array(matrix)

        if M.shape != (self.n, self.n):
            return False

        if self.field == "F_p":
            if not np.issubdtype(M.dtype, np.integer) or np.any(M < 0) or np.any(M >= self.p):
                return False

        det = self._determinant(M)
        if det == 0:
            return False

        if not _check_field(M, self.field, self.p):
            return False

        if self.condition is not None:
            return bool(self.condition(M))

        return True

    #–> GROUP METHODS

    def operation(self, A, B):
        A, B = np.array(A), np.array(B)
        if self.field == "F_p":
            return (A @ B) % self.p
        return A @ B

    def identity(self):
        return np.eye(self.n, dtype=int if self.field == "F_p" else float)

    def inverse(self, A):
        A = np.array(A)
        if self.field == "F_p":
            det = int(np.round(np.linalg.det(A))) % self.p
            det_inv = pow(det, -1, self.p)
            adj = np.round(np.linalg.inv(A) * np.linalg.det(A)).astype(int)
            return (det_inv * adj) % self.p
        return np.linalg.inv(A)

    def _determinant(self, A):
        if self.field == "F_p":
            return int(np.round(np.linalg.det(A))) % self.p
        return np.linalg.det(A)

    #–> TRANSFORMING METHODS 

    def _cayley(self):

        if not self._is_finite():
            raise TypeError(__errorcolor__+"Cannot generate Cayley table for an infinite group.")
        
        elems = list(self.elements())
        return [[self.operation(a, b) for b in elems] for a in elems]

    def toCayleyGroup(self):
        if not self._is_finite():
            raise ValueError(__errorcolor__+"Infinite matrix groups cannot be converted to CayleyGroup.")

        raw_elems = list(self.elements())
        idx = {elem: i for i, elem in enumerate(raw_elems)}

        # Formatear nombres de manera visualmente limpia para los ejes y celdas
        clean_names = [_matrix_to_str(m) for m in raw_elems]

        cayley_matrix = []
        for a in raw_elems:
            row = []
            for b in raw_elems:
                res = self.operation(a, b)
                res_key = tuple(tuple(int(x) for x in r) for r in res) if isinstance(res, np.ndarray) else res
                row.append(idx[res_key])
            cayley_matrix.append(row)

        return CayleyGroup(cayley_matrix, clean_names, _skip_validation=True)

    def toExplicitGroup(self):
        if not self._is_finite():
            raise ValueError(__errorcolor__+"Infinite groups cannot be converted to ExplicitGroup.")
        elems = list(self.elements())
        return ExplicitGroup(elems, self.operation, _skip_validation=True)
    
    #–> GROUP METHODS 

    def _is_finite(self) -> bool:
        return self.field == "F_p"

    def order(self):                        # REVISAR EL _IS_FINITE
        if not self._is_finite():
            return float("inf")
        return sum(1 for _ in self.elements())

    def elements(self):
        # 'yield' generator for finite field elements.
        if not self._is_finite():
            raise TypeError(__errorcolor__+"Cannot enumerate elements of an infinite group.")

        for entries in product(range(self.p), repeat=self.n * self.n):
            M = np.array(entries).reshape((self.n, self.n))
            if M in self:
                yield tuple(tuple(row) for row in M)

    def cayley_table(self, title="", colormap=rainbow, names=None):
        return self.toCayleyGroup().cayley_table(title=title, colormap=colormap, names=names, math_mode=False)

class MatrixSubgroup(MatrixGroup, Subgroup):
    def __init__(self, subgroup: MatrixGroup, group: MatrixGroup):
        if not isinstance(subgroup, MatrixGroup) or not isinstance(group, MatrixGroup):
            raise ValueError(__errorcolor__+"Both arguments must be instances of MatrixGroup")

        if subgroup.n != group.n or subgroup.field != group.field or subgroup.p != group.p:
            raise ValueError(__errorcolor__+"Subgroup matrix configuration does not match the parent group")

        self.subgroup = subgroup
        self.group = group
        super().__init__(subgroup.n, field=subgroup.field, condition=subgroup.condition, p=subgroup.p)


#################### HIDDEN COMMANDS ####################

def _is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def _check_field(M, field, p=None):

    if field == "C":
        return True

    if field == "R":
        if np.iscomplexobj(M) and np.any(np.imag(M) != 0):
            return False
        return True

    if field == "Z":
        if np.iscomplexobj(M) and np.any(np.imag(M) != 0):
            return False
        return np.all(np.equal(np.mod(M, 1), 0))

    if field in ("F_n", "F_p", "F"):
        if p is None:
            raise ValueError(__errorcolor__+"For finite fields F_n, parameter 'p' must be specified.")
        if np.iscomplexobj(M) and np.any(np.imag(M) != 0):
            return False
        return np.all((M >= 0) & (M < p) & np.equal(np.mod(M, 1), 0))

    return True

def _matrix_to_str(M):
    clean_m = [[int(x) if isinstance(x, (int, np.integer)) else x for x in row] for row in M]
    rows = ["[" + "  ".join(str(x) for x in row) + "]" for row in clean_m]
    return "\n".join(rows)


#################### GENERATORS ####################

def GL(n, field="R", p=None):
    """General Linear Group GL_n(F)"""
    return MatrixGroup(n, field=field, p=p)

def SL(n, field="R", p=None):
    """Special Linear Group SL_n(F)"""
    if type(field)==int:
        p = field
        field = "F_p"
    if field == "F_p":
        cond = lambda M: (int(np.round(np.linalg.det(M))) % p) == 1
    else:
        cond = lambda M: np.isclose(np.linalg.det(M), 1.0)
    return MatrixGroup(n, field=field, condition=cond, p=p)

def O(n, field="R"):
    """Orthogonal Group O_n(R)"""
    if field=="F_p" or type(field)==int:
        raise ValueError (__errorcolor__+"GroupsMath cannot generate an orthogonal group in a finite field.")
    if n%2==0:
        raise ValueError (__errorcolor__+"Cannot generate an orthogonal group without Witt index in even dimension.")
    cond = lambda M: np.allclose(M.T @ M, np.eye(n))
    return MatrixGroup(n, field=field, condition=cond)

def SO(n, field="R"):
    """Special Orthogonal Group SO_n(R)"""
    if field=="F_p" or type(field)==int:
            raise ValueError (__errorcolor__+"GroupsMath cannot generate an orthogonal group in a finite field.")
    if n%2==0:
        raise ValueError (__errorcolor__+"Cannot generate an orthogonal group without Witt index in even dimension.")
    cond = lambda M: np.allclose(M.T @ M, np.eye(n)) and np.isclose(np.linalg.det(M), 1.0)
    return MatrixGroup(n, field=field, condition=cond)

def U(n):
    """
    Unitary Group U(n).
    Condition: A^† @ A = I (where A^† is the conjugate transpose).
    """
    cond = lambda M: np.allclose(M.conj().T @ M, np.eye(n))
    return MatrixGroup(n, field="C", condition=cond)

def SU(n):
    """
    Special Unitary Group SU(n).
    Condition: A^† @ A = I and det(A) = 1.
    """
    cond = lambda M: np.allclose(M.conj().T @ M, np.eye(n)) and np.isclose(np.linalg.det(M), 1.0 + 0j)
    return MatrixGroup(n, field="C", condition=cond)

def Sp(n):
    """
    Symplectic Group Sp(2n, R) over real matrices.
    Condition: M^T @ J @ M = J, where J = [[0, I], [-I, 0]].
    Note: The matrix dimension must be even (2n).
    """
    if n % 2 != 0:
        raise ValueError(__errorcolor__+"Symplectic group dimension must be an even integer.")
    
    k = n // 2
    I_k = np.eye(k)
    J = np.block([[np.zeros((k, k)), I_k], 
                  [-I_k, np.zeros((k, k))]])
    
    cond = lambda M: np.allclose(M.T @ J @ M, J)
    return MatrixGroup(n, field="R", condition=cond)

