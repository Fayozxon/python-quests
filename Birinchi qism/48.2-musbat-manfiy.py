# a, b va c
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

# Mubatlar sni:
d = 0
# Manfiylar soni:
k = 0

# Tekshirish:
if a > 0:
    d+=1
elif a < 0:
    k+=1

if b > 0:
    d+=1
elif b < 0:
    k+=1

if c > 0:
    d+=1
elif c < 0:
    k+=1


print('Musbatlar soni:', d)
print('Manfiylar soni:', k)