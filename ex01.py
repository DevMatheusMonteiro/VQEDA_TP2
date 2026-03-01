def largest_unique_number(array):
    max_value = 0
    accesses = 0
    comparisons = 0
    for i, num_i in enumerate(array):
        accesses += 1 # Acessando i-ésimo elemento num_i
        is_unique = True
        for j, num_j in enumerate(array):
            accesses += 1 # Acessando j-ésimo elemento num_j
            if i != j:
                comparisons += 1 # Comparando num_i com num_j
                if num_i == num_j:
                    is_unique = False
        if is_unique:
            comparisons += 1 # Comparando num_i com max_value
            if num_i > max_value:
                max_value = num_i
    return max_value, accesses, comparisons

def largest_unique_number_with_hash_table(array):
    hash_table = {}
    max_value = 0
    accesses = 0
    comparisons = 0
    for num in array:
        accesses += 1 # Checando se o número já está na hash table
        if num in hash_table:
            accesses += 1 # Checando se o número estava como único na hash table
            if hash_table[num]:
                hash_table[num] = False
                accesses += 1 # Escrita para marcar como não único
        else:
            hash_table[num] = True
            accesses += 1 # Escrita para marcar como único
    for num, is_unique in hash_table.items():
        accesses += 1 # Acessando o número e seu status de unicidade na hash table
        if is_unique:
            comparisons += 1 # Comparando num com max_value
            if num > max_value:
                max_value = num
    return max_value, accesses, comparisons

dados = [1, 2, 4, 3, 5]
print(f"Dados: {dados} - Tamanho: {len(dados)}")
max_value, accesses, comparisons = largest_unique_number_with_hash_table(dados)
print("==== Hash Table ====")
print(f"Maior número único: {max_value} - Acessos à estrutura: {accesses} - Comparações: {comparisons}")
max_value, accesses, comparisons = largest_unique_number(dados)
print("==== Lista com Laços Aninhados ====")
print(f"Maior número único: {max_value} - Acessos à estrutura: {accesses} - Comparações: {comparisons}")
print()
dados = [10, 20, 40, 30, 50, 50, 40, 30]
print(f"Dados: {dados} - Tamanho: {len(dados)}")
max_value, accesses, comparisons = largest_unique_number_with_hash_table(dados)
print("==== Hash Table ====")
print(f"Maior número único: {max_value} - Acessos à estrutura: {accesses} - Comparações: {comparisons}")
max_value, accesses, comparisons = largest_unique_number(dados)
print("==== Lista com Laços Aninhados ====")
print(f"Maior número único: {max_value} - Acessos à estrutura: {accesses} - Comparações: {comparisons}")
