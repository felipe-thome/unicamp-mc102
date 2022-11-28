###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome:Felipe Cardoso Thomé
# RA:247510
###################################################

# leitura da sequência de compras e vendas
lista = [int(input())]
estoque = 0
vendas = 0

#loop
i=0
while lista[i] != 0:
    if lista[i] > 0:
        estoque += lista[i]
    elif lista[i] < 0 and -1*lista[i] <= estoque:
        estoque += lista[i]
        vendas += 1
    else:
        print('Quantidade indisponível para a venda de {} unidades.'.format(lista[i]*-1))
    lista.append(int(input()))
    i += 1

# impressão da saída
print('Quantidade de vendas realizadas: {}'.format(vendas))
print('Quantidade em estoque: {}'.format(estoque))