my_list = list(range(1, 101))
new_list1 = [i * 10 if i % 4 == 0 else i * 2 for i in my_list if i % 10 == 0]
print(new_list1)
