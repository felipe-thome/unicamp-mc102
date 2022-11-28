##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Felipe Cardoso Thomé
# RA: 247510
##################################################

# Leitura do valor da hora
valor_hora = int(input())

# Leitura do numero de dias trabalhados na semana
dias = int(input())

# Leitora e processamento dos periodos de trabalho de cada dia

horas_trabalhadas = 0
horas_extras = 0

while dias != 0:
    horas_dia = 0
    periodos = int(input())

    while periodos != 0:
        inicio = int(input())
        final = int(input())
        horas_dia += (final - inicio)
        periodos -= 1

    if horas_dia > 8:
        horas_extras += horas_dia - 8
    horas_trabalhadas += horas_dia
    dias -= 1

horas_regulares = horas_trabalhadas - horas_extras
if horas_regulares > 44:
    horas_extras += horas_regulares - 44

# valor a ser pago
valor = horas_trabalhadas * valor_hora + horas_extras * valor_hora / 2

# impressão da saída
print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))
