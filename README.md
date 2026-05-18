# Sorting_PAA — Instruções de uso

Este repositório contém implementações e utilitários para testes e comparação de algoritmos de ordenação.

Arquivos principais

**Algoritmos** (contêm apenas a lógica de ordenação):

- [bublesort.py](bublesort.py): Bubble Sort — O(n²)
- [insertionsort.py](insertionsort.py): Insertion Sort (CLRS) — O(n²)
- [mergesort.py](mergesort.py): Merge Sort (CLRS) — O(n log n) em todos os casos
- [heapsort.py](heapsort.py): Heapsort (CLRS) — O(n log n) in-place
- [quicksort.py](quicksort.py): Quicksort (CLRS) — O(n log n) average, O(n²) worst-case

**Utilitários**:

- [arrays.py](arrays.py): gerador de arrays por tipo e tamanho (tipos: `ordered`, `reversed`, `random`)
- [sort_cli.py](sort_cli.py): CLI genérica para executar qualquer algoritmo com parâmetros customizados
- [runner.py](runner.py): utilitário para comparar tempos e validar resultados entre múltiplas execuções

Tamanhos suportados (valores em `arrays.sizes`):

- 10
- 50
- 100
- 500
- 1_000
- 5_000
- 30_000
- 50_000
- 100_000
- 150_000
- 200_000

Uso básico

Executar um algoritmo com o `sort_cli.py` escolhendo tipo, tamanho e opções:

```bash
python sort_cli.py --algorithm bublesort --type random --size 100
python sort_cli.py --algorithm mergesort --type random --size 100 --show-input --debug
python sort_cli.py --algorithm quicksort --type reversed --size 1000
python sort_cli.py --algorithm heapsort --type ordered --size 50
python sort_cli.py --algorithm insertionsort --type random --size 10
```

Opções disponíveis:

- `--algorithm`: `bublesort` | `mergesort` | `quicksort` | `heapsort` | `insertionsort`
- `--type`: `ordered` | `reversed` | `random`
- `--size`: um dos tamanhos listados abaixo
- `--show-input`: mostra o array de entrada antes de ordenar
- `--debug`: imprime cada operação do algoritmo (recomendado apenas para tamanhos pequenos)

Runner: comparar algoritmos e medir tempos

```bash
python runner.py --algorithm bublesort --type random --size 50 --repeat 3
python runner.py --algorithm insertion --type random --size 50 --repeat 3
python runner.py --algorithm mergesort --type random --size 1000 --repeat 3
python runner.py --algorithm heapsort --type random --size 5000 --repeat 3 --force
python runner.py --algorithm quicksort --type random --size 5000 --repeat 3 --force
```

Opções:

- `--algorithm`: `insertion`, `mergesort`, `heapsort`, `quicksort` ou qualquer módulo que exporte `sort(A, debug=False)`
- `--repeat`: número de execuções para calcular média de tempo
- `--show-input`: mostra o array de entrada (apenas na primeira execução)
- `--force`: força execução mesmo para tamanhos grandes (padrão: avisa se tamanho > 5000)

Algoritmos implementados (todos seguem CLRS)

1. **Bubble Sort** — O(n²) | simples, para fins educacionais
2. **Insertion Sort** — O(n²) | melhor para pequenos vetores ou semi-ordenados
3. **Merge Sort** — O(n log n) garantido | estável, divide-e-conquista
4. **Heapsort** — O(n log n) | in-place, sem espaço extra
5. **Quicksort** — O(n log n) average / O(n²) worst | in-place, mais rápido na prática

Adicionar novos algoritmos

1. Crie um módulo, ex.: `shellsort.py`, exporte a função `sort(A, debug=False)` que retorna o array ordenado (ou ordena in-place)
2. Execute com `sort_cli.py`:
   ```bash
   python sort_cli.py --algorithm shellsort --type random --size 100
   ```
3. Ou use com `runner.py`:
   ```bash
   python runner.py --algorithm shellsort --type random --size 1000 --repeat 3
   ```

Boas práticas

- Sempre use `A.copy()` antes de ordenar para não alterar a fonte.
- Para visualização de passos, use `yield A.copy()` (generator) ou acumule `snaps.append(A.copy())`.
- Use `logging` em vez de `print` em experimentos automatizados para controlar o verboso.
- Mantenha a função `sort(A, debug=False)` como interface pública em cada algoritmo para compatibilidade com `sort_cli.py` e `runner.py`.
