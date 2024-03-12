from domain import LinkedStack


def main() -> None:
    pilha: LinkedStack = LinkedStack()

    for i in range(0, 10):
        pilha.push(i)

    pilha.pop()
    print(pilha.peek())
    print(len(pilha))
    print(pilha)


if __name__ == '__main__':
    main()
