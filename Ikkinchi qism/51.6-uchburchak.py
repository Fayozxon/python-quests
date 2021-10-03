# n ta uchburchak chiqaruvchi dastur:
print('son > -1 va son < 9')
n = int(input('Uchburchaklar soni: '))

# Tekshirish:
if n > -1 and n < 9:
    for i in range(n):
        print('   *')
        print('  * *')
        print(' * * *')
        print('* * * *')
else:
    print('Siz shartga amal qilmadingiz!')