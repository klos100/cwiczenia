## Zad 1
"""Napisz funkcję (lub funkcje), które zwrócą maksymalną spośród 3 liczb. W rozwiązaniu skorzystaj tylko z możliwośći
definiowania funkcji i używania w nich operatorów porównania"""


def liczba_max(*args):
    l_max = 0
    for i in args:
        if i > l_max:
            l_max = i
    return l_max


print(liczba_max(12, 15, 10))
print(liczba_max(-1, 5, 100))
print(liczba_max(0, 5, -100))


def test_max_liczba():
    assert liczba_max(12, 45, 102) == 102
    assert liczba_max(1, 45, 10) == 45
    assert liczba_max(-1, 5, 10) == 10
    assert liczba_max(-1, 0, -10) == 0


## Zad 2
"""Napisz funkcję, która: 
1. Jeśli jej argument będzie listą, tuplą bądź zbiroem, zwróci sumę jej elementów
2. Jeśli jej argument będzie słownikiem, zwróci sumę wartości
W obu przypadkach ignoruj napisy - o ile napisy nie reprezentują liczb"""
print()

def suma_wartosci(dane):
    if isinstance(dane, dict):
        dane = dane.values()
    dane_wynik = []
    for i in dane:
        if isinstance(i,(str)):
            if i.isdigit():
                dane_wynik.append(i)
        elif isinstance(i,(int,float)):
            dane_wynik.append(i)
    return sum([float(i) for i in dane_wynik])

print(suma_wartosci(['12',15,'b', 2]))
print(suma_wartosci([12, '15', 2]))
print(suma_wartosci((12, 15, 47, '2', 18, 56)))
print(suma_wartosci({12, 15, 47, 2}))
print(suma_wartosci({'a': '12', 'b': 15, 'c':'2'}))

def test_suma_wartosci():
    assert suma_wartosci((12, 25, 5)) == 42
    assert suma_wartosci({'a':2, 'b':25, 'c':5, 'd':8, 'e':10}) == 50
    assert suma_wartosci([2, 25, 5, 8, 1]) == 41
    assert suma_wartosci({28, 1, 5}) == 34


## Zad 3
"""Napisz funkcję, która sprawdzi czy podany napis jest palindromem"""
print()


def czy_palindrom(tekst):
    tekst = (tekst.replace(" ", "").lower())
    if tekst[::-1] == tekst:
        return "To palindrom"
    return "To nie jest palindrom"


print(czy_palindrom('pannap'))
print(czy_palindrom('dupa i dupa'))
print(czy_palindrom('Igor łamał rogi'))


def test_palindrom():
    assert czy_palindrom('kajak') == "To palindrom"
    assert czy_palindrom('kobyła ma mały bok') == "To palindrom"
    assert czy_palindrom('wanna') == "To nie jest palindrom"


## zad 4
"""Napisz funkcję, które wypisze n pierwszych wierszy trójkąta Pascala"""

print([11**i for i in range(5)])

print()
print()
x = 5
if x == 1:
    trojkat = [[1]]
elif x >1:
    n = x - 1
    trojkat = [[1]]
    linia = [1]
    for i in range(n):
        rzad = []
        for i in range(len(linia)-1):
            rzad.append(linia[i]+linia[i+1])
        rzad.insert(0,1)
        rzad.append(1)
        linia = rzad
        trojkat.append(rzad)

print(trojkat)

## Zad 5
"""Napisz funkcję, która sprawdzi, czy napis jest pangramem."""
print()

import string

def czy_pangram(tekst):
    alfabet = string.ascii_lowercase
    alfaset = set(alfabet)
    if set(tekst.lower()).issuperset(alfaset):
        return "To pangram"
    return "To nie pangram"


def test_pangram():
    assert czy_pangram('The quick brown fox jumps over the lazy dog') == "To pangram"
    assert czy_pangram('Pack my box with five dozen liquor jugs') == "To pangram"
    assert czy_pangram('Jackdaws love my big sphinx of quartz') == "To pangram"
    assert czy_pangram('The the lazy dog') == "To nie pangram"
    assert czy_pangram('Dupa jest dupa') == "To nie pangram"


## Zad 6
"""Napisz funkcję, które sprawdzi, czy zadana liczba jest doskonała"""


def liczba_doskonala(liczba):
    dzielniki = []
    for i in range(1, liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    if sum(dzielniki) == liczba:
        return f"{liczba} jest liczbą doskonałą"
    return f"{liczba} nie jest liczbą doskonałą"


print(liczba_doskonala(496))
print(liczba_doskonala(330))


def test_liczba_perfekcyjna():
    assert liczba_doskonala(6) == "6 jest liczbą doskonałą"
    assert liczba_doskonala(28) == "28 jest liczbą doskonałą"
    assert liczba_doskonala(7) == "7 nie jest liczbą doskonałą"


## Zad 7
"""Napisz dekorator, który będzie printował w konsoli czas wykonania dekorowanej funkcji."""

print()
import time


def kontrola_czas(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        funkcja(*args, **kwargs)
        stop = time.time()
        czas = stop - start
        return (f"Czas trwania funkcji: {czas} s")

    return wrapper


@kontrola_czas
def funkc():
    slownik = {x: x ** 2 for x in range(100000)}
    # print (slownik)


print(funkc())
