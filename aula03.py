# numero = int(input('Qual o numero que deseja adicionar?\n'))
# dobro = numero*2
# triplo = numero*3
# raiz = numero**(1/2)

# print('O numero que você digitou é {}, seu dobro e igual a {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(numero, dobro, triplo, raiz))

temperaturaCelsius = float(input('Qual a temperatura atual em celsius?\n'))
conversao = (temperaturaCelsius * (9/5)) + 32

print(f'A sua temperatua atual em celsius é {temperaturaCelsius}\nE sua temperatura atual em fareheint é {conversao}')

if temperaturaCelsius > 10:
    print('E maior que 10')
else:
    print('Outros valores')

