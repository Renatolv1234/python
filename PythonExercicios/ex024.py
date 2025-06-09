cid = str(input('Qual cidade você mora? ')).strip()

cid_cap = cid.capitalize()
santo = 'Santo' in cid_cap

print('O nome da sua cidade começa com "Santo"?\n{}'.format(santo))