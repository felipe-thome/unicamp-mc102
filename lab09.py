###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Felipe Cardoso Thomé
# RA: 247510
###################################################

# Leitura de entrada
lista = []
produtos = []
operacao = []
N = input()
while N != "FIM":
    lista.append(N.split(" : "))
    N = input()

for elemento in lista:
    produtos.append(elemento[0])
    operacao.append(int(elemento[1]))

lista = list(zip(produtos,operacao))

#Processamento do estoque
estoque = {}
vendas = {}
compras = {}

for pedido in lista:
    estoque[pedido[0]] = 0
    compras[pedido[0]] = 0
    vendas[pedido[0]] = 0

for pedido in lista:
    if pedido[1] < 0:
        if estoque[pedido[0]] < pedido[1]*-1:
            print("Quantidade indisponivel para a venda de {} unidade(s) do produto {}.".format(pedido[1]*-1,pedido[0]))
        else:
            estoque[pedido[0]] += pedido[1]
            vendas[pedido[0]] += 1
    else:
        estoque[pedido[0]] += pedido[1]
        compras[pedido[0]] += 1

for produto in sorted(estoque):
    if compras[produto] or vendas[produto]:
        print("Produto: {}".format(produto))
        print("Quantidade em Estoque: {}".format(estoque[produto]))
        print("Pedidos de Compra: {}".format(compras[produto]))
        print("Pedidos de Venda: {}".format(vendas[produto]))