###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Felipe Cardoso Thomé
# RA: 247510
###################################################

# Leitura da palavra
palavra = input()

# Leitura dos palpites e impressão do resultado para cada palpite
tentativas_tot = 6
tentativa = 0
acertou = False
while tentativa < tentativas_tot and not acertou:
    palpite = input()
    resposta = []
    letra = 0
    while letra < len(palavra):
        if palpite[letra] == palavra[letra]:
            resposta.append(palpite[letra].upper())
        elif palpite[letra] in palavra:
            resposta.append(palpite[letra].lower())
        else:
            resposta.append("_")
        letra += 1
    resposta = "".join(resposta)
    print(resposta)
    if resposta == palavra.upper():
        acertou = True
    tentativa += 1

# Impressão da linha final
if acertou:
    print("Resposta correta")
else:
    print("Palavra correta:", palavra)