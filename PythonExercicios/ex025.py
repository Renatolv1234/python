nome = str(input('Qual seu nome completo? ')).strip()

nome_cap = nome.lower()
silva = 'silva' in nome_cap

print('Você possui "Silva" no nome?\n{}'.format(silva))

