nome = str(input('Qual seu nome? ')).strip()

print('Analisando seu nome...')
print('Seu nome em maiúsculas {}'.format(nome.upper()))
print('Seu nome em minúsculas {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome) - nome.count(" ")))

#print('Seu primeiro nome tem {} letras'.format(nome.find(" ")))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(nome, len(separa[0])))