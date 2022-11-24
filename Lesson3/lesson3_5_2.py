import math
import datetime

inputted_lim = int(input('Input a random limit '))
target = math.floor(datetime.datetime.now().microsecond * inputted_lim / 1000000)
print(target)
while True:

    inputted_num = int(input('Input number '))
    print(f'inputted_num {inputted_num}')
    if target == inputted_num:
        print('u r in target')
        break
    else:
        print('Let\'s try again')
        continue
