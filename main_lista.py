from domain import ArrayQueue


def main() -> None:
    fila: ArrayQueue = ArrayQueue()
    for i in range(1, 10):
        fila.enqueue(i)


if __name__ == '__main__':
    main()
