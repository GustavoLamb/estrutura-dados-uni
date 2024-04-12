import math

array = [int(numero) for numero in input().split()]
altura = math.floor(math.log2(len(array)))
simetrico = True

for nivel in range(altura + 1):
    if not simetrico:
        break

    numero_node_nivel = 2 ** nivel
    inf = numero_node_nivel - 1
    sup = numero_node_nivel
    for j, k in enumerate(range(inf, inf + sup//2)):
        last = inf + sup - 1 - j
        if array[k] != array[last]:
            simetrico = False
            break

resposta = 'OK' if simetrico else 'NAO'
print(resposta)
