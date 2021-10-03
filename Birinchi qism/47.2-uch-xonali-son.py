# Uch xonali son:
a = int(input('Uch xonali son: '))

# Xona raqamlarini olish:
a_1 = a//100
a_2 = (a%100)//10
a_3 = a%10

# Tekshirish:
if a_1 == a_2 or a_2 == a_3 or a_1 == a_3:
    print('Bir xil raqamlar mavjud')
else:
    print('Bir xil raqamlar mavjud emas')