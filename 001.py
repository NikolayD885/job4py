# Вычислить число c заданной точностью *d*
# Пример: при d = 0.001, π = 3.141
#         при d = 0.1, π = 3.1
#         при d = 0.00001, π = 3.14154
#         при d от 0.1 до 0.0000000001

from decimal import Decimal, ROUND_FLOOR

d = input("Введите число для заданной точности числа Пи:  ")
pi = str(3.141592653589793238462643383279502884197)
number = Decimal(pi)
print(number.quantize(Decimal(d), ROUND_FLOOR))
print(d)
