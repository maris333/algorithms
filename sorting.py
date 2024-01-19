"""
Zad. 1
Stwórz program, który zbada czas sortowania poznanymi metodami (Bubble Sort, Insertion Sort, Quick Sort) list o elementach 1000, 10 000, 100 000, 1 000 000 elementów. Wyniki zapisz do pliku tekstowego. Listę wypełniaj losowymi wartościami przy wykorzystaniu modułu random, a czas mierz przy użyciu time.

Podpowiedź:
Pomiar czasu wykonania:

 import datetime
 a = datetime.datetime.now()
 b = datetime.datetime.now()
 c = b - a
 c
datetime.timedelta(0, 4, 316543)
 c.days
0
 c.seconds
4
 c.microseconds
316543

"""


import random
import datetime


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def measure_sorting_time(sort_function, array):
    start_time = datetime.datetime.now()
    sort_function(array)
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    return elapsed_time


def main():
    array_sizes = [1000, 10000, 100000, 1000000]

    with open("sorting_times.txt", "w") as file:
        for size in array_sizes:
            random_array = [random.randint(1, 1000) for _ in range(size)]

            bubble_time = measure_sorting_time(bubble_sort, random_array.copy())
            insertion_time = measure_sorting_time(insertion_sort, random_array.copy())
            quick_time = measure_sorting_time(quick_sort, random_array.copy())

            file.write(f"Array Size: {size}\n")
            file.write(f"Bubble Sort Time: {bubble_time}\n")
            file.write(f"Insertion Sort Time: {insertion_time}\n")
            file.write(f"Quick Sort Time: {quick_time}\n\n")


if __name__ == "__main__":
    main()
