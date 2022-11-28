#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 — Encaixe 2D
# Nome: Felipe Cardoso Thomé
# RA: 247510
#####################################################

# rotação
def rotate(p, n=1):
    m = []
    if n == 0:
        m = p
        return m
    else:
        while n != 0:
            m = list(map(lambda *i: [j for j in i], *p))
            for linha in range(len(m)):
                m[linha].reverse()
            n -= 1
        return m


# encaixe
def fit(p, t):
    encaixes = 0
    for x in range((len(t) - len(p)) + 1):
        for y in range((len(t[0]) - len(p[0])) + 1):
            encaixou = True
            for i in range(len(p)):
                for j in range(len(p[0])):
                    if p[i][j] == t[i + x][j + y] == "X":
                        encaixou = False
            if encaixou:
                encaixes += 1
    return encaixes


# Leitura do tabuleiro
T = int(input())
tabuleiro = []
for _ in range(T):
    tabuleiro.append(input().split())

# Leitura da peça
P = int(input())
peca = []
for _ in range(P):
    peca.append(input().split())

# Processamento
resultado = []
for rotacao in range(4):
    peca_temp = rotate(peca, rotacao)
    resultado.append(fit(peca_temp, tabuleiro))
    peca = peca_temp

# Impressão do resultado
print(resultado[0], resultado[1], resultado[2], resultado[3], sep=",")
