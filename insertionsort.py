"""Insertion Sort (CLRS) implementation.

Provides `insertionSort(A, debug=False)` as public API.
"""
from typing import List


def insertionSort(A: List[int], debug: bool = False) -> List[int]:
    """Sort array A in-place using insertion sort (CLRS).
    
    Args:
        A: List of integers to sort
        debug: If True, print each shift and insert operation
    
    Returns:
        The sorted array A (sorted in-place)
    """
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
            if debug:
                print(f"shift: j={j} i={i+1} -> {A}")
        A[i+1] = key
        if debug:
            print(f"insert: j={j} pos={i+1} -> {A}")
    return A


# Alias para manter compatibilidade com runner.py
def sort(A: List[int], debug: bool = False) -> List[int]:
    """Public API: returns a sorted copy of `A` using insertion sort."""
    if not A:
        return []
    B = A.copy()
    insertionSort(B, debug=debug)
    return B