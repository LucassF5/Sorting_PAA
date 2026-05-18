"""Bubble Sort implementation.
"""
from typing import List


def bublesort(A: List[int], debug: bool = False) -> None:
    """Sort array A in-place using bubble sort.
    
    Args:
        A: List of integers to sort
        debug: If True, print each swap operation
    """
    for i in range(len(A)):
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                if debug:
                    print(f"swap: j={j} -> {A}")


def sort(A: List[int], debug: bool = False) -> List[int]:
    """Returns a sorted copy of `A` using bubble sort."""
    if not A:
        return []
    B = A.copy()
    bublesort(B, debug=debug)
    return B