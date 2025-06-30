peso = float (input('Digite seu peso: '))
altura = float (input('Digite sua altura: '))

imc = peso / altura**2

if imc < 18.5:
    print('Você está abaixo do peso!!')
elif imc >= 18.5 and imc < 24.99:
    print('Você está normal')
elif 25 <= imc < 29.9:
    print('Você está com sobrepeso!!')
else:
    print('Você está obeso!!')