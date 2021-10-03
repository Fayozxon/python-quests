# Hovuz:
height = int(input('Balandligi: ')
width = int(input('Kengligi: ')
deepth = int(input('Chuqurligi: ')

#1
# Hovuzga qoplash uchun necha kv. m kafel kerak?
surface_1 = width * height
surface_2 = deepth * height * 2
surface_3 = deepth * width * 2

surface = surface_1 + surface_2 + surface_3
print(surface, 'kv. m kafel kerak')

#2
# Hovuzni to'ldirish uchun qancha suv kerak?
# 1l = 10 kv m
volume = height * width * deepth
water = volume * 10
print('To\'dirish uchun:', water, 'litr suv kerak')
