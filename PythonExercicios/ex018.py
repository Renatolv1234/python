from math import radians, sin, tan, cos
ang = int(input('Digite um angulo: '))

sen = sin(radians(ang))
tang = tan(radians(ang))
cos = cos(radians(ang))

print('O seno de {} é {:.2f} \nA tangente de {} é {:.2f} \nO cosseno de {} é {:.2f}'.format(ang,sen,ang,tang,ang,cos))