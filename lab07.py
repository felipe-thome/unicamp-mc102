###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome: Felipe Cardoso Thomé
# RA: 247510
###################################################

# Leitura das tropas de defesa
n_defesa = int(input())
defesa = []
for tropa in range(n_defesa):
    defesa.append(int(input()))

# Leitura das tropas de ataque
n_ataque = int(input())
ataque = []
for tropa in range(n_ataque):
    ataque.append(int(input()))

# Processamento da guerra
posicao = 0
while len(defesa) >= len(ataque):
    vitorias = 0
    derrotas = 0
    for atacante in ataque:

        if atacante > defender:
            vitorias += 1
        else:
            derrotas += 1
    if vitorias > derrotas:
        venceu = True
        break
    else:
        venceu = False
    posicao += 1
    defesa.pop(0)

# Impressão da saída
if venceu:
    print('Vitória posicionando as tropas a partir da posição', posicao)
else:
    print("Derrota")