"""Gerador de arrays para testes de ordenação.

Fornece três tipos de arrays: 'ordered', 'reversed', 'random'
e a lista de tamanhos suportados em `sizes`.
"""
import random

# Tamanhos solicitados
# Adicionamos tamanhos menores para testes rápidos
sizes = [10, 50, 100, 500, 1000, 5000, 30000, 50000, 100000, 150000, 200000]

def get_array(kind: str, size: int):
    """Retorna um novo array do `kind` e `size` pedidos.

    kind: 'ordered' | 'reversed' | 'random'
    size: inteiro presente em `sizes`
    """
    if size not in sizes:
        raise ValueError(f"Size {size} not supported. Use one of: {sizes}")

    if kind in ("ordered", "asc", "ascending"):
        return list(range(size))
    if kind in ("reversed", "desc", "descending"):
        return list(range(size - 1, -1, -1))
    if kind in ("random", "rand", "shuffle"):
        lst = list(range(size))
        random.shuffle(lst)
        return lst

    raise ValueError(f"Unknown kind: {kind}. Use 'ordered', 'reversed' or 'random'.")


if __name__ == "__main__":
    # Exemplo rápido de uso
    for k in ("ordered", "reversed", "random"):
        print(k, get_array(k, sizes[0])[:10])
