"""
Написать рекурсивную функцию, которая будет принимать на вход список целых чисел
и возвращать инвертированную копию этого списка (рекурсивная реализация функции reverse)
"""

def recursive_reverse(source_list: list)-> list:
    if not source_list:
        return []
    else:
        return [source_list[-1]]+recursive_reverse(source_list[:-1])




"""
Test
"""

source = [1, 2, 3, 4, 5]
print(f'source{source}')
print(recursive_reverse(source))
assert recursive_reverse(source) == [5, 4, 3, 2, 1]

