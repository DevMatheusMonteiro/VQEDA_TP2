def first_non_repeated_char(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in text:
        if char_count[char] == 1:
            return char
    return None

print(first_non_repeated_char("abracadabra"))
print(first_non_repeated_char("Matheus"))
print(first_non_repeated_char("Carlos"))
