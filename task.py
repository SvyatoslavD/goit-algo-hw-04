import random
import timeit
import copy

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]


algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Timsort": sorted
}

sizes = [100, 1000, 10000]
for size in sizes:
    print(f"Size: {size}")
    rl = generate_random_list(size)
    rls = [rl, copy.copy(rl), copy.copy(rl)]

    for trl, algo in zip(rls, algorithms):
        time = timeit.timeit(f"{algorithms[algo].__name__}(trl)",
                             number=10,
                             globals=globals())
        print(f"\t{algo:25}: {time:.6f} seconds")

    print()