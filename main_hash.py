class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome: str = nome
        self._idade: int = idade

    def __hash__(self):
        return hash(self._idade)


def main() -> None:
    pessoa = Pessoa("Fulano", 42)

    print("Hash de um número inteiro:", hash(4))
    print("Hash de uma string:", hash("Batata"))
    print("Hash do meu objeto:", hash(pessoa))


if __name__ == '__main__':
    main()
