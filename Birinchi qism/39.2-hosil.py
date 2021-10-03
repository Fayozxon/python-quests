# Bog'bon olgan hosil:
n = int(input('Hosil (kg): '))

n_1 = n # 2-topshiriq uchun

#1
# Hosilni tonna, sentner va kg'da ifodalash:
t = n//1000
n %= 1000
sr = n//100
n %= 100

print(f'{t} tonna {sr} sentner {n} kg')

#2
# Yashikka 25 kg uzum ketsa
# Solingan uzum nechta yashikka ketgan?

s = n_1//25

print(s, 'ta yashikka solingan')