# Projeto de Organizador Counting Sort
# Obtendo a lista de números
print("Insira os elementos da lista a serem ordenados, utilizando espaços para diferencia-los: ")
listaA = [int(x) for x in input().split()]
listaB = []
listaC = []
i = 1
y = 1

# Inserindo no início da fila 0
listaA.insert(0, 0)

# Gerando o tamanho da lista C
while i <= (max(listaA)+1):
    listaC.append(0)
    i += 1

# Resetando i
i = 1

# Gerando lista B
while i <= len(listaA):
    listaB.append(0)
    i += 1

# Obtendo os valores de A e inserindo em C
for y in range(len(listaC)):
    if y == 0:
        listaC[y] = listaA.count(y)-1
    else:
        listaC[y] = listaA.count(y)

# Somando os anteriores em C
for z in range(1, len(listaC)):
    listaC[z] += listaC[z-1]

# Gerando vetor B atualizado
for w in reversed(listaA):
    if w != 0:
        listaB[listaC[w]] = w
        listaC[w] -= 1

print("Vetor de Resposta: ", end='')
for rsp in range(1, len(listaB)):
    print(listaB[rsp], end='')
    if rsp < (len(listaB)-1):
        print(", ", end='')
    else:
        print("")

