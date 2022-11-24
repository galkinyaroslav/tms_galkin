# 1
string1 = input('введите 2 слова ').split(sep=' ')
print(f'!{string1[1]} ! {string1[0]}!')
print('{}{}{}{}{}'.format('!', string1[1], ' ! ', string1[0], '!'))
print('{0}{1}{2}{3}{4}'.format('!', string1[1], ' ! ', string1[0], '!'))
