# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от-100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Пример: k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
#         k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


from random import randint as rI


def createEquation():
    k = int(input("Введите максимальную степень многочлена: "))
    polynomial = ''

    for i in range(k, -1, -1):
        ratio = rI(-100, 100)
        if i == k:
            if ratio > 0:
                polynomial += str(ratio) + 'x^' + str(i)
            if ratio < 0:
                polynomial += '-' + str(abs(ratio)) + 'x^' + str(i)
        else:
            if ratio > 0:
                polynomial += ' + ' + str(ratio) + 'x^' + str(i)
            if ratio < 0:
                polynomial += ' - ' + str(abs(ratio)) + 'x^' + str(i)

    return polynomial + ' = 0'


polynomial1 = createEquation()
print((polynomial1.replace('x^1 ', 'x ').replace('x^0', '')).replace(' 1x^', ' x^').replace('-1x^', '-x^'))
polynomial2 = createEquation()
print((polynomial2.replace('x^1 ', 'x ').replace('x^0', '')).replace(' 1x^', ' x^').replace('-1x^', '-x^'))

with open(r'polynomial.txt', 'w') as data:
    data.write(str(polynomial1.replace('x^1 ', 'x ').replace('x^0', '.0')).replace(' 1x^', ' x^').replace('-1x^', '-x^'))
    data.write('\n')
    data.write(str(polynomial2.replace('x^1 ', 'x ').replace('x^0', '.0')).replace(' 1x^', ' x^').replace('-1x^', '-x^'))
    data.close
