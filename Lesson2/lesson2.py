# 1
variable1 = '1234'
print(f'1:{id(variable1)}')
variable1 = '1234'
print(f'2:{id(variable1)}')
variable1 = '1234'
print(f'3:{id(variable1)}')

"""
Здесь идентификатор - значит адрес объекта в памяти, получемый через вызов id
В данном задании результат должен быть типа: 
variable1_1 = '1234'
variable1_2 = '1234'
variable1_3 = '1234'

разные переменные, но одинаковые идентификаторы
"""


# 2
variable2 = '1234'
variable3 = '1234'
assert id(variable2) == id(variable3)
print(f'2_2:{id(variable2)}, 2_3:{id(variable3)}')

"""
Здесь по заданию должно быть 2 объекта с одинаковыми данныыми и РАЗНЫМИ идентификаторами

Например:
variable2 = ['1234']
variable3 = ['1234']
assert id(variable2) != id(variable3)
В данном задании результат должен быть типа: 
"""


# 3
print()
variable1_1 = int(variable1)
print(f'3:{id(variable1_1)}')
variable1_2 = float(variable1)
print(f'3:{id(variable1_2)}')
variable1_3 = str(variable1)  # можно было НЕ кастить к строке, так как variable1 изначально строка
print(f'3:{id(variable1_3)}')

variable2_1 = int(variable2)
print(f'3_2:{id(variable2_1)}')
variable2_1 = int(variable3)
print(f'3_3:{id(variable2_1)}')

"""
По заданию, у двух последних переменных идентификаторы НЕ должны меняться.
При приведении строки к int каждый раз создается новый целочисленный объект.

s = "5555555"
id(s)
139910701851056
id(int(s))
139910701283216
id(int(s))
139910701274640
id(int(s))
139910701278768

А вот если обернуть имеющуюся строку в str - объект будет тот же
s = "5555555"
id(s)
139910701851056
id(str(s))
139910701851056
id(str(s))
139910701851056
"""


# 4
inputted_string = input('Input string:')
odd = ''.join([inputted_string[index] for index in range(len(inputted_string)) if index % 2 == 0])
even = ''.join([inputted_string[index] for index in range(len(inputted_string)) if index % 2 == 1])
print(f'Inputted string:{inputted_string.strip()}', end='\n\n')
print(f'odd:{odd}', f'even:{even}', sep='     ', end='\n!!!')
"""
Здесь все должно быть гораздно проще :)

odd = inputted_string[::2]
even = inputted_string[1::2]

В остальном все OK
"""
