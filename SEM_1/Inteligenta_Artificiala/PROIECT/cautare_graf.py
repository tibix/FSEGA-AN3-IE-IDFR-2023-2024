from numpy import Inf

graf = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)],
}


def dijkstra(graf, start, scop):
    distante = {}
    parinti = {}
    for nod in graf:
        distante[nod] = Inf
        parinti[nod] = None
    distante[start] = 0
    noduri = list(graf.keys())
    while noduri:
        noduri.sort(key=lambda x: distante[x])
        nod = noduri.pop(0)
        if nod == scop:
            break
        for vecin, cost in graf[nod]:
            if distante[nod] + cost < distante[vecin]:
                distante[vecin] = distante[nod] + cost
                parinti[vecin] = nod
    cale = [scop]
    nod = scop
    while parinti[nod] is not None:
        cale.insert(0, parinti[nod])
        nod = parinti[nod]
    return cale, distante[scop]


print(dijkstra(graf, 0, 4))
