"""Teste de contador de comparações para Fastsort."""
from fastsort import sort_with_comparisons
from arrays import sizes

print("Fastsort - Contador de Comparações\n")
print("Tamanho | Comparações | Algoritmo")
print("-" * 45)

for size in sizes:
    A = list(range(size))
    result, comps = sort_with_comparisons(A)
    algo = "Quick Sort" if size <= 5000 else "Merge Sort"
    print(f"{size:>7} | {comps:>11} | {algo}")
