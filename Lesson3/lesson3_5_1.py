import random

inputted_lim = int(input('Input a random limit '))
rand = random.randint(1, inputted_lim)
print(rand)

while True:

    inputted_num = int(input('Input number'))
    print(f'inputted_num {inputted_num}')
    if rand == inputted_num:
        print('u r in target')
        break
    else:
        print('Let\'s try again')
        continue
