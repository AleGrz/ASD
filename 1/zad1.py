# Algorytm bazuje na iteracyjnym sortowaniu przez scalanie.
# Podzielony jest on na 3 etapy.
# Najpierw tworzymy "pień" drzewa - 2k wartowników połączoych wskaźnikiem next_level
# Drugi etap to wypełnienie drzewa kolejnymi elementami listy p
# tak, by każda gałąź miała kolejne elementy oddalone od siebie o 2k:
# gałąź 1: 1 -> 2k+1 -> 4k+1 -> ... -> n-2k+1, gałąź 2: 2 -> 2k+2 -> ... -> n-2k+2, gałąź 2k: 2k -> 4k -> ... -> n
# Jest to wydajne dzięki pamiętaniu wskaźnika last_item przy każdym dodawaniu elementu
# Utworzenie takiego drzewa gwarantuje nam, że każda gałąź jest już posortowaną listą.
# Teraz wystarczy scalić gałęzie. Biorę pary gałęzi i scalam je funkcją merge(). Robię tak aż w drzewie zostaje 1 gałąż.
# Pozostało zwrócić ją jako wynik.
# Złożoność to: 2*k (utworzenie pnia) + n (wypełnienie drzewa) + n*log(2*k) (scalenie gałęzi), co sprowadza się do:
# O(n*log(k))
# k = Θ(1) -> O(n)
# k = Θ(log(n)) -> O(n*log(log(n)))
# k = Θ(n) -> O(n*log(n))

import math

from zad1testy import Node, runtests


class SortNode:
    def __init__(self):
        self.next = Node()
        self.last_item = self
        self.next_level = None

    def add_to_end(self,node):
        self.last_item.next = node
        self.last_item = self.last_item.next


def merge(a,b):
    beg = Node()
    final = beg
    while a is not None and b is not None:
        if a.val < b.val:
            final.next = a
            a = a.next
        else:
            final.next = b
            b = b.next
        final = final.next

    if a is not None:
        final.next = a
    elif b is not None:
        final.next = b
    return beg.next


def SortH(p,k):
    if k == 0:
        return p
    k *= 2
    tree = SortNode()
    tree2 = tree

    for i in range(k):
        tree2.next_level = SortNode()
        tree2 = tree2.next_level

    while p.next is not None:
        tree2 = tree.next_level
        while tree2 is not None:
            tree2.add_to_end(p)
            tree2 = tree2.next_level
            if p.next is None:
                break
            p = p.next

    tree2 = tree.next_level
    while tree2 is not None:
        tree2.last_item.next = None
        tree2 = tree2.next_level


    for _ in range(math.ceil(math.log2(k))):
        a = tree.next_level
        b = tree.next_level.next_level
        while a is not None and b is not None:
            a.next = merge(a.next, b.next)
            a.next_level = b.next_level
            a = a.next_level
            b = a
            if b is not None:
                b = b.next_level

    return tree.next_level.next

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )