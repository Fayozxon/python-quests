# a va b sonlar:
a = int(input('a: '))
b = int(input('b: '))

# Tekshirish:
if a < b:
    for i in range(a, b):
        print(i)
else:
    for i in range(a, b, -1):
        print(i)