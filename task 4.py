'''
Дан текст. Вывести его построчно по 40 символов в строке без переноса
'''
text = input()
words = text.split()
answer = ""
    
for word in words:
    if len(answer) + len(word) + 1 < 41:
         answer += word + " "
         
    else:
        print(answer)
        answer=""
print(answer)


'''
яблоко банан груша помидор апельсин помело мандарин огурец тыква перец авокадо кабачок брокколи клебника земляника
яблоко банан груша помидор апельсин 
мандарин огурец тыква перец авокадо 
брокколи клебника земляника
'''