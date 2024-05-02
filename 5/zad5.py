# Algorytm oparty na podwójnym algorytmie Dijkstry: od początkowego wierzchołka i od końcowego. Sprawdzamy 3 odległości:
# Najmniejszą z wierzchołka a do portalu, najmniejszą z wierzchołka b do portalu, oraz odległość od a do b.
# Zwracamy najmniejszą odległość ze zbioru {a do b, a do portalu + b do portalu}
#
# Złożoność O(E*log(V))

import math

from zad5testy import runtests
from queue import PriorityQueue


def list_graph(G, T):
    for node in G:
        T[node[0]].append((node[1], node[2]))
        T[node[1]].append((node[0], node[2]))


def dijikstra(T, a, v):
    lens = [float('inf') for _ in range(v + 1)]
    q = PriorityQueue()
    q.put((0, a))
    lens[a] = 0
    while not q.empty():
        l, node = q.get()
        for vert, vert_l in T[node]:
            cur = lens[vert]
            new = l + vert_l
            if new < cur:
                lens[vert] = new
                q.put((new, vert))
    return lens

def spacetravel(n, E, S, a, b):
    a_portal = math.inf
    b_portal = math.inf
    v = 0
    for n in E:
        if n[1] > v:
            v = n[1]
    T = [[] for _ in range(v + 1)]
    list_graph(E, T)
    lens = dijikstra(T, a, v)
    for i in S:
        if lens[i] < a_portal:
            a_portal = lens[i]
    a_b = lens[b]
    lens = dijikstra(T, b, v)
    for i in S:
        if lens[i] < b_portal:
            b_portal = lens[i]
    if a_b == math.inf and a_portal+b_portal == math.inf:
        return None
    if a_b > a_portal+b_portal:
        return a_portal+b_portal
    return a_b


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
