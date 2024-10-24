import time
import random


# Função quickSort1: modifica a lista original
def quickSort1(lista):
    quickS(lista, 0, len(lista) - 1)

def quickS(lista, esq, drt):
    if esq < drt:
        pontoPartic = particao(lista, esq, drt)
        quickS(lista, esq, pontoPartic - 1)
        quickS(lista, pontoPartic + 1, drt)

def particao(lista, first, last):
    pivotvalue = lista[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and lista[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while lista[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = lista[leftmark]
            lista[leftmark] = lista[rightmark]
            lista[rightmark] = temp
    temp = lista[first]
    lista[first] = lista[rightmark]
    lista[rightmark] = temp
    return rightmark


# Função menoresIgPivo para quickSort2
def menoresIgPivo(lista, pivo):
    return [x for x in lista if x <= pivo]


# Função maioresPivo para quickSort2
def maioresPivo(lista, pivo):
    return [x for x in lista if x > pivo]


# Função quickSort2: retorna uma nova lista ordenada
def quickSort2(lista):
    if len(lista) < 2:
        return lista
    pivo = lista[0]
    menores = menoresIgPivo(lista[1:], pivo)
    maiores = maioresPivo(lista[1:], pivo)
    return quickSort2(menores) + [pivo] + quickSort2(maiores)


# Função para medir o tempo de execução para os algoritmos quickSort1 e quickSort2
def medir_tempo(tamanho_lista):
    lista = [random.randint(0, 1000) for _ in range(tamanho_lista)]

    #print("Lista original:", lista)

    # Teste com quickSort1 (modifica a lista original)
    lista_copia1 = lista.copy()
    t_ini_1 = time.perf_counter()
    quickSort1(lista_copia1)
    t_fin_1 = time.perf_counter()

    # Teste com quickSort2 (retorna uma nova lista)
    lista_copia2 = lista.copy()
    t_ini_2 = time.perf_counter()
    nova_lista_ordenada = quickSort2(lista_copia2)
    t_fin_2 = time.perf_counter()

    #print("Lista ordenada (quickSort2):", nova_lista_ordenada)

    # Retorna o tempo de execução para ambos os algoritmos
    return t_fin_1 - t_ini_1, t_fin_2 - t_ini_2


# Executa os testes para diferentes tamanhos de lista
tamanhos = [100, 1000, 5000, 10000, 30000]
resultados = {}

for tamanho in tamanhos:
    tempo_qs1, tempo_qs2 = medir_tempo(tamanho)
    resultados[tamanho] = (tempo_qs1, tempo_qs2)

# Exibir os resultados em um formato de tabela
print(f"{'Tamanho da Lista':<20} {'Tempo quickSort1 (s)':<25}"
      f" {'Tempo quickSort2 (s)':<25}")
for tamanho, (tempo1, tempo2) in resultados.items():
    print(f"{tamanho:<20} {tempo1:<25} {tempo2:<25}")
