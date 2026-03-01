def selection_sort(array):
    n = len(array)
    comparisons = 0
    swaps = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            swaps += 1
            array[i], array[min_index] = array[min_index], array[i]
    return array, comparisons, swaps

array, comparisons, swaps = selection_sort([64, 11, 12, 22, 25])
print("Lista ordenada:", array)
print("Comparações:", comparisons)
print("Trocas:", swaps)
array, comparisons, swaps = selection_sort([5, 2, 9, 1, 5, 6])
print("Lista ordenada:", array)
print("Comparações:", comparisons)
print("Trocas:", swaps)
array, comparisons, swaps = selection_sort([38, 27, 43, 3, 9, 82, 10])
print("Lista ordenada:", array)
print("Comparações:", comparisons)
print("Trocas:", swaps)
