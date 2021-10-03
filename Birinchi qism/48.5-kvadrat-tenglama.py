# Kvadrat tenglama yechish dasturi:
# a, b va c:
print('a != 0')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

# Diskrimanant:
d = (b**2) - (4*a*c)

if d < 0 or a == 0:
    print('Tenglama yechimga ega emas!')
elif d == 0:
    x = -(b/(2*a))
    print('Javob: x =', x)
else:
    x1 = (-b + (d**(1/2)))/(2*a)
    x2 = (-b - (d**(1/2)))/(2*a)
    print('Javoblar:')
    print('x1 =', x1)
    print('x2 =', x2)