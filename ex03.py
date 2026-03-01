def first_duplicate(array):
    hash_table = {}
    for num in array:
        if num in hash_table:
            return num
        hash_table[num] = 0
    return None

print(first_duplicate(["a", "b", "c", "b"]))
print(first_duplicate(["x", "y", "z", "x"]))
print(first_duplicate(["dog", "cat", "dog"]))
print(first_duplicate(["1", "2", "3", "4", "3"]))
