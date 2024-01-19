"""
Zad. 1
Stwórz funkcję, do której prześlesz listę o rozmiarze 15 elementów. Funkcja ma rekurencyjnie
 wyświetlić wszystkie elementy z tablicy.
"""


def display_elements_recursively(lst, index=0):
    if index < len(lst):
        print(lst[index])
        display_elements_recursively(lst, index + 1)


"""
Zad. 2
Stwórz funkcję rekurencyjnie wyliczającą, ile samogłosek ma przesłany tekst. Wynik zwróć w postaci
słownika {samogłoska : ilość_wystąpień}, np.
dla baadace
freq = {‘a’ : 3, ‘e’ : 1}
"""


def count_vowels(text, vowels=['a', 'e', 'i', 'o', 'u']):
    frequency = {vowel: 0 for vowel in vowels}

    def recursive_count(index):
        if index < len(text):
            char = text[index].lower()
            if char in vowels:
                frequency[char] += 1
            recursive_count(index + 1)

    recursive_count(0)

    return frequency


"""
Zad. 3
Spróbuj napisać rekurencję, która spowoduje crash programu w wyniku osiągnięcia, tzw. maksymalnej 
głębi przeszukiwania rekurencyjnego. 
"""


def recursive_crash(counter=0):
    print(f"Recursion level: {counter}")
    recursive_crash(counter + 1)


"""
Zad. 4
Napisz program, który rekurencyjnie wyświetli wszystkie liczby od N (parametr funkcji) do 0.
"""


def display_numbers_recursively(N):
    if N >= 0:
        print(N)
        display_numbers_recursively(N - 1)


"""
Zad. 5
Mając do dyspozycji dowolny słownik, napisz algorytm, który zwróci informację, ile poziomów 
zagnieżdżeń ma rozpatrywany słownik, np.
Przykład 1:
{“value”: [1, 2, 3, 4]} - wynik: 1
{“value”: {“value2” : [1, 2, 3, 4]}} - wynik: 2
itd.
"""


def count_nested_levels(data):
    if not isinstance(data, dict):
        return 0
    elif not data:
        return 1

    nested_levels = [count_nested_levels(value) for value in data.values()]

    return max(nested_levels) + 1


"""
Zad. 6
Algorytmem podobnym do NWD jest, tzw. algorytm wyznaczania NWW (czyli Najmniejszej Wspólnej Wielokrotności). W celu wyznaczenia takiej wartości, wykorzystuje się wzór: 
(a * b) / NWD(a, b), gdzie
NWD to poznany algorytm wyznaczający Największy Wspólny Dzielnik dwóch liczb. 

Mając do dyspozycji powyższe informacje, zaimplementuj funkcję wyznaczającą największą wspólną wielokrotność dwóch dowolny liczb podanych przez użytkownika.
"""


def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def nww(a, b):
    return (a * b) // nwd(a, b)


def nww_nwd(a, b):
    result = nww(a, b)
    print(f"NWW({a}, {b}) = {result}")
