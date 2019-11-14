class HashingTable(object):
    # Estrutura do que seria um elemento do vetor
    def __init__(self, dado, prox=None):
        self.data = dado
        self.next = prox

    # Getters
    def getData(self): return self.data
    def getProx(self): return self.next

    # Setters
    def setData(self, dado): self.data = dado
    def setProx(self, prox): self.next = prox