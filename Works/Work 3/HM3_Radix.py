import random
import time
from typing import List

def combine_buckets(buckets: List[List[int]]) -> List[int]:
    combined_array = []
    for bucket in buckets:
        combined_array.extend(bucket)
    return combined_array


def sort_by_digit(arr: List[int], digit_place: int) -> None:
    buckets = [[] for _ in range(10)]
    for num in arr:
        bucket_index = (num // digit_place) % 10
        buckets[bucket_index].append(num)
    arr[:] = combine_buckets(buckets)


def radix_sort(arr: List[int]) -> None:
    max_val = max(arr)
    digit_place = 1
    while max_val // digit_place > 0:
        sort_by_digit(arr, digit_place)
        digit_place *= 10


def print_first_elements(arr: List[int], count: int = 20) -> None:
    print(" ".join(map(str, arr[:count])))


random.seed(time.time())

N = 1000000     # Больше достаточно сильно замедляет программу
RANGE = N

arr = [random.randint(1, RANGE) for _ in range(N)]

print("First 20 elements of the original array:")
print_first_elements(arr)

start_time = time.time()

radix_sort(arr)

end_time = time.time()
duration = (end_time - start_time) * 1000

print("\nFirst 20 elements of the sorted array:")
print_first_elements(arr)

print(f"\nTime taken by the Radix sort: {duration:.2f} ms")


