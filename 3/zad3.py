# Algorytm działa na podstawie sum częściowych ilości dominowanych punktów osobno dla współrzędnej x i y.
# Odejmując od ich sumy dla danego punktu ilość wszystkich punktów z zasady włączeń i wyłączeń otrzymujemy:
# liczba punktów dominowanych - liczba punktów dominujących dany punkt.
# Wystarczy znaleźć maksymalną wartość tego wyrażenia. Jest to nasz wynik.
# Złożoność O(n)
from zad3testy import runtests
def dominance(P):
    l = len(P)
    x = [0] * (l + 1)
    y = [0] * (l + 1)

    for point in P:
        x[point[0]] += 1
        y[point[1]] += 1

    for i in range(1,l+1):
        x[i] += x[i-1]
        y[i] += y[i-1]

    max_dom = 0
    for point in P:
        dom = x[point[0]-1]+y[point[1]-1]-l+1
        if dom > max_dom:
            max_dom = dom

    return max_dom

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True)
