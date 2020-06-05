email = 'andre@email.com'
senha = '123456'

emailDigitado = input('Digite aqui o seu email\n')
senhaDigitada = input('Digite aqui sua senha\n')

if email == emailDigitado:
    if senha == senhaDigitada:
        print('Usuario logado')
    else:
        print('Senha digitada está incorreta')
else:
    print('Email digitado está incorreto')
