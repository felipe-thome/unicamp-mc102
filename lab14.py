#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 — Caminho Binário Alternado
# Nome: Felipe Cardoso Thomé
# RA: 247510
#####################################################

def get_cores(tab):
    c = {}
    x = 0
    while x < len(tab) * len(tab[0]):
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                c[str(x)] = int(tab[i][j])
                x += 1
    return c

    # Essa função armazena as cores de cada casa do tabuleiro


def renomeia_tabuleiro(tab):
    x = 0
    while x < len(tab) * len(tab[0]):
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                tab[i][j] = x
                x += 1
    return tab

    # Essa função troca as cores do tabuleiro por indices iteráveis


def pode_direita(tab, cor, i, j):
    try:
        casa_atual = str(tab[i][j])
        casa_da_direita = str(tab[i][j + 1])
        if cor[casa_da_direita] != cor[casa_atual]:
            return True
        else:
            return False
    except IndexError:
        return False

    # Essa função testa se a casa da direita é viável


def pode_esquerda(tab, cor, i, j):
    try:
        casa_atual = str(tab[i][j])
        casa_da_esquerda = str(tab[i][j - 1])
        if j == 0:
            return False
        elif cor[casa_da_esquerda] != cor[casa_atual]:
            return True
        else:
            return False
    except IndexError:
        return False

    # Essa função testa se a casa da esquerda é viável


def pode_cima(tab, cor, i, j):
    try:
        casa_atual = str(tab[i][j])
        casa_cima = str(tab[i - 1][j])
        if i == 0:
            return False
        elif cor[casa_cima] != cor[casa_atual]:
            return True
        else:
            return False
    except IndexError:
        return False

    # Essa função testa se a casa de cima é viável


def pode_baixo(tab, cor, i, j):
    try:
        casa_atual = str(tab[i][j])
        casa_baixo = str(tab[i + 1][j])
        if cor[casa_baixo] != cor[casa_atual]:
            return True
        else:
            return False
    except IndexError:
        return False

    # Essa função testa se a casa de baixo é viável


def get_vizinhos(tab, c):
    v = [[] for _ in range(len(tab) * len(tab[0]))]
    x = 0
    while x < len(tab) * len(tab[0]):
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                if pode_direita(tab, c, i, j):
                    v[x].append(tab[i][j + 1])
                if pode_esquerda(tab, c, i, j):
                    v[x].append(tab[i][j - 1])
                if pode_cima(tab, c, i, j):
                    v[x].append(tab[i - 1][j])
                if pode_baixo(tab, c, i, j):
                    v[x].append(tab[i + 1][j])
                x += 1
    return v

    # Essa função constrói uma lista com cada vértice
    # conectado ao vértice de origem.


def busca(grafo, vertice, lista_visitados):
    lista_visitados.append(vertice)
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            busca(grafo, vizinho, lista_visitados)
    return lista_visitados


# Leitura da Entrada
L = int(input())
tabuleiro = [input().split() for _ in range(L)]
l1, c1, l2, c2 = (int(i) for i in input().split())

# Armazena cores
cores = get_cores(tabuleiro)

# Renomeia casas
renomeia_tabuleiro(tabuleiro)
casa_inicial = tabuleiro[l1][c1]
casa_final = tabuleiro[l2][c2]

# Armazena vizinhos
vizinhos = get_vizinhos(tabuleiro, cores)

# Busca
visitados = []
visitados = busca(vizinhos, casa_inicial, visitados)

encontrou = False
if casa_final in visitados:
    encontrou = True

# Impressão da resposta
if encontrou:
    print("caminho encontrado")
else:
    print("caminho nao encontrado")
