import random
import time
import threading

def generate_array(size):
    return [random.randint(1, 1000000) for _ in range(size)]


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def threaded_quicksort(arr, low, high, max_depth=0, depth=0):
    if low < high:
        pi = partition(arr, low, high)

        if depth < max_depth:
            left_thread = threading.Thread(
                target=threaded_quicksort,
                args=(arr, low, pi - 1, max_depth, depth + 1)
            )
            left_thread.start()

            threaded_quicksort(arr, pi + 1, high, max_depth, depth + 1)

            left_thread.join()
        else:
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)


def measure_execution_time(func):
    start = time.time()
    func()
    end = time.time()
    return (end - start) * 1000


def main(N):
    #N = 1000000 #Объявление N для вызова основной программы не функцией
    data = generate_array(N)

    data_copy = data.copy()
    time_seq = measure_execution_time(
        lambda: quicksort(data_copy, 0, len(data_copy) - 1)
    )
    print(f"Sequential QuickSort: {time_seq:.2f} ms")

    for threads in [2, 4, 8]:
        data_copy = data.copy()
        max_depth = threads.bit_length() - 1

        time_threaded = measure_execution_time(
            lambda: threaded_quicksort(data_copy, 0, len(data_copy) - 1, max_depth)
        )
        print(f"Threaded QuickSort ({threads} threads): {time_threaded:.2f} ms")


if __name__ == "__main__":
    main(1000000)
