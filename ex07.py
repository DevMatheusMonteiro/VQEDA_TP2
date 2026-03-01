def insertion_sort(array):
    comparisons = 0
    shifts = 0
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if temp < array[j]:
                array[j + 1] = array[j]
                shifts += 1
                j -= 1
            else:
                break
        array[j + 1] = temp
    return array, comparisons, shifts

array, comparisons, shifts = insertion_sort([3, 2, 4, 1, 5, 6])
print("Lista ordenada:", array)
print("Comparações:", comparisons)
print("Trocas:", shifts)

array, comparisons, shifts = insertion_sort([6, 5, 4, 3, 2, 1])
print("Lista ordenada:", array)
print("Comparações:", comparisons)
print("Trocas:", shifts)

array, comparisons, shifts = insertion_sort([1, 2, 3, 4, 5, 6])
print("Lista ordenada:", array)
print("Comparações:", comparisons)
print("Trocas:", shifts)