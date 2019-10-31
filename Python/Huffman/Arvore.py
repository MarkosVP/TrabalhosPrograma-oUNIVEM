class Arvore(object):
    # Inicialização de um nó na arvore deve conter
    # Key: (None, str(X)), Value: (None, int(X))
    def __init__(self, data, value, esq, dir):
        self.esq = esq
        self.dir = dir
        self.frequencia = value     # Integer que recebe a frequência
        self.dado = data             # String que recebe a letra
        self.caminho = ''

    # Getters
    def getFrequencia(self): return self.frequencia
    def getDado(self): return self.dado
    def getEsquerda(self): return self.esq
    def getDireita(self): return self.dir
    def getCaminho(self): return self.caminho

    # Setters
    def setDireita(self, right):    self.dir = right
    def setEsquerda(self, left):    self.esq = left
    def setDado(self, key):         self.dado = key
    def setFrequencia(self, value): self.frequencia = value
    def setCaminho(self, cam):      self.caminho = cam
