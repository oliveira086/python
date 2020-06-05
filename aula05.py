#calcular o ganho ou a perca no mini indice
entrada = int(input('Qual o valor do indice na entrada?\n'))
saida = int(input('Qual o valor do indice na saida?\n'))
saldo = entrada - saida
valor = saldo * 0.20

operacao = input('A sua operação foi de:\n[ 1 ] Compra ou [ 2 ] Venda?\n')

if valor < 0:
    valor = valor * -1
    if operacao == 1:
        if entrada > saida:
            print(f'A sua compra teve o saldo de R$ {valor}')
        else:
            print(f'A sua compra teve o saldo de R$ - {valor}')
    else:
        if entrada > saida:
            print(f'A sua compra teve o saldo de R$ {valor}')
        else:
            print(f'A sua compra teve o saldo de R$ - {valor}')
else:
    if operacao == 1:
        if entrada > saida:
            print(f'A sua compra teve o saldo de R$ {valor}')
        else:
            print(f'A sua compra teve o saldo de R$ - {valor}')
    else:
        if entrada > saida:
            print(f'A sua compra teve o saldo de R$ {valor}')
        else:
            print(f'A sua compra teve o saldo de R$ - {valor}')
