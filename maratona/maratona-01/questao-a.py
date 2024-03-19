class Nodo:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.left = 2 * chave + 1
        self.right = 2 * chave + 2


def in_order_print(arvore_array, raiz):
    def in_order_print(arvore_array, nodo_atual):
        if nodo_atual.left < len(arvore_array):
            nodo_esquerdo = Nodo(nodo_atual.left, arvore_array[nodo_atual.left])
            in_order_print(arvore_array, nodo_esquerdo)
        print(nodo_atual.valor, end=' ')
        if nodo_atual.right < len(arvore_array):
            nodo_direito = Nodo(nodo_atual.right, arvore_array[nodo_atual.right])
            in_order_print(arvore_array, nodo_direito)

    in_order_print(arvore_array, raiz)


entrada = [numero for numero in input().split(' ')]
root = Nodo(0, entrada[0])
in_order_print(entrada, root)
