# O'quvchilar soni
n = int(input('O\'quvchilar soni, n: '))
# Olmalar soni
k = int(input('Barcha olmalar soni, k: '))
# Har bir bolaga
once = k // n
# Qolgan olmalar
other = k % n

print('Har bir bola', once, 'tadan olma olgan')
print('Savatdagi qoldiq olmalar', other, 'ta')