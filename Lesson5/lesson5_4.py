from datetime import datetime
# from collections.abc import Callable

def decorator_function(func):
    time = datetime.now().microsecond
    func()
    time2 = datetime.now().microsecond
    print('execution time: ', func, time2 - time)

@decorator_function
def func1():
    list1=0*[100]


@decorator_function
def func2():
    list=[]
    for i in range(100):
        list.insert(0,i)
