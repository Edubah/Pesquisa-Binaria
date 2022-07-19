#Implementação de um algoritmo de Pesquisa Binária

#Naive search, escaneia um lista e pergunta se é igual ao alvo/objetivo que buscamos
#Se a responsta for SIM retorna um index, se não retorna -1
import random
import time


def naive_search(l, target):
    #Exemplo: l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1



#A Pesquisa Binária utiliza "Dividir para Conquistar"
#Vamos aproveitar o fato de outras listas serem sortidas

def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        #target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    #Uma lista sortida de 10000 números
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))


    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive Search time: ", (end - start) / length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary Search time: ", (end - start) / length, "seconds")