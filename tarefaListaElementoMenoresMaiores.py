# Função recursiva que retorna os elementos menores ou iguais a x
def menores_ou_iguais(lista, x):
		if len(lista) == 0:
				return []  # Caso base: lista vazia
		# Se o primeiro elemento for <= x, inclui na lista, se não ignora
		if lista[0] <= x:
				return [lista[0]] + menores_ou_iguais(lista[1:], x)
		else:
				return menores_ou_iguais(lista[1:], x)


# Função recursiva que retorna os elementos maiores que x
def maiores_que(lista, x):
    if len(lista) == 0:
        return []  # Caso base: lista vazia
    # Se o primeiro elemento for > x, inclui na lista, se não ignora
    if lista[0] > x:
        return [lista[0]] + maiores_que(lista[1:], x)
    else:
        return maiores_que(lista[1:], x)


# Programa principal para testar as funções
if __name__ == "__main__":
		lista = [1, 7, 3, 9, 4, 2]
		x = 4
		print("Lista original:", lista)
		print(f"Elementos menores ou iguais a {x}: {menores_ou_iguais(lista, x)}")

		lista = [1, 7, 3, 9, 4, 2]
		x = 4
		print("Lista original:", lista)
		print(f"Elementos maiores que {x}: {maiores_que(lista, x)}")
