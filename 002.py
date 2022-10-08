# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите натуральное число: "))

ListA = []
count = 2
while number > 2:
    if number % count != 0:
        count += 1
    else:
        number //= count
        ListA.append(count)

print(ListA)
