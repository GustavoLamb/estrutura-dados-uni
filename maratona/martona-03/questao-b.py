vertices, arestas = input().split(" ")

dicio = {f'{vertice}': [] for vertice in range(1, int(vertices) + 1)}

if int(arestas) != 0:
    for i in range(int(arestas)):
        vertice_1, vertice_2 = input().split()
        dicio[vertice_1] += [vertice_2]

    juiz = -1

    for key in dicio.keys():
        if len(dicio[key]) == 0:
            juiz = key
            break

    for key in dicio.keys():
        if juiz == key:
            continue
        if juiz not in dicio[key]:
            juiz = -1
            break

    print(juiz)
else:
    print(-1)
