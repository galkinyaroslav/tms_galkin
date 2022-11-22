# 1
variable1 = '1234'
print(f'1:{id(variable1)}')
variable1 = '1234'
print(f'2:{id(variable1)}')
variable1 = '1234'
print(f'3:{id(variable1)}')

# 2
variable2 = '1234'
variable3 = '1234'
assert id(variable2) == id(variable3)
print(f'2_2:{id(variable2)}, 2_3:{id(variable3)}')

# 3
variable1_1 = int(variable1)
print(f'3:{id(variable1_1)}')
variable1_2 = float(variable1)
print(f'3:{id(variable1_2)}')
variable1_3 = str(variable1)
print(f'3:{id(variable1_3)}')
variable2_1 = int(variable2)
print(f'3_2:{id(variable2_1)}')
variable2_1 = int(variable3)
print(f'3_3:{id(variable2_1)}')

# 4
inputted_string = input('Input string:')
odd = ''.join([inputted_string[index] for index in range(len(inputted_string)) if index % 2 == 0])
even = ''.join([inputted_string[index] for index in range(len(inputted_string)) if index % 2 == 1])
print(f'Inputted string:{inputted_string.strip()}', end='\n\n')
print(f'odd:{odd}', f'even:{even}', sep='     ', end='\n!!!')
