# 15ta butun son:

butun_sonlar = [23, -45, 12, 6, -9, 3, -34, 2, 10, -20, 56, 78, -90, 29, 11]

manfiy_sonlar = 0
musbat_sonlar = 0
uchga_karrali = 0

for i in butun_sonlar:
    if i < 0:
        manfiy_sonlar += i
    elif i > 0:
        musbat_sonlar += 1
        
    if i%3 == 0:
        uchga_karrali += 1

print('Manfiy sonlar yig\'indisi:', manfiy_sonlar)
print('Musbat sonlar soni:', musbat_sonlar)
print('Uchga bo\'linuvchi sonlar soni:', uchga_karrali)
