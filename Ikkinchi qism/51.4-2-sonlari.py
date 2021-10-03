# Bir nechta sonlar ichidan 2 soni nechta ekanligini topish:
# Sonlar:
n = input('Sonlarni probel bilan kiriting: ').split()
# 2 lar soni:
s = 0
# Sikl:
for i in range(len(n)):
    if int(n[i]) == 2:
        s+=1

print('2 lar soni:', s, 'ta')