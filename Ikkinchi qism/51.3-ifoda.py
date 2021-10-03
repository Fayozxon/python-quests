# Ifodani hisoblash
# d=1*2+2*3+...+(n–1)*n
print('n >= 2')
n = int(input('n: '))

d = 0

# Sikl:
for i in range(1, n-1):
    s = i*(i+1)
    d+=s

print(d)