# a va b sonlar:
a = int(input('a: '))
b = int(input('b: '))

bool = a > 0 and b > 0

if  bool and a+b >= 100:
    print('a sonnig b songa nisbati:')
    print(b / a)
elif bool and a+b < 100:
    print('a va b ko\'paytmasi:')
    print(a*b)