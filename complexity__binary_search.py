"""
Zad 1.
Wygeneruj listę 30 elementów składających się z liczb całkowitych z przedziału [0, 30]. Następnie, wykorzystując
wyszukiwanie binarne, sprawdź, czy znajduje się w niej co najmniej 10 liczb większych od wartości 20.
Pamiętaj o odpowiednim zmodyfikowaniu listy, aby możliwe było przeprowadzenie procesu wyszukiwania binarnego.
"""
import random


def binary_search_count(lst, target):
    """Perform binary search to count occurrences greater than or equal to the target."""
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return len(lst) - left


def check_numbers_greater_than_20():
    """Generate a list, modify it, and check if there are at least 10 numbers greater than 20."""

    random_list = sorted(random.randint(0, 30) for _ in range(30))

    target_value = 20
    index_to_insert = binary_search_count(random_list, target_value)
    random_list = random_list[index_to_insert:]

    count_greater_than_20 = binary_search_count(random_list, target_value + 1)

    print(f"Generated List: {random_list}")
    print(f"Count of numbers greater than 20: {count_greater_than_20}")

    if count_greater_than_20 >= 10:
        print("There are at least 10 numbers greater than 20.")
    else:
        print("There are less than 10 numbers greater than 20.")


"""
Zad 2.
Mając dane liczby naturalne p i q, znajdź taką liczbę naturalną x, dla której 
 x3 + px = q 
lub ustal, że taka liczba nie istnieje

Wejście 
W pierwszym wierszu wejścia znajduje się liczba zagadek z, nie większa niż 10 000. W kolejnych wierszach podajesz 
liczby naturalne p i q. Obie liczby są dodatnie, liczba p nie przekracza 1012, zaś q – 1018. Liczby są oddzielone
pojedynczym odstępem, każda zagadka podana jest w osobnym wierszu. 

Wyjście 
Wypisz odpowiedzi na wszystkie zagadki, w tej kolejności, w jakiej były podane na wejściu. Odpowiedź powinna być 
liczbą naturalną spełniającą podane równanie. Jeśli taka liczba nie istnieje, zamiast liczby wypisz słowo NIE.

Przykład 
Dla danych wejściowych: 
2 
3 14 
7 10 
poprawnym wynikiem jest: 
2 
NIE
"""


def find_x(p, q):
    if q == 0:
        return 0

    x_min = 0
    x_max = q ** (1 / 3) + 1

    for x in range(x_min, x_max + 1):
        if x ** 3 + p * x == q:
            return x

    return "NIE"


def solve_puzzle(p, q, z):
    for _ in range(z):
        result = find_x(p, q)
        print(result)

solve_puzzle(100, 10, 10)
