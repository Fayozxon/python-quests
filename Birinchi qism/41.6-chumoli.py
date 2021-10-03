# Chumolining bodib o'tgan yo'li, mm:
n = int(input('Yo\'l, mm\'da: '))
# Necha metr:
m = n//1000
n%=1000
# Necha sm:
sm = n//10
n%=10

print(f'{m} metr, {sm} santimetr, {n} millimetr')