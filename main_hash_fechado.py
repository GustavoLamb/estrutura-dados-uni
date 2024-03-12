from domain import ClosedHashing
from exception import OverflowError


def main() -> None:
    tabela = ClosedHashing()

    tabela.insert(19645, "Gustavo")
    tabela.insert(19321, "Gregory")
    tabela.insert(19642, "Milena")
    tabela.insert(19610, "Fulano")
    tabela.insert(19521, "Fulana")

    print(tabela,  f'Tamanho = {tabela.size()}', f'Vazia = {tabela.is_empty()}')

    ra: int = int(input("\nInforme um RA para excluir da tabela: "))

    print(f"Aluno RA {ra}: {tabela.search(ra)}. Será excluido")

    if tabela.delete(ra):
        print("Aluno excluido com sucesso!!\n")
    else:
        print("Aluno não existe na tabela!\n")

    print(tabela,  f'Tamanho = {tabela.size()}', f'Vazia = {tabela.is_empty()}')

    input("\nPressione ENTER para continuar e limpar a tabela\n")

    tabela.clear()
    print(tabela, f'Tamanho = {tabela.size()}', f'Vazia = {tabela.is_empty()}')


def test_overflow() -> None:
    tabela = ClosedHashing(3)

    try:
        tabela.insert(19645, "Gustavo")
        tabela.insert(19321, "Gregory")
        tabela.insert(19642, "Milena")
        tabela.insert(19610, "Fulano")
        tabela.insert(19521, "Fulana")
    except OverflowError as exception:
        print(exception)


if __name__ == '__main__':
    main()

