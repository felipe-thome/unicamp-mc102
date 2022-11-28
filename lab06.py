##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Felipe Cardoso Thomé
# RA: 247510
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split()]
torre_estavel = torre.copy()
torre_estavel.sort()
# Leitura e processamento dos movimentos
M = 1
while M != 0:
    M = int(input())
    if M == 0:
        break
    espatula = torre[0:M]
    espatula.reverse()
    torre = espatula + torre[M:]

# Impressão da saída
if torre == torre_estavel:
    print("Torre estavel")
else:
    print("Torre instavel")