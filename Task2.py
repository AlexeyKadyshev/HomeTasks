﻿#Задача 2: Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |

number = int(input("Введите трёхзначное число: "))
if 99 < number < 1000 :
    num3 = number % 10
    num2 = number // 10 % 10
    num1 = number // 100
    print(num1 + num2 + num3)
else:
    print("Введено некорректное число")