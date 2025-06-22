import random
import time
from typing import List

def quick_sort(arr: List[int], low: int, high: int) -> None:
    if low >= high:
        return

    random_index = random.randint(low, high)
    randArr = arr[random_index]
    arr[random_index], arr[low] = arr[low], arr[random_index]

    lowerThanRandArr = low
    greaterThanRandArr = high
    i = low + 1

    while i <= greaterThanRandArr:
        if arr[i] < randArr:
            arr[i], arr[lowerThanRandArr] = arr[lowerThanRandArr], arr[i]
            i += 1
            lowerThanRandArr += 1
        elif arr[i] > randArr:
            arr[i], arr[greaterThanRandArr] = arr[greaterThanRandArr], arr[i]
            greaterThanRandArr -= 1
        else:
            i += 1

    quick_sort(arr, low, lowerThanRandArr - 1)
    quick_sort(arr, greaterThanRandArr + 1, high)

def print_first_elements(arr: List[int], count: int = 20) -> None:
    print(" ".join(map(str, arr[:count])))

random.seed(time.time())

N = 1000000   # Больше достаточно сильно замедляет программу
RANGE = N

arr = [random.randint(1, RANGE) for _ in range(N)]

print("First 20 elements of the original array:")
print_first_elements(arr)

start_time = time.time()

quick_sort(arr, 0, len(arr) - 1)

end_time = time.time()
duration = (end_time - start_time) * 1000

print("\nFirst 20 elements of the sorted array:")
print_first_elements(arr)

print(f"\nTime taken by Quick sort: {duration:.2f} ms")
