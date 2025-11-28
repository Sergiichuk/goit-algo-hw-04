import random
import timeit



# Сортування вставками
def insertion_sort(arr):
    arr = arr[:]  # копія
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
    return arr


# Сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0


    # злиття двох списків
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result



# Тестування

def compare_algorithms():
    sizes = [500, 2000, 5000]  # щоб не зависало
    print("Порівняння insertion sort, merge sort та Timsort\n")

    for n in sizes:
        print(f"Розмір масиву: {n}")
        data = [random.randint(1, 100000) for _ in range(n)]

        t1 = timeit.timeit(lambda: insertion_sort(data), number=1)
        t2 = timeit.timeit(lambda: merge_sort(data), number=1)
        t3 = timeit.timeit(lambda: sorted(data), number=1)

        print(f"Insertion sort: {t1:.4f} сек")
        print(f"Merge sort:     {t2:.4f} сек")
        print(f"Timsort:        {t3:.4f} сек\n")




if __name__ == "__main__":
    compare_algorithms()
