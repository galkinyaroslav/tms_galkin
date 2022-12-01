num = 10  # 1*1*2*3*4*5=120


def fact(n: int) -> int:
    if n == 1:
        print('last val')
        return 1
    print(f'pre val n={n}')
    n *= fact(n - 1)
    print(f'post val n={n}')
    return n


result = fact(num)
print(f'result>>>{result}')
