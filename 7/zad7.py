# Algorytm zachłanny, działa po kolumnach. Trzymamy tablicę maksymalnych dystansów dla każdego pola wielkości n x n.
# Dla każdej kolumny zapamiętujemy jej "punkty graniczne". Następnie dla każdej kolumny bierzemy te "punkty graniczne" i
# propagujemy, czyli dopóki nie napotkamy bariery ustawiamy tablicę obecnego max dystansu na max z obecnej wartości i
# wartości poporzedniego pola + 1, następnie przesuwamy się w górę i w dół. Zwracamy wartość największego dystansu dla
# [n-1, n-1]

# Złożoność O(n^3)

from zad7testy import runtests

def maze( L ):
    n = len(L)
    T = [[0 for _ in range(n)] for _ in range(n)]
    start = [0]
    new_start = []
    for x in range(n):
        for point in start:
                i = point
                v = T[i][x-1]+1
                while 0 <= i < n and L[i][x] == ".":
                    T[i][x] = max(T[i][x],v)
                    v+=1
                    i+=1
                if x+1<n and L[i-1][x+1] != "#" and not i-1 in new_start:
                    new_start.append(i - 1)
                i = point
                v = T[i][x-1]+1
                while 0 <= i < n and L[i][x] == ".":
                    T[i][x] = max(T[i][x],v)
                    v+=1
                    i-=1
                if x+1<n and L[i+1][x+1] != "#" and not i+1 in new_start:
                    new_start.append(i + 1)
        start = new_start
        new_start = []
        if x<n-1:
            for i in range(1,n-1):
                if (L[i+1][x+1] == "#" or L[i-1][x+1] == "#") and T[i][x]!=0 and L[i][x+1] == ".":
                    if not i in start:
                        start.append(i)
    return T[n-1][n-1]-1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )