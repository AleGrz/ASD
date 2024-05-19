# Algorytm bazuje na zmodyfikowanym algorytmie Dijkstry, z dołożonymi krawędziami skoku, i z założeniem że nie można
# przemieszczać się przez 2 kolejne krawędzie skoku. Aby algorytm był poprawny, należy zdefiniować dwie różne tablice
# przechowujące długość - osobno dla normalnych przemieszczeń i dla skoków.
#
# Złożoność obliczeniowa O(n^4)
# Złożoność pamięciowa O(n)

import math
from queue import PriorityQueue

from zad6testy import runtests

def graphify(g):
    c = []
    for i in g:
        c.append([])
        for j in range(len(i)):
            if i[j] > 0:
                c[-1].append([j, i[j], False])
    return c


def dijkstra(G,s,end):
    lens = [math.inf for _ in G]
    lens_jumped = [math.inf for _ in G]
    lens[s] = 0
    lens_jumped[s] = 0
    pq = PriorityQueue()
    pq.put((0,s,True))
    while not pq.empty():
        l, u, can_skip = pq.get()
        for v, w, is_shortcut in G[u]:
            if not is_shortcut:
                cur = lens[v]
                new = l + w
                if new < cur:
                    lens[v] = new
                    pq.put((new,v,True))
            elif can_skip:
                cur = lens_jumped[v]
                new = l + w
                if new < cur:
                    lens_jumped[v] = new
                    pq.put((new,v,False))
    return min(lens[end], lens_jumped[end])

def jumper( G, s, w ):
    C = graphify(G)
    for v in range(len(C)):
        for c in C[v]:
            if not c[2]:
                for d in C[c[0]]:
                    m = max(c[1], d[1])
                    if v != d[0] and not d[2]:
                        for x in C[v]:
                            if x[0] == d[0] and x[2]:
                                x[1] = min(m, x[1])
                                break
                        else:
                            C[v].append([d[0],m,True])
    return dijkstra(C,s,w)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )