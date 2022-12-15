def number_filter(str_number: str):
    polar_cout = 0
    dot_count = 0
    digit_count = 0
    err_count=0
    for idx, val in enumerate(str_number): # TODO можно еще добавить проверку для экспоненциальных чисел 123E+10
        # print(val,' >>> ',idx)
        if val.isdigit():
            digit_count += 1
        elif val == '.':
            dot_count += 1
        elif (val == '+' or val == '-') and idx == 0:
            polar_cout += 1
        else:
            err_count+=1
    if err_count==0:
        number = float(str_number)
        if dot_count == 0:
            print(True)
            if number < 0:
                print(int(number), ' >>> Вы ввели отрицательное целое число')
            else:
                print(int(number), ' >>> Вы ввели положительное целое число')
        elif dot_count == 1:
            if number < 0 :
                print(number, ' >>> Вы ввели отрицательное дробное число')
            else:
                print(number, ' >>> Вы ввели положительное дробное число')
    else:
            print(str_number, ' >>> Вы ввели некорректное число')

while True:
    num = input('Введите число: ')
    number_filter(num)
