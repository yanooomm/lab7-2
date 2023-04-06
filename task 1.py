'''
Вводится строка. Вывести, являетлся ли она корректным адресов эл. почты
'''

num = '.-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph = 'abcdefghijklmnopqrstuvwxyzvABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=input('Введите адрес эл почты: ')
answer = 1

if s[(s.find('@'))+1] in alph:
    answer *=1
else:
    answer *= 0

if s.count('@') == 1 and s.find('.') != 0 and s.find('-') != 0 and s.count(' ') == 0:
    for i in range(len(s)):
        x = s[i]
        if x.isdigit() or x in num:
            answer *= 1
        else:
            answer *= 0
else:
    answer *= 0
    
if answer == 1:
    print('Адрес введен корректно')
else:
    print('Адрес введен некорректно')


'''
Введите адрес эл почты: pochta@mail.ru
Адрес введен корректно

Введите адрес эл почты: .pochta@mail.ru
Адрес введен некорректно

Введите адрес эл почты: pochta?2mail.ru
Адрес введен некорректно

Введите адрес эл почты: pochta @mail.ru
Адрес введен некорректно

Введите адрес эл почты: pochta@mail,ru
Адрес введен некорректно
'''