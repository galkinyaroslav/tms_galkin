# 2 3
while True:
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    if not age.isdigit() or int(age) <= 0:
        print('Ошибка, повторите ввод')
    elif int(age) < 10:
        print(f'Привет, шкет {name}?')
    elif int(age) < 18:
        print(f'Как жизнь, {name}?')
    elif int(age) < 100:
        print(f'Чего желате, {name}?')
    else:
        print(f'{name}, Вы лжете - в наше время столько не живут...')
