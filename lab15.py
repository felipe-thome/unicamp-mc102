#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 — Caça-Palavras
# Nome: Felipe Cardoso Thomé
# RA: 247510
#####################################################

# Aux Functions
def print_matriz(m):
    for linha in m:
        print(linha)


def print_resultado(r):
    for key in r:
        print("Palavra {}: {}".format(key,r[key]))


# Main Functions
def get_tabela():
    matriz = []
    entrada = input()
    while entrada != "0":
        linha = [letra for letra in entrada]
        matriz.append(linha)
        entrada = input()
    return matriz


def get_palavras():
    lista = []
    entrada = input()
    while entrada != "0":
        lista.append(entrada)
        entrada = input()
    return lista


def linha_coluna(tab, i, j):
    letras = []
    for x in range(len(tab)):
        letras.append(tab[x][j])
    for y in range(len(tab[0])):
        letras.append(tab[i][y])
    return letras


def get_vizinhos(tab):
    vizinhos = {}
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            letra = tab[i][j]
            if letra not in vizinhos:
                vizinhos[letra] = set([le for le in linha_coluna(tab, i, j)])
            else:
                for le in linha_coluna(tab, i, j):
                    vizinhos[letra].add(le)
    print(vizinhos)
    return vizinhos


def vizinhos_palavra(p, g):
    g_p = {}
    i = 0
    for letra in p:
        i += 1
        g_p[str(i)] = g[letra]
    return g_p


def primeira_letra(p):
    return p[0]


def busca(grafo, vertice, lista_visitados, verifica):
    for vizinho in grafo[vertice]:
        if vizinho not in lista_visitados:
            busca(grafo, vizinho, lista_visitados)

    return lista_visitados


def procura_palavras(l_p, g):
    print(l_p)
    r = {}
    for p in l_p:
        l_v = []
        verifica = [False] * len(p)
        lista_visitados = busca(g, p[0], l_v, verifica)


# Programa
tabela = get_tabela()
# palavras = get_palavras()
# grafo = get_vizinhos(tabela)
# resultados = procura_palavras(palavras, grafo)
# print_resultado(resultados)

get_vizinhos(tabela)