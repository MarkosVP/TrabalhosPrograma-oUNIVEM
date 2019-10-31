# Por meio do código a seguir, pretendemos realizar a opera;áo de modelagem e minimizaão de códigos, ou seja
# buscamos compactar valores da melhor forma possível, utilizando Python. Para tal, utlizaremos de orientação
# a objeto, e alguns outros recursos disponíveis.

# Importando a classe da Árvore Binária criada

from Arvore import Arvore


# Função que Cria os nós da Árvore
def CriaNo(frequencia, variavel, no):
    if variavel is None and no is not None:
        noFreq = Arvore(None, int(frequencia), None, no)    # Gerando nó de Frequência

        return noFreq   # Retornando nó de Frequênica, já construido
    elif no is None and variavel is not None:
        noDado = Arvore(str(variavel), None, None, None)  # Gerando nó de Variável
        noFreq = Arvore(None, int(frequencia), None, noDado)  # Gerando nó de Frequência

        return noFreq  # Retornando nó de Frequênica, já construido
    else:
        print("Erro, não foi possível gerar o nó!")


def GerarCodigo(no):
    if no is not None:
        # Gerando o caminho por meio
        if no.getEsquerda() is not None:
            no.getEsquerda().setCaminho(no.getCaminho() + '0')
            GerarCodigo(no.getEsquerda())
        if no.getDireita() is not None:
            no.getDireita().setCaminho(no.getCaminho() + '1')
            GerarCodigo(no.getDireita())


def In_Order(no):
    if no is not None:
        In_Order(no.getEsquerda())
        if no.getFrequencia() is None:
            print("(", no.getDado(), ")", " = ", no.getCaminho())
        In_Order(no.getDireita())


# Gerando lista inicial
huffman = []
# Lista de dictionarys com as respostas
dictResp = {}
# Variável temporária para receber as respostas

# Obtendo uma lista de caracteres e convertendo em lista
lista = list(str(input("Insira a frase/texto a ser comprimida: ")).replace(" ", ""))

# Criando uma lista de nós
huffman.append(CriaNo(1, lista[0], None))
dictResp[lista[0]] = ''
del lista[0]

for i in lista:
    # Variável que estipula se devemos incluir ou não um novo elemento na lista de huffman
    include = True

    # Buscando pelo elemento idêntico e adicionando a frequência do mesmo
    for x in huffman:
        if i == x.getDireita().getDado():
            x.setFrequencia(x.getFrequencia() + 1)
            include = False

    # Caso não localizado na lista 'huffman', gerar novo elemento
    if include:
        huffman.append(CriaNo(1, i, None))
        dictResp[i] = ''

while len(huffman) > 1:
    # Organizando a nossa lista de Huffman
    huffman.sort(key=lambda x: x.getFrequencia())

    # Se nossos nós tiverem valores iguais ou o 1o for menor que o 2o, inserimos a esquerda
    if (huffman[0].getFrequencia() == huffman[1].getFrequencia()) or (
            huffman[0].getFrequencia() < huffman[1].getFrequencia()):
        # Caso nosso nó contém espaço
        if huffman[1].getEsquerda() is None:
            # O nó 0 contém somente um Dado
            if huffman[0].getEsquerda() is None and huffman[0].getDireita() is not None:
                huffman[1].setEsquerda(huffman[0].getDireita())
                huffman[1].setFrequencia(huffman[1].getFrequencia() + huffman[0].getFrequencia())
                del huffman[0]
            # O nó 0 contém mais elementos em si
            else:
                huffman[1].setEsquerda(huffman[0])
                huffman[1].setFrequencia(huffman[0].getFrequencia() + huffman[1].getFrequencia())
                del huffman[0]
        else:
            # O nó 0 contém somente um Dado
            if huffman[0].getEsquerda() is None and huffman[0].getDireita() is not None:
                huffman[1] = (CriaNo(huffman[1].getFrequencia() + huffman[0].getFrequencia(), None, huffman[1]))
                huffman[1].setEsquerda(huffman[0].getDireita())
                del huffman[0]
            # O nó 0 contém mais elementos em si
            else:
                huffman[1] = (CriaNo(huffman[1].getFrequencia() + huffman[0].getFrequencia(), None,huffman[1]))
                huffman[1].setEsquerda(huffman[0])
                del huffman[0]

    # Se o 1o nó for maior que o segundo, inserimos o 2o na esquerda do primeiro
    else:
        # Caso nosso nó contém espaço
        if huffman[0].getEsquerda() is None:
            # O nó 0 contém somente um Dado
            if huffman[1].getEsquerda() is None and huffman[1].getDireita() is not None:
                huffman[0].setEsquerda(huffman[1].getDireita())
                huffman[0].setFrequencia(huffman[1].getFrequencia() + huffman[0].getFrequencia())
                del huffman[1]
            # O nó 0 contém mais elementos em si
            else:
                huffman[0].setEsquerda(huffman[1])
                huffman[0].setFrequencia(huffman[0].getFrequencia() + huffman[1].getFrequencia())
                del huffman[1]
        else:
            # O nó 0 contém somente um Dado
            if huffman[1].getEsquerda() is None and huffman[1].getDireita() is not None:
                huffman[0] = (CriaNo(huffman[1].getFrequencia() + huffman[0].getFrequencia(), None, huffman[0]))
                huffman[0].setEsquerda(huffman[1].getDireita())
                del huffman[1]
            # O nó 0 contém mais elementos em si
            else:
                huffman[0] = (CriaNo(huffman[1].getFrequencia() + huffman[0].getFrequencia(), None, huffman[0]))
                huffman[0].setEsquerda(huffman[1])
                del huffman[1]

# Organizando a nossa lista de Huffman caso a mesma tenha resíduos
huffman.sort(key=lambda x: x.getFrequencia())
GerarCodigo(huffman[0])

In_Order(huffman[0])


