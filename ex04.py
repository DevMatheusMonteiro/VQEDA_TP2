def identify_missing_letters(text):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    hash_table = {}
    for letter in text.lower():
        if letter not in hash_table:
            hash_table[letter] = 1
    missing_letters = [l for l in alphabet if l not in hash_table]
    return missing_letters

missing_letters = identify_missing_letters("ABcd fghijlmnopqrstuvwxyz")
print("Letras ausentes:", missing_letters)

missing_letters = identify_missing_letters("123 áéíóú * jklmnopqrstuvwxyz")
print("Letras ausentes:", missing_letters)