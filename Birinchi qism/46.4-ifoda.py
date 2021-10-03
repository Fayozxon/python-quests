# a, b va c:
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

bool = a**2 - b**2 == c**2

# Tekshirish:
if bool:
    print('Ko\'paytmasi: ', a*b*c)
else:
    print('Yig\'idisi:', a+b+c)