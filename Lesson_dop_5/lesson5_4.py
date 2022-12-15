from datetime import datetime
import time


def datetime_1s():
    print('Waiting...')
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


n = input('Input number of elements>> ')
while not n.isdigit():
    n = input('Try again. Input number of elements>> ')
list_of_dates = [datetime_1s() for _ in range(int(n))]

print(list_of_dates)
