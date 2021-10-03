import time

# 30dan katta, 90dan kichik 6ga karrali sonlar:

print('30dan 90gacha bo\'gan 6ga karrali sonlar:')

for son in range(31, 90):
    if son%6==0:
        print(son)
        time.sleep(0.5)
