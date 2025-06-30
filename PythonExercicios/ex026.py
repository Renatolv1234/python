frase = input('Escreva uma frase: ').strip().upper()
print('Na frase a letra A aparece {} vezes'.format(frase.count("A")))
print('Na frase a letra A aparece na posição {} pela primeira vez'.format(frase.find("A")+1))
print('Na frase a letra A aparece na posição {} pela ultima vez'.format(frase.rfind("A")+1))