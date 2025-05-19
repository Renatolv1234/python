medida = float(input('Digite um valor em metros: '))
km = medida / 10000
hm = medida / 1000
dam = medida / 100
dm = medida * 10
cm = medida * 100
mm = cm * 1000
print('Seu valor em metros {},  \nEm Quilômetros {}, \nEm Hectômetro {}, \nEm Decâmetro {} , \nEm Decimetro {}, \nEm centimetros {} \nE em milimetros {}'.format(medida,km,hm,dam,dm, cm, mm))
