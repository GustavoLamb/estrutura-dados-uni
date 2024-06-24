vertices, arestas = input().split(" ")

dicio = {f'{vertice}': 0 for vertice in range(1, int(vertices) + 1)}

for i in range(int(arestas)):
    vertice_1, vertice_2 = input().split()
    dicio[vertice_1] += 1
    dicio[vertice_2] += 1

vertice = '1'

for key in dicio.keys():
    if dicio[vertice] < dicio[key]:
        vertice = key

print(vertice)




