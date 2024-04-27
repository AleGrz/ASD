# Program działa na podstawie tablicy częstości posortowanej przy pomocy sortowania pozycyjnego.
# Tworzymy ją i wypełniamy częstością występowania pierwszych p elementów. szukamy k-tego elementu od końca i dodajemy
# go do sumy. Iterujemy przez całą tablicę, za każdym razem usuwając ostatni i dodając następny element używając
# wyszukiwania binarnego. Jeśli usuwamy większy element od obecnego k-tego i dodajemy mniejszy lub równy, przesuwamy
# k-ty element o 1 do przodu. Jeśli usuwamy mniejszy lub równu element od k-tego i dodajemy większy, przesuwamy
# k-ty element o 1 do tyłu. Za każdym razem dodajemy wartość obecnego k do sumy.
#
# Złożoność obliczeniowa: O(n**2-n*p)
# Złożoność pamięciowa: P(n)

from zad2testy import runtests


def k_move_step_back(T, ind, pos):
    if pos >= T[ind][1]:
        ind -= 1
        while T[ind][1] == 0:
            ind -= 1
        pos = 1
    else:
        pos += 1
    return ind, pos


def k_move_step_forward(T, ind, pos):
    if pos <= 1:
        ind += 1
        while T[ind][1] == 0:
            ind += 1
        pos = T[ind][1]
    else:
        pos -= 1
    return ind, pos


def remove(t, val):
    ind = find_val(t, val)
    t[ind][1] -= 1
    return ind


def add(t, val):
    ind = find_val(t, val)
    t[ind][1] += 1
    return ind


def find_val(t, v):
    left, right = 0, len(t)
    while left <= right:
        ind = (left + right) // 2
        if t[ind][0] == v:
            return ind
        elif t[ind][0] < v:
            left = ind + 1
        else:
            right = ind - 1


def unique(l):
    radix_sort(l)
    out = []
    prev = None
    for i in l:
        if i != prev:
            out.append([i, 0])
            prev = i
    return out


def maks(arr):
    m = arr[0]
    for i in arr:
        if i > m:
            m = i
    return m


def radix_sort(arr):
    m = maks(arr)
    p = 1
    while m // p > 0:
        counting_sort(arr, p)
        p *= 10


def counting_sort(arr, p):
    s = len(arr)
    c = [0] * 10
    out = [0] * s

    for i in range(0, s):
        ind = arr[i] // p
        c[ind % 10] += 1
    for i in range(1, 10):
        c[i] += c[i - 1]
    i = s - 1
    while i >= 0:
        ind = arr[i] // p
        out[c[ind % 10] - 1] = arr[i]
        c[ind % 10] -= 1
        i -= 1

    for i in range(0, s):
        arr[i] = out[i]


def ksum(T, k, p):
    x = T.copy()
    x = unique(x)

    for i in range(p): #p
        add(x, T[i]) #logm

    ind = len(x) - 1
    pos = k

    while pos > x[ind][1]:  #m
        pos -= x[ind][1]
        ind -= 1
    suma = x[ind][0]

    for i in range(p, len(T)):  #n-p
        a = add(x, T[i])    #logm
        r = remove(x, T[i - p]) #logm

        if a <= ind < r:
            ind, pos = k_move_step_back(x, ind, pos)    #m
        elif r <= ind < a:
            ind, pos = k_move_step_forward(x, ind, pos) #m
        elif a < ind and r == ind:
            if pos > x[ind][1]:
                ind, pos = k_move_step_back(x, ind, pos) #m

        suma += x[ind][0]

    return suma

runtests(ksum, all_tests=True)
