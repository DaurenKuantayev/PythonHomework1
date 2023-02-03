# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

print('Введите номер билетика')
LuckyTicket = int(input())
x = LuckyTicket
result = []
while x > 0:
    result.append(x % 10)
    x //= 10
result.reverse() #Можно и без него
SummFirstPart = int(result[0]+result[1]+result[2])
SummSecondPart = int(result[3]+result[4]+result[5])
if SummFirstPart == SummSecondPart:
    print(LuckyTicket, '-> yes')
else: 
    print(LuckyTicket, '-> no')
