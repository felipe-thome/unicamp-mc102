###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 — Redimensionamento de Imagens
# Nome: Felipe Cardoso Thomé
# RA: 247510
###################################################
def e_par(x):
    if x % 2 == 0:
        par = True
    else:
        par = False
    return par


def media(a, b):
    me = (a + b) / 2
    return me


def teto(n):
    if e_par(n):
        return n / 2
    else:
        return (n + 1) / 2


def media_lista(lista):
    a = 0
    for elemento in lista:
        a += elemento
    return a / (len(lista))


def get_submatrizes(matriz):
    n = len(matriz)
    m = len(matriz[0])

    if e_par(n) and e_par(m):
        submatrizes = {}
        i = 0
        while i < len(matriz):
            j = 0
            while j < len(matriz[0]):
                c = []
                for x in range(2):
                    for y in range(2):
                        c.append(matriz[i + x][j + y])
                submatrizes[(str(int(i / 2))) + " " + (str(int(j / 2)))] = c
                j += 2
            i += 2

    elif not e_par(n) and e_par(m):
        submatrizes = {}
        i = 0
        while i < len(matriz) - 1:
            j = 0
            while j < len(matriz[0]):
                c = []
                for x in range(2):
                    for y in range(2):
                        c.append(matriz[i + x][j + y])
                submatrizes[(str(int(i / 2))) + " " + (str(int(j / 2)))] = c
                j += 2
            i += 2
        i = len(matriz) - 1
        j = 0
        while j < len(matriz[0]):
            c = []
            for y in range(2):
                c.append(matriz[i][j + y])
            submatrizes[(str(int(i / 2))) + " " + (str(int(j / 2)))] = c
            j += 2

    elif e_par(n) and not e_par(m):
        submatrizes = {}
        i = 0
        while i < len(matriz):
            j = 0
            while j < len(matriz[0]) - 1:
                c = []
                for x in range(2):
                    for y in range(2):
                        c.append(matriz[i + x][j + y])
                submatrizes[(str(int(i / 2))) + " " + (str(int(j / 2)))] = c
                j += 2
            i += 2

        i = 0
        j = len(matriz[0]) - 1
        while i < len(matriz):
            c = []
            for x in range(2):
                c.append(matriz[i + x][j])
            submatrizes[(str(int(i / 2))) + " " + (str(int(j / 2)))] = c
            i += 2

    elif not e_par(n) and not e_par(m):
        submatrizes = {}
        i = 0
        while i < len(matriz) - 1:
            j = 0
            while j < len(matriz[0]) - 1:
                c = []
                for x in range(2):
                    for y in range(2):
                        c.append(matriz[i + x][j + y])
                submatrizes[(str(int(i / 2))) + " " + (str(int(j / 2)))] = c
                j += 2
            i += 2
        i = len(matriz) - 1
        j = 0
        while j < len(matriz[0]) - 1:
            c = []
            for y in range(2):
                c.append(matriz[i][j + y])
            submatrizes[(str(int(i / 2))) + " " + (str(int(j / 2)))] = c
            j += 2
        i = 0
        j = len(matriz[0]) - 1
        while i < len(matriz[0]) - 1:
            c = []
            for x in range(2):
                c.append(matriz[i + x][j])
            submatrizes[(str(int(i / 2))) + " " + (str(int(j / 2)))] = c
            i += 2
        i = len(matriz) - 1
        j = len(matriz[0]) - 1
        submatrizes[(str(int(i / 2))) + " " + (str(int(j / 2)))] = [matriz[i][j]]

    return submatrizes


def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))


def expansao(imagem):
    A = imagem
    n = len(imagem)
    m = len(imagem[0])
    B = []
    for x in range(2 * n - 1):
        linha = ["_" for _ in range(2 * m - 1)]
        B.append(linha)
    for i in range(n):
        I = i * 2
        for j in range(m):
            J = j * 2
            B[I][J] = A[i][j]

    for I in range(len(B)):
        for J in range(len(B[0])):
            if e_par(I) and not e_par(J):
                B[I][J] = media(B[I][J - 1], B[I][J + 1])
            elif not e_par(I) and e_par(J):
                B[I][J] = media(B[I - 1][J], B[I + 1][J])
            elif not e_par(I) and not e_par(J):
                B[I][J] = media_lista([B[I - 1][J + 1], B[I + 1][J - 1], B[I + 1][J + 1], B[I - 1][J - 1]])
    return B


def retracao(imagem):
    n = len(imagem)
    m = len(imagem[0])
    B = []
    for x in range(int(teto(n))):
        linha = ["_" for _ in range(int(teto(m)))]
        B.append(linha)
    submatrizes = get_submatrizes(imagem)
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] = media_lista(submatrizes[str(i) + " " + str(j)])
    return B


# leitura da imagem
_ = input()
m, n = [int(x) for x in input().split()]
_ = input()

imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

# leitura do redimensionamento
tipo = input()

# impressão final
if tipo == "expansao":
    imprimir_imagem(expansao(imagem_original))
elif tipo == "retracao":
    imprimir_imagem(retracao(imagem_original))
