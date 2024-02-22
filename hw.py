import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


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

# Генерація даних
sizes = [100, 1000, 5000, 10000]
data_types = ['Random', 'Sorted', 'Reversed']

# Результати
results = {}

for size in sizes:
    results[size] = {}
    for data_type in data_types:
        if data_type == 'Random':
            data = [random.randint(0, size) for _ in range(size)]
        elif data_type == 'Sorted':
            data = sorted([random.randint(0, size) for _ in range(size)])
        elif data_type == 'Reversed':
            data = sorted([random.randint(0, size) for _ in range(size)], reverse=True)
        
        # Вимірювання часу
        insertion_sort_time = timeit.timeit('insertion_sort(data.copy())', globals=globals(), number=1)
        merge_sort_time = timeit.timeit('merge_sort(data.copy())', globals=globals(), number=1)
        timsort_time = timeit.timeit('sorted(data.copy())', globals=globals(), number=1)
        
        results[size][data_type] = {
            'Insertion Sort': insertion_sort_time,
            'Merge Sort': merge_sort_time,
            'Timsort': timsort_time
        }

# Вивід результатів
for size in sizes:
    print(f"Size: {size}")
    for data_type in data_types:
        print(f"\tData type: {data_type}")
        for sort_type, time_taken in results[size][data_type].items():
            print(f"\t\t{sort_type}: {time_taken:.5f} seconds")
    print("\n")