# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
# Пример: 47756688399943 -> [5]
#         1113384455229 -> [8,9]
#         1115566773322 -> []

uniqueList = {}
uniqueNumbers = ""

listA = "".join(list(map(str, input("Введите элементы: ").split())))

for c in listA:
    if uniqueList.get(c):
        uniqueList[c] += 1
    else:
        uniqueList[c] = 1

for i in uniqueList.items():
    if i[1] == 1:
        uniqueNumbers += str(i[0])

print(f"Неповторяющиеся элементы: {uniqueNumbers}") if uniqueNumbers else print("Неповторяющихся элементов нет")
