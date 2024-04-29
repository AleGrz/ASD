# Algorytm zaczyna od stworzenia posortowanej kopii tablicy przy pomocy heapsorta.
# Iterujemy przez każdy element w oryginalnej tablicy od  tyłu, sprawdzając jego indeks w posortowanej
# tablicy wyszukiwaniem binarnym. Jest to jego ranga. Następnie usuwamy go z posortowanej tablicy, aby nie "psuł" wyniku
# dla następnego elementu. Obecną najwyższą rangę trzymamy w zmiennej maks, którą aktualizujemy jeśli obecna ranga jest
# większa. Po przejściu przez całą tablicę mamy gwarancję, że w zmiennej maks znajduje sie najwyższa ranga i to właśnie
# ją zwracamy. Jest jeszcze drobna optymalizacja: jeśli obecnie maksymalna ranga jest większa od obecnego indeksu, nie
# ma sensu sprawdzać mniejszych indeksów, więc zwracam ją jako największą rangę
#
# Złożoność obliczeniowa: kopiowanie tablicy (n) + heapsort (n*log(n)) +
# + iterowanie przez całą tablicę (n) * wyszukiwanie binarne i usuwanie (n), co sprowadza się do O(n^2)
#
# Złożoność pamięciowa: O(n) (kopiuję tablicę do posortowania)

from kol1testy import runtests


def build_heap(T):
    n = len(T)
    for i in range((n - 1) // 2, -1, -1):
        heapify(T, n, i)


def heapify(T, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    m = i
    if l < n and T[l] > T[m]:
        m = l
    if r < n and T[r] > T[m]:
        m = r
    if i != m:
        T[i], T[m] = T[m], T[i]
        heapify(T, n, m)


def heapsort(T):                              # zwykły heapsort do posortowania tablicy
    n = len(T)
    build_heap(T)
    for i in range(n - 1, -1, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)


def findbin(l, v):                            # wyszukiwanie binarne z cofaniem do najmniejszego elementu dla
    left = 0                                  # multizbiorów
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] > v:
            right = mid - 1
        elif l[mid] < v:
            left = mid + 1
        else:
            while mid > 0 and l[mid - 1] == v: # ponieważ bierzemy pod uwagę tylko elementy mniejsze od v
                mid -= 1
            return mid


def maxrank(T):
    s = [v for v in T]  # tworzę kopię tablicy T
    heapsort(s)         # sortuję ją
    l = len(T)
    maks = 0
    for i in range(l - 1, -1, -1):  # idąc od tyłu iteruję przez każdy element
        ind = findbin(s, T[i])      # szukam rangi, czyli indeksu w posortowanej tablicy
        if ind > maks:              # w miarę potrzeb aktualizuję maks
            maks = ind
        if maks > i:                # jeśli maks jest większy od obecnego indeksu w T, to nie ma sensu sprawdzać dalej
            return maks
        s.pop(ind)                  # usuwam element z posortowanej tablicy
    return maks


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxrank, all_tests=True)
