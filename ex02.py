import random

def get_intersection(array1, array2):
    intersection = []
    hash_table = {}
    steps = 0
    for num in array1:
        steps += 1 # Incrementa o contador de passos para cada iteração
        hash_table[num] = 0
        steps += 1 # Incrementa o contador de passos para cada inserção na tabela hash
    for num in array2:
        steps += 1 # Incrementa o contador de passos para cada iteração
        steps += 1 # Incrementa o contador de passos para cada comparação
        if num in hash_table:
            if hash_table[num] == 0:
                intersection.append(num)
                # Incrementa o contador de passos para cada inserção na lista de interseção
                steps += 1
                hash_table[num] = 1
                steps += 1 # Incrementa o contador de passos para cada atualização na tabela hash
    return intersection, steps

array1 = [random.randint(1, 100) for _ in range(500)]
array2 = [random.randint(1, 100) for _ in range(500)]
intersection, steps = get_intersection(array1, array2)
print(f"Interseção: {intersection}\nNúmero de passos: {steps}")

array1 = [random.randint(1, 100) for _ in range(500)]
array2 = [random.randint(101, 200) for _ in range(500)]
intersection, steps = get_intersection(array1, array2)
print(f"Interseção: {intersection}\nNúmero de passos: {steps}")
