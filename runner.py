"""Runner para comparar tempos de algoritmos de ordenação.

Uso:
  python runner.py --algorithm insertion --type random --size 50 --repeat 3

Opções principais:
- `--algorithm`: 'insertion' ou 'python' (pode ser o nome de um módulo que exporta `sort(A, debug=False)`)
- `--type`: 'ordered' | 'reversed' | 'random'
- `--size`: um valor presente em `arrays.sizes`
- `--repeat`: número de execuções para média
- `--debug`: passar debug para o algoritmo (quando suportado)
- `--force`: força execução mesmo para tamanhos grandes
"""
import argparse
import time
import importlib
from arrays import get_array, sizes


def load_algorithm(name):
    if name == 'insertion' or name == 'insertionsort':
        import insertionsort as mod
        if hasattr(mod, 'sort'):
            return mod.sort
        fn = getattr(mod, 'insertionSort', None)
        if fn is None:
            raise ImportError('insertionsort.py não exporta sort ou insertionSort')
        return fn
    if name == 'python':
        return lambda A, debug=False: sorted(A)

    # tentar importar módulo do mesmo nome
    mod = importlib.import_module(name)
    if hasattr(mod, 'sort'):
        return mod.sort
    # tentativas de nomes alternativos
    for alt in ('sort_array', 'quicksort'):
        if hasattr(mod, alt):
            return getattr(mod, alt)
    raise ImportError(f"Nenhuma função de ordenação encontrada no módulo '{name}'")


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--algorithm', default='python', help="Nome do algoritmo (ex.: insertion, python, heapsort, quicksort, merge_sort)")
    p.add_argument('--type', choices=['ordered', 'reversed', 'random'], default='random')
    p.add_argument('--size', type=int, choices=sizes, default=100)
    p.add_argument('--repeat', type=int, default=1)
    p.add_argument('--debug', action='store_true')
    p.add_argument('--show-input', action='store_true', help='Mostrar array de entrada antes da ordenação')
    p.add_argument('--force', action='store_true', help='Ignorar aviso para tamanhos grandes')
    args = p.parse_args()

    if args.size > 5000 and not args.force:
        print(f"Aviso: tamanho {args.size} pode ser muito lento para algoritmos O(n^2). Use --force para continuar.")
        return

    sort_fn = load_algorithm(args.algorithm)

    times = []
    correct = True
    input_shown = False
    
    for i in range(args.repeat):
        A = get_array(args.type, args.size)
        
        # Mostra o array de entrada apenas na primeira execução se solicitado
        if args.show_input and not input_shown:
            if args.size <= 100:
                print(f"Input ({args.type}, {args.size}):", A)
            else:
                print(f"Input ({args.type}, {args.size}): length={len(A)}, first 10: {A[:10]}, last 10: {A[-10:]}")
            input_shown = True
        
        work = A.copy()
        start = time.perf_counter()
        try:
            res = sort_fn(work, debug=args.debug)
        except TypeError:
            # função sem parâmetro debug
            res = sort_fn(work)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

        # validação simples
        expected = sorted(A)
        # res pode ser None se a função ordenar in-place; então comparar `work`
        out = res if res is not None else work
        if out != expected:
            correct = False
            print(f"Run {i+1}: saída incorreta para {args.algorithm} (size={args.size})")
        else:
            print(f"Run {i+1}: OK — {elapsed:.6f}s")

    avg = sum(times) / len(times)
    print(f"\nAlgorithm: {args.algorithm} | type: {args.type} | size: {args.size}")
    print(f"Runs: {len(times)} | Avg time: {avg:.6f}s")


if __name__ == '__main__':
    main()
