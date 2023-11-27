import random
import sys

try:
    n = int(input("Введите количество элементов: "))
    if n < 1:
        print("Кол-во элементов не может быть меньше единицы.")
        sys.exit()
    list1 = [0] * n
    for i in range(n):
        list1[i] = random.randint(-1000, 1000)
    print(list1)
    a = int(input("Введите левую границу диапазона: "))
    b = int(input("Введите правую границу диапазона: "))
    count = 0
    for i in list1:
        if a <= i <= b:
            count += 1
    print("Количесво элементом списка в введенном диапазоне: ", count)
    maxn = 0
    ind = 0
    for i in range(n):
        if maxn < list1[i]:
            maxn = list1[i]
            ind = i
    summ = 0
    for i in list1[ind+1:]:
        summ += i
    print("Сумма элементов после максимального: ", summ)
except ValueError:
    print("Неправильный тип данных.")

