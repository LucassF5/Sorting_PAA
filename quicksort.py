"""Quicksort (CLRS) implementation (in-place).

Implements PARTITION and QUICKSORT following CLRS structure.
Provides `sort(A, debug=False)` as public API.
"""
from typing import List
import random


def partition(A: List[int], p: int, r: int, debug: bool = False) -> int:
    """Partition array A[p..r] using random pivot.

    Randomly selects a pivot to avoid worst-case O(n²) on ordered arrays.
    Returns the index q where A[p..q-1] <= A[q] and A[q+1..r] > A[q].
    """
    # Random pivot selection to avoid O(n²) worst case
    pivot_idx = random.randint(p, r)
    A[pivot_idx], A[r] = A[r], A[pivot_idx]
    
    x = A[r]  # pivot
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            if debug:
                print(f"partition swap A[{i}] with A[{j}], pivot={x}")
    A[i + 1], A[r] = A[r], A[i + 1]
    if debug:
        print(f"partition pivot A[{i+1}]={x}, A[p:{r+1}]={A[p:r+1]}")
    return i + 1


def quicksort(A: List[int], p: int, r: int, debug: bool = False) -> None:
    """Recursively sort A[p..r] in-place using quicksort with random pivot."""
    if p < r:
        q = partition(A, p, r, debug=debug)
        quicksort(A, p, q - 1, debug=debug)
        quicksort(A, q + 1, r, debug=debug)


def sort(A: List[int], debug: bool = False) -> List[int]:
    """Public API: returns a sorted copy of `A` using quicksort."""
    if not A:
        return []
    B = A.copy()
    quicksort(B, 0, len(B) - 1, debug=debug)
    return B
