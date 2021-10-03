# Son:
n = int(input('Natural son: '))


# Oxirgi raqamini aniqlash:
if n > 0:
    l = n%10
elif n < 0:
    l = -n%10
else:
    l = 0

print(f'{n} sonining oxirgi raqami - {l}')