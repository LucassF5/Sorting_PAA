"""CLI genérica para executar algoritmos de ordenação com array customizado.

Uso:
  python sort_cli.py --algorithm merge_sort --type reversed --size 10 --show-input --debug
  python sort_cli.py --algorithm quicksort --type ordered --size 100
  python sort_cli.py --algorithm heapsort --type random --size 50
  python sort_cli.py --algorithm insertionsort --type random --size 10
"""
import argparse
import importlib
from arrays import get_array, sizes


def load_algorithm(name):
    """Carrega a função sort de um módulo de algoritmo.
    
    Tenta importar o módulo pelo nome e procura por 'sort' ou 'insertionSort'.
    """
    try:
        # Caso especial para insertionsort que usa insertionSort em vez de sort
        if name == 'insertionsort':
            mod = importlib.import_module('insertionsort')
            if hasattr(mod, 'insertionSort'):
                return getattr(mod, 'insertionSort')
        
        # Tenta importar pelo nome do módulo
        mod = importlib.import_module(name)
        if hasattr(mod, 'sort'):
            return getattr(mod, 'sort')
        
        raise ImportError(f"Módulo '{name}' não exporta função 'sort'")
    except ModuleNotFoundError:
        raise ImportError(f"Módulo '{name}' não encontrado")


def main():
    p = argparse.ArgumentParser(
        description="Executar algoritmo de ordenação com array customizado"
    )
    p.add_argument(
        '--algorithm',
        required=True,
        help="Nome do módulo do algoritmo (merge_sort, quicksort, heapsort, insertionsort)"
    )
    p.add_argument(
        '--type',
        choices=['ordered', 'reversed', 'random'],
        default='random',
        help="Tipo do array"
    )
    p.add_argument(
        '--size',
        type=int,
        choices=sizes,
        default=100,
        help="Tamanho do array"
    )
    p.add_argument(
        '--show-input',
        action='store_true',
        help="Mostrar array de entrada antes da ordenação"
    )
    p.add_argument(
        '--debug',
        action='store_true',
        help="Ativar saída de debug do algoritmo"
    )
    args = p.parse_args()

    # Carregar algoritmo
    try:
        sort_fn = load_algorithm(args.algorithm)
    except ImportError as e:
        print(f"Erro: {e}")
        return

    # Gerar array
    A = get_array(args.type, args.size)

    # Mostrar entrada se solicitado
    if args.show_input:
        if args.size <= 100:
            print(f"Input ({args.type}, {args.size}):", A)
        else:
            print(f"Input ({args.type}, {args.size}): length={len(A)}, first 10: {A[:10]}, last 10: {A[-10:]}")

    # Executar algoritmo
    A_copy = A.copy()
    try:
        result = sort_fn(A_copy, debug=args.debug)
    except TypeError:
        # Função sem parâmetro debug
        result = sort_fn(A_copy)

    # Mostrar resultado
    if args.size <= 100:
        print(f"Sorted ({args.type}, {args.size}):", result if result is not None else A_copy)
    else:
        output = result if result is not None else A_copy
        print(f"Sorted ({args.type}, {args.size}): length={len(output)}")

    # Validação simples
    expected = sorted(A)
    output = result if result is not None else A_copy
    # if output == expected:
    #     print("✓ Resultado correto")
    # else:
    #     print("✗ Resultado incorreto")


if __name__ == '__main__':
    main()
