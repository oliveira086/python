numeroFuncionario = int(input('Qual o numero do funcionario?\n'))
horasTrabalhadas = float(input('Qual o total de horas trabalhadas?\n'))
valorPorHora = float(input('Qual o valor que o funcionario recebe por hora?\n'))

salario = horasTrabalhadas * valorPorHora

print('Numero = {}\nSalario = R$ {:.2f}'.format(numeroFuncionario, salario))