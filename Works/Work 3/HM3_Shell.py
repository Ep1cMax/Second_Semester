import random
import time
from typing import List


def shell_sort(arr: List[int]) -> None:
    n = len(arr)
    step = n // 2

    while step > 0:
        for i in range(step, n):
            temp = arr[i]
            j = i

            while j >= step and arr[j - step] > temp:
                arr[j] = arr[j - step]
                j -= step

            arr[j] = temp

        step = step // 2


def print_first_elements(arr: List[int], count: int = 20) -> None:
    print(" ".join(map(str, arr[:count])))

random.seed(time.time())

N = 100000  # Больше достаточно сильно замедляет программу
RANGE = N

arr = [random.randint(1, RANGE) for _ in range(N)]

print("Первые 20 элементов исходного массива:")
print_first_elements(arr)

start_time = time.time()
shell_sort(arr)
end_time = time.time()
duration = (end_time - start_time) * 1000

print("\nПервые 20 элементов отсортированного массива:")
print_first_elements(arr)

print(f"\nВремя выполнения сортировки Шелла: {duration:.2f} мс")
