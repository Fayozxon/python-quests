# a va b sonlar:
a = int(input('a son: '))
b = int(input('b son: '))

# Yig\indisi:
add = a + b
# Ko\paytmasi:
multiply = a * b

add_last = add%10
multiply_last = multiply%10

print('Yig\'indi va ko\'paytma oxirgi raqamlari ko\'paytmasi:')
print(add_last * multiply_last)
