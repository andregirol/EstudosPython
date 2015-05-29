# Pequeno programa que soma os elementos de uma matriz, em ordem,
# e coloca os resultados em outra matriz
# no exemplo, ele somara (ver listas abaixo):

# matrizsoma = [(1+4+7), (2+5+8), (3+6+9)]

# listas padrao para apenas testarmos:
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

# inicializando a matriz para o teste com as listas acima
matriz = [a,b,c]

# Descobre o tamanho as listas menores calculando o tamanho de uma delas (pegando a primeira como cobaia)
tamanholista = len(matriz[0])

#lista que recebe a soma dos valores da primeira matriz
matrizsoma = list()

# guarda a posicao da lista dentro da matriz e controla o laco que vai varrer as listas dentro da matriz (linha 7)
# comecando com zero, que eh a primeira posicao dentro da lista
posicao = 0

###########
# Daqui pra baixo:
# varre a matriz, pega , em ordem, cada elemento das listas e soma na matriz soma:
###########

# esse while vai manter a varredura dos elementos especificos da matriz (por exemplo:
# se posicao = 1, ele vai ler:
#
#       a[1],b[1],c[1] e somar em: matrizsoma[1] e assim por diante...


# enquanto a posicao for menor que o tamanho de todas as matrizes (voce me falou que todas tem o mesmo tamanho)
while posicao < tamanholista:

    for lista in matriz:
        # Aqui, leia assim:

        # tente (try) somar a posicao x da lista dentro da matriz para a 'matrizsoma'
        try:
           matrizsoma[posicao] = matrizsoma[posicao] + lista[posicao]

        # se der pau (except -> excecao em informatica, que significa um erro interno),
        # significa que aquela posicao em 'matrizsoma' esta vazia,
        # como o python nao aceita guardar coisas dentro de posicoes que nao existem ainda
        # entao crie a posicao e adicione o elemento
        except:
            matrizsoma.append(lista[posicao])

    # avanca o contador para os proximos elementos de todas as listas
    posicao = posicao + 1

# imprime os resultados na tela
print (matrizsoma)