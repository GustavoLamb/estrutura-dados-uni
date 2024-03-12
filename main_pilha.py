from domain import ArrayStack
from domain.abstract import ADTStack


def merge(p1: ArrayStack, p2: ArrayStack) -> ADTStack:
    pilha_merged: ArrayStack = ArrayStack()
    elemento_p1: object = p1.pop() if not p1.is_empty() else None
    elemento_p2: object = p1.pop() if not p2.is_empty() else None

    while not (elemento_p1 is None and elemento_p2 is None):

        if elemento_p2 is None or elemento_p1 < elemento_p2:
            pilha_merged.push(elemento_p1)
            elemento_p1 = None
        else:
            pilha_merged.push(elemento_p2)
            elemento_p2 = None

        elemento_p1 = p1.pop() if not p1.is_empty() and elemento_p1 is None else elemento_p1
        elemento_p2 = p2.pop() if not p2.is_empty() and elemento_p2 is None else elemento_p2

    return pilha_merged


def main() -> None:
    pilha1: ArrayStack = ArrayStack()
    pilha2: ArrayStack = ArrayStack()
    for elemento in [6, 4, 3, 1]:
        pilha1.push(elemento)

    for elemento in [5, 2]:
        pilha2.push(elemento)

    nova_pilha: ADTStack = merge(pilha1, pilha2)

    print('Pilha Merged:', nova_pilha)


if __name__ == '__main__':
    main()
