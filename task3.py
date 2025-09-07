import time
import random


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def tim_sort(arr):
    return sorted(arr)


def benchmark_sorting_algorithm(sort_func, data):
    start_time = time.time()
    sort_func(data.copy())
    end_time = time.time()
    return end_time - start_time


def main():
    algorithms = {
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
        "Tim Sort": tim_sort
    }

    random_data_small = [random.randint(0, 1000) for _ in range(100)]
    sorted_data_small = sorted(random_data_small)
    reversed_data_small = sorted_data_small[::-1]
    random_data_large = [random.randint(0, 1000) for _ in range(10000)]
    sorted_data_large = sorted(random_data_large)
    reversed_data_large = sorted_data_large[::-1]

    datasets = {"Random Small": random_data_small,
                "Sorted Small": sorted_data_small,
                "Reversed Small": reversed_data_small,
                "Random Large": random_data_large,
                "Sorted Large": sorted_data_large,
                "Reversed Large": reversed_data_large}

    results = {alg: {} for alg in algorithms}
    for alg_name, alg_func in algorithms.items():
        for data_name, data in datasets.items():
            elapsed_time = benchmark_sorting_algorithm(alg_func, data)
            results[alg_name][data_name] = elapsed_time
            print(f"{alg_name} on {data_name}: {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    main()
