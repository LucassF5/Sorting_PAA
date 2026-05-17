"""Heapsort (CLRS) implementation (in-place).

Implements MAX-HEAPIFY, BUILD-MAX-HEAP, and HEAPSORT following CLRS structure.
Provides `sort(A, debug=False)` as public API.
"""
from typing import List


def max_heapify(A: List[int], i: int, heap_size: int, debug: bool = False) -> None:
    """Maintain max-heap property for subtree rooted at index i (0-based).

    heap_size: number of elements in the heap (A[0..heap_size-1])
    Assumes left and right subtrees are already max-heaps.
    """
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < heap_size and A[left] > A[largest]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        if debug:
            print(f"heapify swap i={i} with largest={largest}")
        max_heapify(A, largest, heap_size, debug=debug)


def build_max_heap(A: List[int], debug: bool = False) -> None:
    """Build max-heap from unordered array A (in-place)."""
    heap_size = len(A)
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(A, i, heap_size, debug=debug)


def heapsort(A: List[int], debug: bool = False) -> None:
    """Sort array A in-place using heapsort (CLRS)."""
    build_max_heap(A, debug=debug)
    heap_size = len(A)
    for i in range(heap_size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        if debug:
            print(f"extract max: swap A[0] with A[{i}]")
        heap_size -= 1
        max_heapify(A, 0, heap_size, debug=debug)


def sort(A: List[int], debug: bool = False) -> List[int]:
    """Public API: returns a sorted copy of `A` using heapsort."""
    if not A:
        return []
    B = A.copy()
    heapsort(B, debug=debug)
    return B
