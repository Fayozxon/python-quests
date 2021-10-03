# Ifoda - n!/k!(n-k)!
# Sonlar:
print('Manfiy bo\'lmagan butun sonlar(n > k):')
n = int(input('n: '))
k = int(input('k: '))

ns = 1
ks = 1
nks = 1
# Sanagich:
i = 1
# Sikl:
while i <= n:
    ns*=i
    i+=1
i = 1
while i <= k:
    ks*=i
    i+=1
i = 1
while i <= n-k:
    nks*=i
    i+=1
# Ifoda:
s = ns/(ks*nks)

print('Javob:', s)