'''
Uch xonali son xonalari yi'gindisi,
ko'paytmasini hisoblash:
'''

son = int(input('Uch xonali son: '))

son_1 = son//100
son_2 = (son%100)//10
son_3 = son%10

print('Xonalari ko\'paytmasi:', son_1 * son_2 * son_3)
print('Xonalari yig\'indisi:', son_1 + son_2 + son_3)
