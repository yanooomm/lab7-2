'''
Вводится номер банковской карты, определить платежную систему
'''

num = input('Введите номер карты: ')
n1 = int(num[0])
n2 = int(num[1])
if n1 == 2 :
    print('MIR')
elif n1 == 3:
    if n2 == 0 or n2 == 6 or n2 == 8:
        print('Dinners Club')
    if n2 == 1 or n2 == 5:
        print('JSB International')
    if n2 == 4 or n2 == 7:
        print('American Express')
if n1 == 4:
    print('VISA')
if n1 == 5:
    if n2 == 0 or n2 == 6 or n2 == 7 or n2 == 8:
        print('Maestro')
    if n2 == 1 or n2 == 2 or n2 == 3 or n2 == 4 or n2 == 5:
        print('MasterCard')
if n1 == 6:
    if n2 == 0:
        print('Discover')
    if n2 == 2:
        print('China UnionPay')
    if n2 == 3 or n2 == 7:
        print('Maestro')
if n1 == 7:
    print('УЭК')
    
'''
ведите номер карты: 4325432109876543
VISA

Введите номер карты: 6234543234565432
China UnionPay
'''