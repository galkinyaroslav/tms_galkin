# 1
def my_list_reverse(old_list: list) -> list:
    new_list = []
    tmp_counter_list = []
    counter = -1
    for item in old_list:
        tmp_counter_list.append(counter)
        new_list.append(item)
        counter -= 1
    for item in tmp_counter_list:
        new_list[item] = old_list[-item - 1]
    return new_list


my_list = list(range(11, 61))
# my_reverse_list = [my_list[-idx - 1] for idx, val in enumerate(my_list)]
# print(my_reverse_list)
# my_list.reverse()  # built-in function REVERSE
# assert my_list == my_reverse_list
# my_reverse_list2 = my_list[::-1]
# print(my_reverse_list2)
my_reverse_list3 = my_list_reverse(my_list)
print(f'my_reverse_list3>>>{my_reverse_list3}')
