a = 'asdsa'
b = a[::-1]
assert a == b

str_list = ['ada','sdfg','qwe','wew','sdfghgfds','ertre']
res=filter(lambda x: x == x[::-1], str_list)
print(list(res))

