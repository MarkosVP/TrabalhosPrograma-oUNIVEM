# O código em questão trabalha com o valor ASCII das palavras digitadas
# É realizada a soma total da String em ASCII e realizada a divisão por 100
# O resto da divisão será o endereçamento de nossa palavra
from HashingTable import HashingTable

# Gerando base do programa
# Inicializando variáveis de controle
op = 0
hashtable = [HashingTable('')]*100

while op != 4:
    # Declarando menu
    print('                        Gerador de Tabela Hashing')
    print('Selecione uma opção:')
    print('1. Inserir na Tabela')
    print('2. Buscar elemento')
    print('3. Imprimir Tabela')
    print('4. Sair')
    print('')

    op = int(input('Seleção: '))
    print('')

    # Inserção de palavras
    if op == 1:
        dado = str(input('Insira a palavra a ser inserido: '))
        chave = 0

        # Valida se o dado informado tem mais que 100 caracteres
        if len(dado) >= 100:
            print('Palavra digitada maior do que o esperado!')
            print('Máximo de 99 Caracteres.')
            continue

        # Obtendo o a soma do código ASCII da palavra
        for c in dado:
            chave += int(ord(c))

        # Obtendo o endereçamento do nosso elemento
        endereco = chave % 100

        # Inserindo na lista
        # Caso esteja vazio o primeiro elemento
        if hashtable[endereco].getData() == '':
            hashtable[endereco] = HashingTable(dado)
        # Caso o primeiro elemento não esteja vazio
        else:
            # Obtendo proximo elemento
            prox = hashtable[endereco].getProx()

            # Caso o proximo seja Nulo, insere nele
            if prox is None:
                hashtable[endereco].setProx(HashingTable(dado))
            # Caso o Proximo não seja nulo, busca até achar um Nulo
            else:
                while prox is not None:
                    if prox.getProx() is None:
                        # Insere nessa posição e encerra o Loop
                        prox.setProx(HashingTable(dado))
                        break
                    else:
                        # Vai para oproximo elemento
                        prox = prox.getProx()


        # Validando se o elemento foi inserido na posição correta
        if hashtable[endereco].getData() == dado:
            print('Inserção concluída!')
        else:
            # Percorre palavras da chave até localizar ou parar em Nulo
            prox = hashtable[endereco].getProx()

            while prox is not None:
                if prox.getData() == dado:
                    print('Inserção concluída!')
                    break
                else:
                    prox = prox.getProx()

            if prox is None:
                print('Erro!')
        print('')

    # Buscando palavras
    elif op == 2:
        dado = str(input('Insira a palavra de nossa Busca: '))
        chaveBusca = 0

        # Valida se o dado informado tem mais que 100 caracteres
        if len(dado) >= 100:
            print('Palavra digitada maior do que o esperado!')
            print('Máximo de 99 Caracteres.')
            continue

        # Obtendo o a soma do código ASCII da palavra
        for char in dado:
            chaveBusca += int(ord(char))

        # Obtendo o endereçamento do nosso elemento
        endereco = chaveBusca % 100

        # Realizando a busca
        if hashtable[endereco].getData() == dado:
            print("A palavra '", dado, "' está presente na nossa tabela!")
        else:
            prox = hashtable[endereco].getProx()
            while prox is not None:
                if prox.getData() == dado:
                    print("A palavra '", dado, "' está presente na nossa tabela!")
                    break
                else:
                    prox = prox.getProx()

            if prox is None:
                print("Palavra não localizada!!")
        print('')

    # Imprimindo nossa lista com as palavras
    elif op == 3:
        print('Imprimindo a lista:')
        for vt in hashtable:
            if vt.getData() != '':
                prox = vt
                while prox is not None:
                    print(prox.getData(), end='')
                    prox = prox.getProx()

                    if prox is not None:
                        print(" - ", end='')
                print('')

    else:
        print('Encerrando...')