"""Merge Sort (CLRS) implementation (in-place merge using sentinels).

Implements the pseudocode MERGE(A,p,q,r) and MERGE-SORT(A,p,r) from CLRS.
Provides `sort(A, debug=False)` as public API (returns a sorted copy).
"""
from typing import List


def merge(A: List[int], p: int, q: int, r: int, debug: bool = False) -> None:
    """Merge subarrays A[p..q] and A[q+1..r] in-place using sentinel values.

    Indices are 0-based. This follows CLRS pseudocode where p, q, r are indices.
    """
    INF = float('inf')
    n1 = q - p + 1
    n2 = r - q

    # L[0..n1] with sentinel at L[n1]
    L = [0] * (n1 + 1)
    # R[0..n2] with sentinel at R[n2]
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]

    L[n1] = INF
    R[n2] = INF

    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    if debug:
        print(f"merge p={p} q={q} r={r} -> {A[p:r+1]}")


def mergesort(A: List[int], p: int, r: int, debug: bool = False) -> None:
    """Recursively sort A[p..r] in-place using merge sort (CLRS)."""
    if p < r:
        q = (p + r) // 2
        mergesort(A, p, q, debug=debug)
        mergesort(A, q + 1, r, debug=debug)
        merge(A, p, q, r, debug=debug)


def sort(A: List[int], debug: bool = False) -> List[int]:
    """Public API: returns a sorted copy of `A` using CLRS merge sort (in-place on copy)."""
    if not A:
        return []
    B = A.copy()
    mergesort(B, 0, len(B) - 1, debug=debug)
    return B
