# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов: 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
#                                   17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
# Результат:                        40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

polynomial1 = ''
polynomial2 = ''
with open('polynomial.txt', 'r') as data:
    polynomial1 = (data.readline().replace(' + ', ' +').replace(' - ', ' -')).replace('x ', 'x^1 ').replace('.0', 'x^0').split()[:-2]
    polynomial2 = (data.readline().replace(' + ', ' +').replace(' - ', ' -')).replace('x ', 'x^1 ').replace('.0', 'x^0').split()[:-2]
#print(polynomial1)
#print(polynomial2)

firstEquation = polynomial1
Polynomial1 = {}

for i in range(len(polynomial1)):
    firstEquation[i] = firstEquation[i].replace("+", "").split("x^")
    Polynomial1[int(firstEquation[i][1])] = int(firstEquation[i][0])
#print(Polynomial1)

secondEquation = polynomial2
Polynomial2 = {}

for i in range(len(polynomial2)):
    secondEquation[i] = secondEquation[i].replace("+", "").split("x^")
    Polynomial2[int(secondEquation[i][1])] = int(secondEquation[i][0])
#print(Polynomial2)

sumPolinomial = {}

for i in range(max(len(Polynomial1), len(Polynomial2)), -1, -1):
    first = Polynomial1.get(i)
    second = Polynomial2.get(i)
    if first != None or second != None:
        sumPolinomial[i] = (first if first != None else 0) + \
            (second if second != None else 0)
#print(sumPolinomial)

SumPolinomial = ''
i = len(sumPolinomial) - 1

while i > -1:
    if sumPolinomial.get(i) > 0:
        SumPolinomial +=' + ' + str(sumPolinomial.get(i)) + 'x^' + str(i)
    elif sumPolinomial.get(i) < 0:
        SumPolinomial += (str(sumPolinomial.get(i)).replace('-', ' - ')) + 'x^' + str(i)
    i = i - 1
print(SumPolinomial.replace('x^1 ', 'x ').replace('x^0', '') + ' = 0')

with open(r'sumpolynomial.txt', 'w') as data:
    data.write(SumPolinomial.replace('x^1 ', 'x ').replace('x^0', '') + ' = 0')
    data.close