#1. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
def MultyN():
    import random
    from functools import reduce    
    numb_N = int(input('Введите количество элементов списка \n'))
    if numb_N <= 0:
        print('Введите положительное число!\n')
    else:
        list_N = [random.randint(-numb_N,numb_N) for i in range(numb_N)]
        print(f'Исходный список: {list_N}')
        file_pos = open('file.txt', 'r', encoding='utf-8')
        data_pos = file_pos.readlines()
        file_pos.close()
        print(f'Позиции для перемножения: {[line.rstrip() for line in data_pos]}')
        list_for_multy = [list_N[int(el)] for el in [line.rstrip() for line in data_pos]]
        multy = reduce(lambda x, y: x * y, list_for_multy)
        print(f'Произведие равно {multy}')
       
MultyN()

#2. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.
def SumPosl():
    from functools import reduce
    numbPosl = int(input('Введите количество чисел последовательности \n'))
    if numbPosl <= 0:
        print('Необходимо ввести положительное число! \n ')
    else:
        listN = [round((1 + 1/i) ** i, 2) for i in range(1, numbPosl+1)]
        sum = reduce(lambda x, y: x + y, listN)
        print(f'Последовательность: {listN}, сумма чисел последовательности равна {sum}')

SumPosl()

#3. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def SumNechet():
    from functools import reduce
    numb_spis = int(input('Введите количество элементов списка\n'))
    print('Введите элементы списка через клавишу Enter')
    spis =[int(input()) for i in range(numb_spis)]
    sum_spis = reduce(lambda x, y: x + y, list(filter(lambda el: el in spis and spis.index(el) % 2 != 0, spis)))
    print(f'Исходный список: {spis}')
    print(f'Сумма элементов, стоящих на нечетных позициях, равна {sum_spis}')

SumNechet()

#4. Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.
#*Пример: Для N = 5: 1, -3, 9, -27, 81
def Degree():
    n = int(input('Введите число больше нуля:\n'))
    osnov = -3
    if (n <= 0):
        print('Введите число больше нуля!!!')
    else:
        print(list(map(lambda i: osnov ** i, [i for i in range(n)])))

Degree()

#5. Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
#*Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def Posled():
    n = int(input('Введите число больше нуля:\n'))
    ind = [i for i in range(1,n+1)]
    if (n <= 0):
        print('Введите число больше нуля!!!')
    else:
        print(*zip(ind, map(lambda i: 3*i + 1, [i for i in range(1,n+1)])))

Posled()



