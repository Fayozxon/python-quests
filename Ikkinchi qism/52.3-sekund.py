# Sekund:
n =  int(input('Sutkaning n sekundi: '))

# Soat:
h = n//3600
n%=3600
min = n//60
n%=60

print(f'Sutka boshlangandan beri {h} soat, {min} minut, {n} sekund o\'tdi')