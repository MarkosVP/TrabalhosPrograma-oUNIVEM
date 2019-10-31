# o objetivo do código que se segue é:
# 1º Criar uma lista com as letras da frase inserida
# 2º Criar um Dictionary organizado por frequência a partir da lista anterior
# 3º Gerar uma lista de Nós da Árvore de Huffman, organizando-a em tempo real
# 4º Criar a árvore de Huffman vinculando suas frequências

from Arvore import Arvore
from pprint import pprint

# Função que cria um Dictionary
def setDictionary(variable, frequency):
    dict = {}
    dict["var"]=variable
    dict["freq"]=frequency
    return dict

# Função que obtem valor da Variável
def getVariable(dict):
    return dict.get("var")

# Função que obtem valor da Frequência
def getFrequency(dict):
    return dict.get("freq")

# Função que altere o valor da Frequência
def setFrequency(dict, frequency):
    dict["freq"]=frequency

def CreateNo(dict):
    # Criando noa e nob como do tipo Arvore
    noa = Arvore(str(dict.get("var")), None, False) # noa recebe índice
    nob = Arvore(None, int(dict.get("freq")), True) # nob recebe a requencia do nó
    nob.setDireita(noa) # nob recebe a sua direita o noa, vinculando FreqNode com ValNode

    return nob

# Obter a sequência de caracteres e criar uma lista com eles individuais
lpalavra = list(str(input("Insira uma série de caracteres: ")))
ldict=[]
i=0

# Criar a lista de Dictionaries
while i < len(lpalavra):
    if len(ldict) > 0:
        not_exists = True
        for x in ldict:
            if getVariable(x) == lpalavra[i]:
                setFrequency(x, (int(getFrequency(x))+1))
                not_exists = False
        if not_exists:
            ldict.append(setDictionary(lpalavra[i], 1))
    else:
        ldict.append(setDictionary(lpalavra[i], 1))
    i+=1

# Organizar Lista
ldict.sort(key=getFrequency)

# Criando a árvore de Huffman
huffman=[]

if( len(huffman) == 0 ):
    huffman.append(CreateNo(ldict[0]))
    del ldict[0]
#elif( len(huffman) > 0 ):
    # for x in ldict:

print(huffman[0].getFrequencia())
print(huffman[0].getDireita().getDado())