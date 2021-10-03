# Bog'dagi olmalardan
a = int(input('Anvar tergan olmalar, a: '))
b = int(input('Dilshod tergan olmalar, b: '))
c = int(input('Mahmud tergan olmalar, c: '))

all = a + b + c
once = all//3
other = all%3

print('Har bir kishiga', once, 'dona')
print('Qolgan olmalar', other)