###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome:
# RA:
###################################################

# Leitura de dados
extrato = {}
brancos = 0
nulos = 0
voto = input()
while voto != "0":
    if voto == "Branco":
        brancos += 1
    elif voto == "Nulo":
        nulos += 1
    elif voto not in extrato:
        extrato[voto] = 1
    else:
        extrato[voto] += 1
    voto = input()

# Saída de dados

for candidato in sorted(extrato, key = extrato.get, reverse = True):
    print(candidato,extrato[candidato])

print("Brancos {}".format(brancos))
print("Nulos {}".format(nulos))

