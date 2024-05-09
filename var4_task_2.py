"""Распечатать все четырехзначные числа, в записи 
которых нет повторяющихся цифр, и
вывести их количество. Ограничений по 
использованию циклов и массивов нет."""


count = 0

for i in range(1000, 10000):
    num_list = list(str(i))
    if len(num_list) == len(set(num_list)):
        print(i)
        count += 1

print("Количество четырехзначных чисел без повторяющихся цифр:", count)