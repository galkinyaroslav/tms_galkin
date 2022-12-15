"""
Написать рекурсивную функцию, которая принимат на вход список целых чисел
и возвращает максимальное число в списке
"""


def recursive_max(some_list, maximum=0):
    if not some_list:
        return maximum
    else:
        if some_list[0] > maximum:
            maximum = some_list[0]
        return recursive_max(some_list[1:], maximum)


"""
Test
"""

source = [2, 1, 0, 5, 7, 6, 4, 3, 123 ,2345, 346, 4576,24,36]
print(source)
print(f'out {recursive_max(source)}')
assert recursive_max(source) == 4576
