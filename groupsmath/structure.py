from .core import *
from .core import __errorcolor__

''' Revisar, que aparecen errores '''

#################### WARNINGS ####################

print("\033[33m[!] WARNING: The library 'groupsmath.structure' is under development and it might produce errors.\033[0m")


#################### STRUCTURE DESCRIPTION ####################

def structure_description(G):
    """
    Caracteriza algebraicamente la estructura de G sin usar tablas predefinidas.
    Retorna una cadena con la notación de grupos (ej: 'C2 x C2', 'C3 : C4', 'S3').
    """
    n = G.order()
    
    # 1. CASO TRIVIAL
    if n == 1:
        return "I"

    # 2. CASO ABELIANO (Teorema Fundamental)
    if G.is_abelian():
        return _decompose_abelian(G)

    # 3. CASO SIMPLE
    if G.is_simple():
        return _describe_simple(G)

    # 4. DESCOMPOSICIÓN POR SUBGRUPOS NORMALES
    normals = G.normal_subgroups()
    # Filtramos para quedarnos solo con subgrupos normales propios no triviales
    proper_normals = [H for H in normals if 1 < H.order() < n]

    # Intentar factorizar usando subgrupos normales (de mayor a menor tamaño)
    proper_normals.sort(key=lambda h: h.order(), reverse=True)

    for N in proper_normals:
        # Buscar un complemento H tal que N * H = G y N \cap H = {e}
        complement = _find_complement(G, N)
        
        if complement is not None:
            name_N = structure_description(N)
            name_H = structure_description(complement)
            
            # Si el complemento H también es normal -> Producto Directo (N x H)
            if complement.is_normal():
                return f"{name_N} x {name_H}"
            # Si H no es normal -> Producto Semidirecto (N : H)
            else:
                return f"{name_N} : {name_H}"

    # 5. SI NO HAY COMPLEMENTO (Extensión no escindida N.H)
    # Tomamos el mayor subgrupo normal N y el cociente G/N
    N = proper_normals[0]
    Q = G.quotient(N)
    return f"{structure_description(N)}.{structure_description(Q)}"


#################### HIDDEN FUNCTIONS ####################

def _decompose_abelian(G):
    """Descompone un grupo abeliano en factores cíclicos C_d1 x C_d2 ..."""
    n = G.order()
    orders = G.element_orders()
    
    # Si el elemento de orden máximo es n, es cíclico puro
    if max(orders) == n:
        return f"C{n}"

    # Descomposición en factores de invariantes
    # Para grupos abelianos pequeños, extrae exponentes del grupo
    factors = []
    temp_n = n
    # Extraer factores cíclicos iterativamente sobre los elementos
    curr_group = G
    while temp_n > 1:
        m = max(curr_group.element_orders())
        factors.append(f"C{m}")
        temp_n //= m
        if temp_n == 1:
            break
        # Reducción aproximada de la componente abeliana
        break # Para extender con divisores elementales p-primarios completos

    if len(factors) == 1 and temp_n > 1:
        # Fallback de seguridad en caso de multiplicidad
        return f"C{max(orders)} x C{n // max(orders)}"
        
    return " x ".join(sorted(factors, reverse=True))

def _find_complement(G, N):
    """Busca un subgrupo H <= G tal que N & H = {e} y |N| * |H| = |G|."""
    target_order = G.order() // N.order()
    
    for H in G.subgroups():
        if H.order() == target_order:
            # Comprobar intersección trivial N & H = {e}
            intersection = set(N.elements).intersection(set(H.elements))
            if len(intersection) == 1:
                return H
    return None

def _describe_simple(G):
    """Identifica la familia del grupo simple."""
    n = G.order()
    if G.is_abelian():
        return f"C{n}"  # C_p con p primo
    
    # Clasificación básica de simples no abelianos por orden
    if n == 60:
        return "A5"
    if n == 168:
        return "PSL(2,7)"
    if n == 360:
        return "A6"
    return f"SimpleGroup({n})"

