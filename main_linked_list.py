from domain import SinglyLinkedList


def main() -> None:
    lista: SinglyLinkedList = SinglyLinkedList()

    for i in range(0, 10):
        lista.insert_last(i)

    metada_inicial = lista.split(9)

    print("Metade inicial:", metada_inicial)
    print("Metade final:", lista)


if __name__ == '__main__':
    main()
