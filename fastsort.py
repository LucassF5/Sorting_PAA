"""Hybrid Sort: Quick Sort + Merge Sort.

Usa Quick Sort para vetores pequenos e Merge Sort para vetores grandes,
evitando o pior caso O(n²) do Quick Sort em entradas grandes.
"""
from typing import List
import quicksort
import mergesort

THRESHOLD = 5000


def sort(A: List[int], debug: bool = False) -> List[int]:
    if not A:
        return []
    if len(A) <= THRESHOLD:
        return quicksort.sort(A, debug=debug)
    else:
        return mergesort.sort(A, debug=debug)
