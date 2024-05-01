# Aleksander Grzybek
# Algorytm naiwny, sprawdza wszystkie możliwe ścieżki za każdym razem zapisując część wspólną obecnego przedziału i
# przedziału następnego elementu. Jeśli jest to zbiór pusty dla każdej ścieżki to wynikiem jest Fałsz. Jeśli algorytm
# znajdzie ścieżkę z przedziałem <a,b>, gdzie a <= b, to zwraca wartość True.
# Złożoność O(n!)

from zad4testy import runtests

def union(b1,t1,b2,t2):
    top = min(t1,t2)
    bottom = max(b1,b2)
    if top >= bottom:
        return bottom, top
    return None
def list_graph(G,T):
    for node in G:
        T[node[0]].append((node[1],node[2]))
        T[node[1]].append((node[0],node[2]))
def Flight(L,x,y,t):
    v = 0
    for n in L:
        if n[1] > v:
            v = n[1]
    T = [[] for _ in range(v+1)]
    list_graph(L,T)
    s = []
    for el in T[x]:
        vis = [False] * (v + 1)
        top = el[1]+t
        bottom = el[1]-t
        s.append((el[0],bottom, top))
        while len(s)>0:
            node = s.pop()
            if node[0]==y:
                return True
            if not vis[node[0]]:
                vis[node[0]] = True
                for n in T[node[0]]:
                    top = n[1] + t
                    bottom = n[1] - t
                    r = union(node[1], node[2], bottom, top)
                    if r:
                        s.append((n[0], r[0], r[1]))
    return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True)
